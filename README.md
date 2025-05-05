#Mini project

In project 2, we focused on natural language processing (NLP)to extract place names from a collection of news articles from Al Jazeera related to gaza. we used python and stanza NLP library to process articles from january 2024 to identify and count location mentions. we also used regex and a gazetteer for extraction. The purpose of this project is to explore how NER tools such as stanza can be applied to the real-world textual data to geographic references.

## components and tools
The project had multiple components and tools that we used throughout the process. The data set contained a folder named articles which had raw txt files of news articles about Gaza from january 2024. These files had to be processed in bulk using python to extract text content for NLP. Then we had Colab notebook in which the main code is written and executed titled as: Gaza.. we also used python for scripting and data processing, stanza library for name entity recognition, regex to clean and normalize places and OS module to read files from article directory.


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

## Advantage and disadvantages of NER
Following are the advantage and dis advantages that we noticed using NER.
### Advantages
It captures place names which are not listed in the gazetteer. It also handles multi-word and context dependent mentions.
### Disadvantages
It may extract non-place entities like false positives and depends on the quality of the model.






