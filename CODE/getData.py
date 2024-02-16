from homeharvest import scrape_property
import pandas as pd

metro_dict = {"New York-Newark-Jersey City" : ['New York, NY', 'Newark, NJ', 'Jersey City, NJ', 'Hempstead, NY', 'Brookhaven, NY', 'Lslip, NY', 'Oyster Bay, NY', 'North Hempstead, NY', 'Babylon, NY', 'Huntington, NY', 'Yonkers, NY', 'Paterson, NJ', 'Elizabeth, NJ', 'Ramapo, NY', 'Smithtown, NY', 'Edison, NJ', 'Woodbridge Township, NJ', 'New Rochelle, NY', 'Mount Vernon, NY', 'White Plains, NY', 'Passaic, NJ', 'Union, NJ', 'Wayne, NJ'],
                "Los Angeles-Long Beach-Anaheim" : ['Los Angeles, CA', 'Long Beach, CA', 'Anaheim, CA', 'Santa Clarita, CA', 'Glendale, CA', 'Lancaster, CA', 'Palmdale, CA', 'Pomona , CA', 'Torrance, CA', 'Pasadena, CA', 'Downey, CA', 'West Covina, CA', 'El Monte, CA', 'Inglewood, CA', 'Burbank, CA', 'Norwalk, CA', 'Santa Ana, CA', 'Irvine, CA', 'Huntington Beach, CA', 'Garden Grove, CA', 'Fullerton, CA', 'Orange, CA', 'Costa Mesa, CA'],
                "Chicago-Naperville-Elgin" : ['Chicago, IL', 'Aurora, IL', 'Joliet, Illinois', 'Naperville, IL', 'Elgin, IL', 'Kenosha, Wisconsin', 'Waukegan, Illinois', 'Cicero, Illinois', 'Schaumburg, Illinois', 'Evanston, IL', 'Hammond, Indiana', 'Arlington Heights, Illinois', 'Bolingbrook, Illinois', 'Gary, Indiana', 'Palatine, Illinois', 'Skokie, Illinois', 'Des Plaines, Illinois', 'Orland Park, Illinois', 'Oak Lawn, Illinois', 'Berwyn, Illinois', 'Mount Prospect, Illinois', 'Tinley Park, Illinois', 'Oak Park, IL', 'Wheaton, Illinois', 'Downers Grove, Illinois'],
                "Dallas-Fort Worth-Arlington" : ['Dallas, TX', 'Fort Worth, TX', 'Arlington, TX', 'Plano, TX', 'Irving, TX', 'Garland, TX', 'Frisco, TX', 'McKinney, TX', 'Grand Prairie, TX', 'Denton, TX', 'Mesquite, TX', 'Carrollton, TX', 'Lewisville, TX', 'Richardson, TX', 'Allen, TX'],
                "Houston-The Woodlands-Sugar Land": ['Houston, TX', 'The Woodlands, TX', 'Sugar Land, TX', 'Pasadena, TX', 'Pearland, TX', 'League City, TX', 'Baytown, TX', 'Conroe, TX', 'Galveston, TX', 'Texas City, TX', 'Spring, TX', 'Missouri City, TX'],
                "Washington-Arlington-Alexandria" : ['Washington, D.C.', 'Arlington, VA', 'Alexandria, VA', 'Frederick, Maryland', 'Gaithersburg, Maryland', 'Rockville, Maryland', 'Bethesda, Maryland', 'Silver Spring, Maryland', 'Reston, Virginia'],
                "Miami-Fort Lauderdale" : ['Miami, FL', 'Fort Lauderdale, FL', 'Hialeah, FL', 'Pembroke Pines, FL', 'Hollywood, FL', 'Miramar, FL', 'Coral Springs, FL', 'Miami Gardens, FL', 'Pompano Beach, FL', 'West Palm Beach, FL', 'Davie, FL', 'Boca Raton, FL', 'Sunrise, FL', 'Plantation, FL', 'Miami Beach, FL', 'Deerfield Beach, FL', 'Boynton Beach, FL', 'Lauderhill, FL'],
                "Philadelphia-Wilmington" : ['Philadelphia, PA', 'Wilmington, DE', 'Reading, PA', 'Upper Darby Township, PA', 'Camden, NJ', 'Cherry Hill, NJ', 'Gloucester Township, NJ', 'Vineland, NJ', 'Bensalem Township, PA', 'Lower Merion Township, PA', 'Abington Township, PA', 'Bristol Township, PA', 'Haverford Township, PA', 'Washington Township, NJ', 'Evesham Township, NJ', 'Middletown Township, PA', 'Egg Harbor Township, NJ', 'Mount Laurel, NJ', 'Northampton Township, PA', 'Winslow Township, NJ'],
                "Atlanta-Sandy Springs-Alpharetta" : ['Atlanta, GA', 'Sandy Springs, GA', 'Alpharetta, GA', 'Athens, GA', 'East Cobb, GA', 'South Fulton, GA', 'Roswell, GA', 'Big Creek, GA', 'Johns Creek, GA', 'Mableton, GA', 'Lost Mountain, GA', 'Marietta, GA', 'Stonecrest, GA', 'Smyrna, GA', 'Brookhaven, GA', 'Dunwoody, GA'],
                "Phoenix-Mesa-Chandler" : ['Phoenix, AZ', 'Mesa, AZ', 'Chandler, AZ', 'Gilbert, AZ', 'Glendale, AZ', 'Scottsdale, AZ', 'Peoria, AZ', 'Tempe, AZ', 'Suprise, AZ', 'Goodyear, AZ', 'Buckeye, AZ', 'Avondale, AZ', 'Queen Creek, AZ'],
                "Boston-Cambridge-Newton" : ['Boston, MA', 'Cambridge, MA', 'Newton, MA', 'Worcester, MA', 'Providence, Rhode Island', 'Manchester, NH', 'Lowell, MA', 'Brockton, MA', 'Quincy, MA', 'Lynn, MA', 'New Bedford, MA', 'Fall River, MA', 'Nashua, NH', 'Lawrence, MA', 'Cranston, Rhode Island', 'Warwick, Rhode Island', 'Somerville, MA', 'Pawtucket, Rhode Island', 'Framingham, MA', 'Haverhill, MA', 'Malden, MA', 'Waltham, MA', 'Brookline, MA', 'Revere, MA', 'Plymouth, MA', 'Medford, MA', 'Taunton, MA', 'Weymouth, MA', 'Peabody, MA', 'Methuen, MA'],
                "San Francisco-Oakland-Berkeley" : ['San Francisco, CA', 'Oakland, CA', 'Berkeley, CA', 'Santa Rosa, CA', 'Fairfield, CA', 'Alameda, CA', 'Contra Costa, CA', 'Santa Clara, CA', 'San Joaquin, CA', 'Stanislaus, CA'],
                "Riverside-Ontario" : ['Riverside, CA', 'Ontario, CA', 'Cathedral City, California', 'Corona, CA', 'Jurupa Valley, CA', 'Moreno Valley, CA', 'Murrieta, CA', 'Perris, CA', 'Riverside, CA', 'Temecula, CA', 'Apple Valley, CA', 'Chino, CA', 'Chino Hills, CA', 'Fontana, CA', 'Hesperia, CA', 'Rancho Cucamonga, CA', 'Rialto, CA', 'San Bernardino, CA', 'Victorville, CA', 'Upland, CA'],
                "Detroit-Warren-Dearborn" : ['Detroit, MI', 'Warren, MI', 'Dearborn, MI', 'Wayne, MI', 'Oakland, MI', 'Macomb, MI', 'Livingston, MI', 'St. Clair, MI', 'Lapeer, MI'],
                "Seattle-Tacoma-Bellevue" : ['Seattle, WA', 'Tacoma, WA', 'Bellevue, WA', 'Kent, WA', 'Everett, WA', 'Arlington, WA', 'Auburn, , WA', 'Bainbridge Island, WA', 'Beaux Arts Village, WA', 'Bonney Lake, WA', 'Bothell, WA', 'Bremerton, WA',  'Brier, WA', 'Buckley, WA', 'Burien, WA', 'Covington, WA', 'Des Moines, WA', 'Duvall, WA', 'Enumclaw, WA', 'Edmonds, WA', 'Federal Way, WA', 'Gig Harbor, WA', 'Gold Bar, WA', 'Granite Falls, WA', 'Issaquah, WA', 'Kenmore, WA', 'Kirkland, WA', 'Lake Forest Par, WA','Lake Stevens, WA', 'Lakewood, WA', 'Lynnwood, WA', 'Maple Valley, WA', 'Marysville, WA', 'Mercer Island, WA', 'Mill Creek, WA', 'Monroe, WA', 'Mountlake Terrace, WA', 'Mount Vernon, WA', 'Mukilteo, WA', 'Newcastle, WA', 'Normandy Park, WA', 'North Bend, WA', 'Olympia, WA', 'Orting, WA', 'Puyallup, WA', 'Poulsbo, WA', 'Redmond, WA', 'Renton, WA', 'Sammamish, WA', 'SeaTac, WA', 'Shoreline, WA', 'Silverdale, WA', 'Snohomish, WA', 'Snoqualmie, WA', 'Stanwood, WA', 'Sultan, WA', 'Sumner, WA', 'Tukwila, WA', 'Woodinville, WA', 'Woodway, WA'],
                "Minneapolis-St. Paul-Bloomington" : ['Minneapolis, MN',  'Saint Paul, MN', 'Bloomington, MN', 'Brooklyn Park, MN', 'Plymouth, MN', 'Woodbury, MN', 'Maple Grove, MN', 'Blaine, MN', 'Lakeville, MN', 'Eagan, MN', 'Burnsville, MN', 'Eden Prairie, MN', 'Coon Rapids, MN', 'Apple Valley, MN', 'Minnetonka, MN', 'Edina, MN', 'St. Louis Park, MN'],
                "San Diego-Chula Vista-Carlsbad" : ['San Diego, CA', 'Chula Vista, CA','Carlsbad, CA', 'Coronado, CA', 'El Cajon, CA', ' Encinitas, CA', 'Escondido, CA', 'Imperial Beach, CA', 'La Mesa, CA', 'Lemon Grove, CA', 'National City, CA', 'Oceanside, CA', 'Poway, CA', 'San Marcos, CA', 'Santee, CA', 'Solana Beach, CA', 'Vista, CA'],
                "Tampa-St. Petersburg-Clearwater" : ['Tampa, FL', 'St. Petersburg, FL', 'Clearwater, FL', 'Riverview, FL', 'Brandon, FL', 'Spring Hill, FL'],
                "Denver-Aurora-Lakewood" : ['Denver, CO', 'Aurora, CO', 'Lakewood, CO', 'Arvada, CO', 'Centennial, CO', 'Highlands Ranch, CO', 'Thornton, CO', 'Westminster, CO'],
                "St. Louis" : ['St. Louis City, MO', 'St. Charles, MO', 'Crawford County, MO', 'Franklin County, MO', 'Jefferson County, MO', 'Lincoln County, MO', 'Warren County, MO', 'Bond County, IL', 'Calhoun County, IL', 'Clinton County, IL', 'Jersey County, IL', 'Macoupin County, IL', 'Madison County, IL', 'Monroe County, IL', 'St. Clair County, IL']
            }

def Combine(property_list: list, list_type: str):
    for index in range(len(property_list)):
        if index == 0:
            properties = Create_df_city(city=property_list[index], list_type=list_type)
            print(properties)
        else:
            add_location = Create_df_city(city=property_list[index], list_type=list_type)
            print(add_location)
            result = pd.concat([properties, add_location])
            properties = result
    # end for
    result = result.drop_duplicates(subset=['property_url'])
    return result


def Create_df_city(city: str, list_type: str):
    if list_type == 'sold':
        properties: pd.DataFrame = scrape_property(
                location=city,
                listing_type=list_type, # for_sale / sold / for_rent
                past_days=270
            )
    else:
        properties: pd.DataFrame = scrape_property(
                location=city,
                listing_type=list_type, # for_sale / sold / for_rent
                past_days=30
            )
    return properties #pandas dataframe


if __name__ == "__main__":
    typelist = ['sold', 'for_sale', 'for_rent']
    for typ in typelist:
        dfs = []
        for key, value in metro_dict.items():
            df = Combine(value, typ)
            df[ 'metro_area' ] = key
            dfs.append(df)
        # end for
        csv_string = typ + '.csv'
        result = pd.concat(dfs, ignore_index=True)
        result.to_csv(csv_string, index=False)
    # end for