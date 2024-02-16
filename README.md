User Guide: Real Estate Property Purchasing vs. Renting Valuation

DESCRIPTION 
This user guide provides instructions for using the programming tool to analyze real estate housing datasets using various machine learning models: XGBoost, Random Forest, KNN, BayesianRidge, ANN and Linear Regression models. The zip file package includes a DOC folder and a CODE folder:
a. The DOC folder contains our final report and poster files: team084report.pdf and team084poster.pdf.
b. The CODE folder contains all the necessary files for executing the project:

1. Four Excel/CSV files :
a. sold_cleaned_11.21.23.csv (this file is used to train and test various machine learning models)
b. for_sale_cleaned_up_11.21.23_updated.xlsx (the selected machine learning model will then be applied to this dataset to predict reasonable selling price for each property)a
c. for_rent_cleaned_up_11.22.23.csv (this file is used directly in the tableau visualization dashboard)
d. for_sale_predict_viz_final.xlsx (this file is the output of the our selected model - Random Forest predicted results by using the for_sale_cleaned_up_11.21.23_updated.xlsx dataset as input)

2. One Python file to scrape data and Four Python files that perform EDA, data wrangling, feature selection, and training/testing for each of our models: XGBoost, Randomforest, KNN, BayesianRidge, ANN and Linear Regression.
a. getData.py
b. XGBoost.ipynb
c. Randomforest_final.ipynb
d. KNN, BayesianRidge, and ANN.ipynb
e. Linear Regression.py

3. One Tableau file which is our final virtualization product - a user friendly interactive dashboard help users to make decision between purchasing and renting in each location in US.
a. 6242_Project_Final Visualiztion.twb	

	
INSTALLATION 
Download and install Python:
a.Visit https://www.python.org/downloads/
b.Select python version >= 3.10
c.Click on the appropriate download link for macOS or Windows.

Download and install Tableau:
1.Visit https://www.tableau.com/trial/tableau-online
2.Enter your information (name, email, GT details, etc.)
3.You will then receive an email to access your Tableau Online site


EXECUTION 
I. Scraping data:
a.Open Python
b.Install the web scraping library "homeharvest "by running the command "pip install homeharvest" in the terminal
c.Run the file "getData.py" to retrieve the raw data housing datasets, we expect to retrieve 3 datasets, one for already sold houses, one for on sales houses, and one for rental houses. 

Note: you can skip this scraping data procedure since we have provided the scraped dataset in the CODE folder:
	sold_cleaned_11.21.23.csv 
	for_sale_cleaned_up_11.21.23_updated.xlsx
	for_rent_cleaned_up_11.22.23.csv 

II. Running Model:
a. Open the Python environment and install the required libraries. Please ensure that you have installed the required Python libraries, including: 
	a.pandas
	b.matplotlib
	c.os
	d.seaborn
	e.numpy
	f.featurewiz
	g.scikit-learn (sklearn)	
	h.tensorflow
	i.xgboost

b. Download the sold_cleaned_11.21.23.csv dataset and run the provided Python code for each model:
	XGBoost.ipynb
	Randomforest_final.ipynb
	KNN, BayesianRidge, and ANN.ipynb
	Linear Regression.py

c. Observe the results. The output will display various metrics and visualizations related to the dataset and the effectiveness of the different models used in the analysis. We expect to see the following metrics: MSE, RMSE, MAE, MAPE, EVS and more. And following visualizations: histogram for all features, correlation heatmap, distribution of sold_price, boxplot for sold_price etc. 

d. Download the for_sale_cleaned_up_11.21.23_updated.xlsx dataset and run the Randomforest_final.ipynb Python code, and observe the results (We selected Randomforest as our final machine learning model). You can also find the output of this procedure in the CODE folder: for_sale_predict_viz_final.xlsx

III. Access to Dashboard:
For the Tableau file which is our final virtualization dashboard:
a.Sign in to the tableau site and from the Home or Explore pages, select New > Workbook Upload 
b.In the dialog that opens,select "Choose a file" to select the 6242_Project_Final Visualiztion.twb file from your computer or drag and drop a file into the upload area of the dialog
c.In the Name field, enter a name for your workbook. By default, the workbook will retain the name of the file
d.Choose a project where your workbook will be published, or leave as is to publish the workbook to the Default project
e.Select Upload

You can also find a demo of this tableau dashboard at https://www.youtube.com/watch?v=tbYkrp02Btc
