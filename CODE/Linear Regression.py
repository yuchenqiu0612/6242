# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 10:43:23 2023

@author: Jenny
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 
from featurewiz import featurewiz
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler, StandardScaler


np.random.seed(1234)

#load data
path = os.path.join(os.getcwd(), "sold_cleaned_11.21.23.csv")
data = pd.read_csv(path)

#inspect if data has any missing value
data.info()

#check data detailed info to see if any uncommon number
des=data.describe()


#drop unnecessary columns
data=data.drop(["property_url","mls","mls_id","status","street","unit","city","state","full_baths","half_baths","days_on_mls",\
                "list_price","list_date","last_sold_date","lot_sqft","latitude","longitude","stories","hoa_fee","parking_garage","metro_area"],axis=1)
    

# make label for categorical features
# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Fit and transform style,zipcode, year_built columns to categorical data 
data['style_encoded'] = label_encoder.fit_transform(data['style'].astype(str))    
data['zipcode_encoded'] = label_encoder.fit_transform(data['zip_code'].astype(str))
data['year_built_encoded'] = label_encoder.fit_transform(data['year_built'].astype(str))    

#drop style,zipcode, year_built columns
data=data.drop(["style","zip_code","year_built"],axis=1)

#plot historgram for all features
data.hist(bins=50,figsize=(20,15))

#check the correlation between each feature
corrDf = data.corr()
corrDf['sold_price'].sort_values(ascending=False)

#plot heatmap 
cmap = sn.diverging_palette(230, 20, as_cmap=True)
plt.figure(figsize=(30,10))
sn.heatmap(corrDf, annot=True,fmt=".1g",vmin=-1,vmax=1,center=0,cmap=cmap)
plt.title("Figure 2: Correlation Heatmap",fontsize="large")

#extract the highly correlated pairs with absolute correlation over 0.05
corr_pairs = corrDf.unstack()
highly_corr_pairs=corr_pairs[(abs(corr_pairs)>=0.3)&(abs(corr_pairs)<1)].sort_values()

#normalize data for numerica features(use MinMaxScaler, StandardScaler based on data distribution or other feature)
columns_to_minmax_scale = ['sqft', 'price_per_sqft','Occupied housing units Percent (%)','Vacant housing units Percent (%)',\
                           'Homeowner vacancy rate','Rental vacancy rate']  
columns_to_standardize = ['Household Median Income', 'Total population','age over 35 and less than 85','age over 35 and less than 85 percentage ',\
                         'Total housing units','Occupied housing units/ Totla Household','Owner-occupied','Renter-occupied',\
                           'Vacant housing units','related number of bedroom units','related number of bedroom  (%)']   

# Apply Min-Max scaling to selected columns
minmax_scaler = MinMaxScaler()
data[columns_to_minmax_scale] = minmax_scaler.fit_transform(data[columns_to_minmax_scale])

# Apply Standardization to selected columns
standard_scaler = StandardScaler()
data[columns_to_standardize] = standard_scaler.fit_transform(data[columns_to_standardize])


# Identify outliers using IQR
Q1 = data['sold_price'].quantile(0.25)
Q3 = data['sold_price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
data_filtered = data[(data['sold_price'] >= lower_bound) & (data['sold_price'] <= upper_bound)].copy()

# Apply log transformation using .loc to avoid SettingWithCopyWarning
data_filtered.loc[:, 'log_sold_price'] = np.log1p(data_filtered['sold_price'])


#set X and y
feature_cols=['beds', 'sqft', 'price_per_sqft', 'Household Median Income', 'Total population',
'age over 35 and less than 85', 'age over 35 and less than 85 percentage ', 'Total housing units', 'Occupied housing units/ Totla Household', 'Occupied housing units Percent (%)',
'Owner-occupied', 'Renter-occupied', 'Vacant housing units', 'Vacant housing units Percent (%)', 'Homeowner vacancy rate', 'Rental vacancy rate', \
    'related number of bedroom units','related number of bedroom  (%)', 'style_encoded', 'zipcode_encoded', 'year_built_encoded']

X=data_filtered[feature_cols]
y=data_filtered['log_sold_price']




from featurewiz import featurewiz
# automatic feature selection by using featurewiz package
data_for_feature_selection=pd.concat([X,y],axis=1)
target = 'log_sold_price'

features, train = featurewiz(data_for_feature_selection, target, corr_limit=0.7, verbose=2, sep=",",
header=0,test_data="", feature_engg="", category_encoders="")

#split data into feature and target
X_new = train.drop(['log_sold_price'],axis=1)
y_new = train.log_sold_price.values.astype(float)



#split data into 70% train and 30% test
X_train, X_test, y_train, y_test = train_test_split(X_new, y_new, test_size=0.3, stratify=None, random_state=1)



from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, median_absolute_error, mean_squared_log_error, r2_score, explained_variance_score

# Creating a multiple linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Model evaluation

# Calculating Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE): {mse:.4f}")

# Calculating Root Mean Squared Error (RMSE)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")

# Calculating Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae:.4f}")

# Calculating Median Absolute Error (MAD)
mad = median_absolute_error(y_test, y_pred)
print(f"Median Absolute Error (MAD): {mad:.4f}")

# Calculating Mean Squared Log Error (MSLE)
msle = mean_squared_log_error(y_test, y_pred)
print(f"Mean Squared Log Error (MSLE): {msle:.4f}")

# Calculating Root Mean Squared Log Error (RMSLE)
rmsle = np.sqrt(msle)
print(f"Root Mean Squared Log Error (RMSLE): {rmsle:.4f}")

# Calculating Explained Variance Score (EVS)
evs = explained_variance_score(y_test, y_pred)
print(f"Explained Variance Score (EVS): {evs:.4f}")

# Calculating R-squared (Coefficient of Determination)
r_squared = r2_score(y_test, y_pred)
print(f"R-squared (R^2) Score: {r_squared:.4f}")


def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape = mean_absolute_percentage_error(y_test, y_pred)
print(f"Mean Absolute Percentage Error (MAPE): {mape:.4f}%")



# Exponentiate the predictions to get them back on the original price scale
predictions = np.exp(y_pred)

# Exponentiate the actual log prices to get them back on the original price scale
actual_prices = np.exp(y_test)

# Calculate evaluation metrics on the original price scale
mse = mean_squared_error(actual_prices, predictions)
rmse = np.sqrt(mse)
mae = mean_absolute_error(actual_prices, predictions)
mad = median_absolute_error(actual_prices, predictions)


