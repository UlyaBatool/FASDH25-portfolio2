#Import required libraries
#Imports regular expressions to identify patterns in the text 
import re
#Imports os to interact with the file system 
import os
#Imports pandas to work with tabular data and export tsv
import pandas as pd


#Function to write data rows into a tsv file using pandas 
def write_tsv(rows, column_list, path):
   
    #creates a dataframe from the rows 
    df = pd.DataFrame(rows, columns=column_list)
    
    #To save dataframe as tsv file 
    df.to_csv(path, sep="\t", index=False)


#Define the folder containing the corpus of news articles  
articles_dir = "../articles"  


#Define the path to gazetteer tsv file containing place names and alternate names 
path = "../gazetteers/geonames_gaza_selection.tsv"
#Open file and read it 
with open(path, encoding="utf-8") as file:
    data = file.read()


#Create a dictionary to store regex patterns and overall match count for each place
patterns = {}

#Split the gazetteer data into separate rows 
rows = data.split("\n")

#Skip the header row and process the subsequent rows because the pattern starts from the next row
for row in rows[1:]:

    
    columns = row.split("\t")   #Split row by tabs to have each column 
    asciiname = columns[0]      #The first column contains the main place name 


#Skip rows with incomplete data, first six    
    if len(columns) < 6 : #continue working at 6th column 
        continue

#Get the alternate names from column 6  
    alt_names = columns[5].strip() # to access the 6 column that contains alternate names 
    names = [asciiname]            # to start a list with the main name 

    
    if alt_names:
#Separate different alternate names using comma and add them to the list
        alt_names_list = alt_names.split(",")

        
        
#By looping through each alternate name to seperate alternate names and make a new list of alternate names 
        for name in alt_names_list:
            name = name.strip() #remove white spaces from the alternate name
            if name:
                names.append(name)#add alternate name to the list


    
    #Define a regex pattern that would match all of the name variants # Task 2A Solution 1 from Deepseek A1
    regex_pattern = "|".join(re.escape(name) for name in names)
    
    #Store the pattern and start the count at zero  
    patterns[asciiname] = {"pattern": regex_pattern, "count":0}


#Create a dictionary to store the frequency of place names per month 
mentions_per_month = {}


#Define the start date of Gaza war to skip articles before that 
war_start_date = "2023-10-07"


#Process each article file in the articles_dir by looping through them to count the patterns 
for filename in os.listdir(articles_dir):
    
    #Extract date in (YYYY-MM-DD) format from the filenames  
    article_date = filename.split("_")[0]

    #Skip files from before the war 
    if article_date < war_start_date:
        continue
    

#Define a path to read the current articles 
    article_path = os.path.join(articles_dir, filename)        
    with open(article_path, encoding="utf-8") as file:
        text = file.read()
        

    #Check each place's pattern in the article by looping through it 
    for place in patterns:
        pattern = patterns[place]["pattern"]
        matches = re.findall(pattern, text, re.IGNORECASE) #to include both capital and small letters 
        count = len(matches)#sum of matches found
        
        #Add the number of times the place was found to the total frequency:
        patterns[place]["count"] += count
        
        #Get the month part from the date
        month_key = article_date[:7]
        

#Add place and month to dictionary if they are not there
#Add the place if not in the dictionary yet 
        if place not in mentions_per_month:
            mentions_per_month[place] = {}
            
        #Check whether the month is in the dictionary 
        if month_key not in mentions_per_month[place]:
            #If not add it with a count of zero 
            mentions_per_month[place][month_key] = 0

        #Add the current count to the total for that month   
        mentions_per_month[place][month_key] += count
          


# Print the final dictionary to see the frequency of each month 
# Loop through each place name in the place_count dictionary
for place in mentions_per_month:
    # Start printing this place's data in a dictionary format 
    print(f'"{place}": {{')

    #Get all the months when this place was mentioned 
    month_list = list(mentions_per_month[place].keys())

    #Print how many times the place was mentioned in each month by looping through it 
    print(f' {place}" : {{') 
    for month in month_list:
        count = mentions_per_month[place][month] #Exact count for that month 

        # Print the output by adding a comma after each line, except the last one for a proper format 
        if month != month_list[-1]: # adds comma if not the last month # ChatGpt 4A solution 2 
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')

    #End the dictionary block for this place and print the output 
    print("},")

#Create an empty list to store the data in the form of rows 
rows = []

#Loop through each place to extract its monthly mention counts 
for place in mentions_per_month:

    #For each month the place was mentioned, retrieve the count
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]

         #Add the place, month, and count as one row so we can save it in a table format
        rows.append((place, month, count))

        

#Save the final result into a TSV file so it can be used outside this script
write_tsv(rows, ["placename", "month", "count"], "regex_counts.tsv")
