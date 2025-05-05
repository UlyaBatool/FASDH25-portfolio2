"""
This is the starting script for today's class,
in which we'll build our first maps in Python.
"""

import pandas as pd
import plotly.express as px

# Load data
counts = pd.read_csv("ner_counts.tsv", sep="\t")
coords = pd.read_csv("gazetteers/NER_gazetteer.tsv", sep="\t")


# Clean column names (remove any leading/trailing whitespace)
counts.columns = counts.columns.str.strip()
coords.columns = coords.columns.str.strip()

# Rename columns in coords to match counts and plotting requirements
coords = coords.rename(columns={
    "Name": "Place",
    "Latitude": "latitude",
    "Longitude": "longitude"
})

# Merge data on 'placename'
data = pd.merge(counts, coords, left_on="placename", right_on="Place")

# Ensure 'count' is numeric and drop rows with missing values
data["count"] = pd.to_numeric(data["count"], errors="coerce")
data = data.dropna(subset=["count", "latitude", "longitude"])

fig = px.scatter_map(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="Place",
    size="count",
    color="count",
    title="NER-extracted Places",
    zoom=2,
)

fig.show()

# Save map to an HTML file
fig.write_html("NER_map.html")
