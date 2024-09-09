import numpy as np
import pandas as pd
import re

posts = pd.read_csv("Dataset/sgexams_posts_Oct2023.csv")

keywords = r"\bexam\b|\bexamination\b|\bexams\b|\bexaminations\b|\bpsle\b|\bo level\b|\bo levels\b|\ba level\b|\ba levels\b|\bassessment\b|\bassessments\b|\btest\b|\btests\b|\bquiz\b|\bquizzes\b|\bmidterm\b|\bmidterms\b|\bfinal\b|\bfinals\b|\bweighted assessment\b|\bweighted assessments\b|\bcontinual assessment\b| \bcontinual assessments\b| \bwa\d | \bca\d | \bsa\d | \bh\d | \bs\d"

filtered_posts = posts.loc[posts[["title", "body", "flair"]].apply(
    lambda col: col.str.contains(keywords, flags=re.I, regex=True)).any(axis=1)]

filtered_posts.to_csv("Dataset/filtered_posts.csv")
