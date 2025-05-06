# import the relevant libraries: plotly express and pandas
# To work with tabular data 
import pandas as pd
# To make maps from extracted place names 
import plotly.express as px 

# Load the frequency data from regex_counts.tsv containing placenames and their frequency 

freq_df = pd.read_csv("../regex_counts.tsv", sep="\t")

#load the gazetteer tsv file that contain coordinates for the map and load into data frame
gazetteer_path = "../gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(gazetteer_path, sep="\t")

#To remove placenames without coordinates from the data frame:
coordinates_df = coordinates_df.dropna()


#Rename asciiname in coordinates  dataframe with placenames in frequency dataframe to have a commmon name column after merging
#4B -Solution 1 

coords_renamed = coordinates_df.rename(columns={'asciiname': 'placename'})


#Merge the two data frames to match place name with its coordinates, using the common column "asciname"
merged_df = pd.merge(coords_renamed, freq_df, on = "placename")



#To create an interactive animated map by using markers:
fig = px.scatter_map(merged_df,   
                     lat ="latitude",                   #dispalce latitude on marker 
                     lon="longitude",                   #displaces longitude on marker 
                     hover_name = "placename",          # shows placename on hover 
                    size= "count",                      # Marker size based on frequency  
                     color="count",                     # Color gradient based on frequency
                    animation_frame = "month",          # Creates a frame for each month to observe change
    color_continuous_scale=px.colors.sequential.YlOrRd, # sets color gradient for marker frequency to spot hotspots
                    size_max=25 )                       # to increase the size of marker for better navigation 

#update to a dark layout to match with color scale 
fig.update_layout(map_style= "carto-darkmatter-nolabels")

# To save map in html format # ChatGpt 4B Solution 2
fig.write_html("regex_map.html")

# To save map in png format 
fig.write_image("regex_map.png") 
