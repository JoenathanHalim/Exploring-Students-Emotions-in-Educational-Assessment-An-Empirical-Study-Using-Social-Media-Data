import numpy as np
import pandas as pd

# Create Dataset
posts = pd.read_csv("sgexams_posts_Oct2023.csv ")

# Define a search function


def search_string(s, keywords):
    s = str(s).lower()
    return any(keyword in s for keyword in keywords)


keywords = ["exam", "examination", "psle", "o levels", "a levels",
            "assessment", "weighted assessment", "continual assessment"]

# Search for keywords in all columns
mask = posts.apply(lambda x: x.map(lambda s: search_string(s, keywords)))

# Filter the database
filtered_posts = posts.loc[keywords.any(axis=1)]


print(filtered_posts.head().to_string())
print(filtered_posts.shape)
