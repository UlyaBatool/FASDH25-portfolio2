
#MINI-PROJECT 2: PLACE NAME ANALYSIS OF GAZA CONFLICT
This project extracts place names from Gaza war news articles, analyzes their mention frequency after the date the war started, and visualizes the results on interactive maps. It uses two techniques,a regex-based approach with a gazetteer to improve recall by including alternate place names, and Named Entity Recognition (NER) with the Stanza library to identify place names. The maps, animated by month, compare regex and NER extractions to highlight the effectiveness of each method.

##Repository Structure 
FASDH25-portfolio2/
├── articles/ # News article corpus (YYYY-MM-DD format)
├── gazetteers/
│ ├── countries.tsv
│ ├──geonames_gaza_selection.tsv # Original gazetteer
│ ├──NER_gazetteer.tsv # Generated NER gazetteer
│ └──README.txt 
├── scripts/
│ ├── ner_map.py 
│ ├──
│ ├── regex_mapping.py # Regex-based mapping script
│ ├── build_gazetteer.py # Gazetteer construction script
│ └── copy_of_Gaza_NER2_kamil_faizan.ipynb # NER extraction notebook
│ │
│ ├── regex_counts.tsv # Regex-extracted frequencies
│ ├── ner_counts.tsv # NER-extracted frequencies
│ ├── regex_map.html # Regex interactive visualization
│ ├── regex_map.png # Regex static visualization
│ ├── ner_map.html # NER interactive visualization
│ └── ner_map.png # NER static visualization
└── README.md # This documentation

## components and tools
The project had multiple components and tools that we used throughout the process. The data set contained a folder named articles which had raw txt files of news articles about Gaza from january 2024. These files had to be processed in bulk using python to extract text content for NLP. Then we had Colab notebook in which the main code is written and executed titled as: Gaza.. we also used python for scripting and data processing, stanza library for name entity recognition, regex to clean and normalize places and OS module to read files from article directory. 

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
we renamed our class exercise filename to Gaza_NER2_Anisha_Ulya_Sehrish.ipynb and located it in the repository.
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


## 4A. Map the regex-extracted placenames
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

## Regex and  Gazetteer Technique Advantages and Disadvantages 
### Advantages 
The Regex + Gazetteer technique offers several advantages in processing and extracting place names from text. One of its main benefits is efficiency and speed, as regex can quickly scan through large datasets and identify patterns. This makes it well-suited for handling large corpora of text. Additionally, this technique provides flexibility, as it can account for various alternate spellings, abbreviations, and even localized forms of place names, thus improving the recall of place names. Furthermore, the approach is customizable, allowing for the construction of regex patterns tailored to match specific place names. It is also scalable, as the regex and gazetteer can be easily extended with more place names or new data. Lastly, when combined with geospatial data, this technique enables interactive visualizations, allowing for the mapping of place name frequencies over time, providing valuable insights.
### Disvantages 
Despite its advantages, the Regex + Gazetteer technique has certain limitations. One significant disadvantage is its low recall; places that are not included in the gazetteer or have unusual or inconsistent spellings may be missed. The technique also requires regular maintenance to ensure the gazetteer is up to date with new place names or changes in spelling conventions, which can be time-consuming. Moreover, if the regex patterns are too rigid, the technique may suffer from overfitting, missing out on place name variations or alternative representations. Additionally, the process of creating regex patterns to cover all potential variations can become complex and resource-intensive. Finally, this method is context-insensitive, meaning it cannot account for place names used in figurative or non-literal contexts, which could lead to inaccuracies in the results.

## Advantage and disadvantages of NER
Following are the advantage and disadvantages that we noticed using NER.
### Advantages
It captures place names which are not listed in the gazetteer. It also handles multi-word and context dependent mentions.
### Disadvantages
It may extract non-place entities like false positives and depends on the quality of the model.







