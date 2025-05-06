import pandas as pd
import plotly.express as px

# Loading the data files
counts_df = pd.read_csv("../ner_counts.tsv", sep="\t")
coords_df = pd.read_csv("../NER_gazetteer.tsv", sep="\t")

# Merging the dataframes and placename
merged_df = pd.merge(counts_df, coords_df, on="placename", how="inner")

# Clean the data by removing rows with missing coordinates or count
clean_df = merged_df.dropna(subset=["latitude", "longitude", "count"]).copy()  # 🟢 copy added

# Step 4: Convert columns to float safely
clean_df["latitude"] = clean_df["latitude"].astype(float)
clean_df["longitude"] = clean_df["longitude"].astype(float)
clean_df["count"] = clean_df["count"].astype(float)  # this line prevents NaN in marker size

# Step 5: Create the map
fig = px.scatter_geo(
    clean_df,
    lat="latitude",
    lon="longitude",
    size="count",
    color="placename",
    hover_name="placename",
    projection="natural earth",
    size_max=20,
    title="NER Place Frequencies (Jan 2024)"
)

# Step 6: Export the map as HTML and PNG
fig.write_html("ner_map.html")
fig.write_image("ner_map.png")

print("Map files saved as 'ner_map.html' and 'ner_map.png'")
