<<<<<<< HEAD

#MINI-PROJECT 2: PLACE NAME ANALYSIS OF GAZA CONFLICT

=======
# MINI-PROJECT 2: PLACE NAME ANALYSIS OF GAZA CONFLICT
>>>>>>> 484f0ff0468f9e11795fd9860127a24056451c3c
This project extracts place names from Gaza war news articles, analyzes their mention frequency after the date the war started, and visualizes the results on interactive maps. It uses two techniques,a regex-based approach with a gazetteer to improve recall by including alternate place names, and Named Entity Recognition (NER) with the Stanza library to identify place names. The maps, animated by month, compare regex and NER extractions to highlight the effectiveness of each method.

##Repository Structure
 
FASDH25-portfolio2/
├── .git/                                # Git version control folder
├── .gitignore                           # Specifies files/folders to ignore in Git
├── README.md                            # Main documentation file
│
├── articles/                            # News articles (named by date)
│
├── outputs/                             # Final outputs from NER and Regex processing
│   ├── regex_map.html                   # Regex interactive visualization
│   ├── regex_map.png                    # Regex static visualization
│   ├── regex_counts.tsv                 # Regex-based place name frequencies
│   ├── ner_map.html                     # NER interactive visualization
│   ├── ner_map.png                      # NER static visualization
│   ├── NER_gazetteer.tsv                # Gazetteer built from NER
│   └── ner_counts.tsv                   # NER-based place name frequencies
│
├── scripts/                             # Scripts and notebooks
│   ├── ner_map.py                       # NER map generation script
│   ├── regex_mapping.py                 # Regex-based mapping script
│   ├── final_regex_script.py            # Final version of regex script
│   ├── sehrish_hakim_mapping.py         # Mapping work by Sehrish Hakim
│   ├── ner_counts.tsv                   # NER-extracted frequency file (duplicate in outputs)
│   ├── regex_counts.tsv                 # Regex-extracted frequency file (duplicate in outputs)
│   └── copy_of_gaza_NER_ulya_anisha_sehrish.ipynb # Notebook by Ulya, Anisha & Sehrish
│
├── gazetteers/                          # Gazetteer data and metadata
│   ├── countries.tsv
│   ├── geonames_gaza_selection.tsv      # Original gazetteer
│   ├── NER_gazetteer.tsv                # Generated from NER data
│   └── README.txt
│
├── Ai documentation/                    # AI documentation by group members
│   ├── Ai_documentation_sehrish_hakim.pdf
│   └── Ai_documentation_anisha_ulya.pdf


## 2A. Use gazetteer and regex to extract places in Gaza from the corpus

### Preparation for the task 

We started by copying a script we wrote in class  session_10.1/<your_name>_6.py) to repository and then modified the script for the task and then saved it as regex_script_final.py after completion. 
### Step 1: Load Gazetteer and Corpus
The script starts by reading a TSV gazetteer file that lists places in Gaza along with their alternate names. It also defines the directory containing the article corpus. These are read from the portfolio repository, not the session folders.

### Step 2: Build Regex Patterns from Place Names

To improve recall, the script constructs regular expressions using both the primary name "asciiname" and alternate names for each place. This ensures different spellings and variants are captured accurately in the text.
### Step 3: Filter Articles by War Start Date
Each article file’s name contains a date. The script skips all articles that were published before the start of the Gaza war (October 7, 2023), ensuring that only relevant data is processed.

### Step 4: Count Mentions of Places per Month

The script goes through each article and searches for all mentions of each place using the compiled regex patterns. It then builds a nested dictionary "mentions_per_month" where the outer key is the place name and the inner key is the month of publication, allowing us to track temporal frequency.

### Step 5: Export Results to a TSV File

All the place mention counts are flattened into a list of rows and saved as "regex_counts.tsv". This file has three columns: placename, month, and count, and it can be used for further analysis or visualization.


## part 2B: Named entity recognition with stanza

In this part we used our class colab notebook to extract and count place names (GPEs) from "january 2024" articles using stanza NLP library. following are the steps of NER in google collab.

### Notebook Setup

we renamed our class exercise filename to Gaza_NER2_Ulya_Anisha_Sehrish.ipynb and located it in the repository.

### Loading the corpus

we changed the data path so that the notebook reads all txt files from the project's articles folder instead of session_10.1.

### Filtering by date

we used python's od.listdir() and string methods to include only files whose names start with 2024-01.

### Extracting place names with stanza

we installed and downloaded the english model using codes such as !pip install stanza. then we ran nlp(text) on each article and collected all entites where ent.type == 'GPE'.

### counting mentions

we accumulated counts in a python counter so that each distinct entity text e.g "Gaza" maps to its frequency across all january files.

### cleaning and merging duplicates

we normalized names by striping possessive endings, removing punctuations, and lowercasing then capitalizing. next we merged entries so that varients like "Gaza" and "gaza" add into a single "Gaza" count.

### Exporting Results

we wrote the final dictionary to ner_counts.tsv with two columns (placename, count). finally we downloaded the notebook as ipynb and commited it to the repository.

## part 3: Create a gazetteer for the NER places

In this part we geocoded every place name from ner_counts.tsv assigning “NA” when no match was found—and compiled the results into NER_gazetteer.tsv with placename, latitude, and longitude columns. 

### Geocoding

In this part we used the GeoNames API to fetch coordinates for each place in our dataset by sending HTTP requests and parsing the JSON responses. next we found coordinates for the places. we got our result in NER-gazetteer.tsv with three columns of place, latitude and longitude. 

### Editing outputs manually

In our output we got other entities than placenames as well such as events, organization and person's names so we manually removed them from the folder and refined our output.

## 4A: Map the regex-extracted placenames

### Load Required Libraries

We import pandas for handling tabular data and plotly.express for creating interactive maps.

### Read Frequency Data and Gazetteer Coordinates

We read two TSV files, regex_counts.tsv, which contains the frequency of place name mentions by month,and a gazetteer file geonames_gaza_selection.tsv that provides geographic coordinates for each place.

### Clean and Prepare Data for Merging

To ensure compatibility, we rename the asciiname column in the gazetteer to placename, which matches the column name in the frequency dataset. We also remove entries in the gazetteer that do not have coordinates.

### Merge Frequency Data with Coordinates

We perform a merge on the placename column to align each place’s frequency data with its corresponding latitude and longitude.

### Create Animated Map Using Plotly Express

We use px.scatter_map to plot placenames as markers on a map. Marker "size" and "color" represent the frequency of mentions, and the animation advances by "month". This allows viewers to observe how spatial attention changes over time.

### Apply Styling for Better Visualization

We use the "carto-darkmatter-nolabels" map style for contrast and the "YlOrRd" color scale to visually represent frequency intensity—making hotspots stand out clearly.

### Save Outputs in HTML and PNG Formats

The interactive map is saved as "regex_map.html" for exploration in browsers, and a static image is saved as "regex_map.png" for presentations and documentation.

## 4B: Mapping the NER-extracted placenames

### Mapping

We used Plotly Express to visualize how often different place names appeared in our dataset from January 2024. Using the frequencies stored in ner_counts.tsv and the corresponding coordinates from NER_gazetteer.tsv, we created an interactive map (ner_map.html) and a static image (ner_map.png) to display these locations and their occurrence visually.

## Regex and  Gazetteer Technique Advantages and Disadvantages 

### Advantages of NER

Named Entity Recognition is a powerful tool for identifying place names in text due to its ability to understand context. Unlike regex, NER doesn’t rely on exact matches or fixed patterns—it uses machine learning models trained on large corpora to recognize entities even when they appear in varied or unexpected forms. This means it can detect a broader range of place names, including those not explicitly listed in a gazetteer. It also reduces the need for manual updates, as pre-trained models are often effective out of the box. Additionally, NER can distinguish between different types of named entities (e.g., people, organizations, and locations), making it useful in more nuanced analyses.

### Disadvantages of NER

Despite its strengths, NER has some limitations. It is more complex to implement than regex and typically requires substantial computational resources, especially for large datasets. The quality of its output heavily depends on the model’s training data, meaning errors can occur if the model is not fine-tuned for the specific domain or language. Ambiguity in text—such as place names that are also common words (e.g., "Turkey")—can lead to misclassifications. Moreover, while NER handles variability better than regex, it may still miss newly coined or less common names without retraining or additional data. Lastly, because it operates as a black box, its decision-making process is less transparent and harder to manually control or correct.

### Advantages of Regex + Gazetteer

The Regex + Gazetteer technique offers several advantages in processing and extracting place names from text. One of its main benefits is efficiency and speed, as regex can quickly scan through large datasets and identify patterns. This makes it well-suited for handling large corpora of text. Additionally, this technique provides flexibility, as it can account for various alternate spellings, abbreviations, and even localized forms of place names, thus improving the recall of place names. Furthermore, the approach is customizable, allowing for the construction of regex patterns tailored to match specific place names. It is also scalable, as the regex and gazetteer can be easily extended with more place names or new data. Lastly, when combined with geospatial data, this technique enables interactive visualizations, allowing for the mapping of place name frequencies over time, providing valuable insights.

### Disadvantages of Regex + Gazetteer
 
Despite its advantages, the Regex + Gazetteer technique has certain limitations. One significant disadvantage is its low recall; places that are not included in the gazetteer or have unusual or inconsistent spellings may be missed. The technique also requires regular maintenance to ensure the gazetteer is up to date with new place names or changes in spelling conventions, which can be time-consuming. Moreover, if the regex patterns are too rigid, the technique may suffer from overfitting, missing out on place name variations or alternative representations. Additionally, the process of creating regex patterns to cover all potential variations can become complex and resource-intensive. Finally, this method is context-insensitive, meaning it cannot account for place names used in figurative or non-literal contexts, which could lead to inaccuracies in the results.

## Output Maps

### Regex_map 

![Regex Map](FASDH25-portfolio2/outputs/regex_map.png)
![Regex Map](FASDH25-portfolio2/outputs/ner_map.png)

## Self critical Analysis 

One of the main challenges we faced in this project was dealing with incomplete or inconsistent data from the GeoNames API—sometimes it didn’t return coordinates, or the places were ambiguous. This caused issues when we tried to merge and map the data, especially when column names didn’t match or when missing values led to errors in visualization. While we managed to clean and fix these problems manually, it highlighted the need for better error handling and data validation in our workflow. another issue that we faced was while using google colab, everytime we opened colab we had to install and run each code which took us a lot of time. sometimes it would take 25 minutes to load one code. If we had more time, we would focus on making the process more automated and reliable, with clearer logic and perhaps better tools to filter or verify geocoding results. Overall, the project worked, but there’s definitely room for making it more efficient and user-friendly.
