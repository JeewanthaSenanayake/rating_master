import pandas as pd

# Load the three files as dataframes
metadata = pd.read_csv("/home/jeewantha/Project/dataSte/title-metadata.tsv", sep='\t')
crew = pd.read_csv("/home/jeewantha/Project/dataSte/title-crew.tsv", sep='\t')
ratings = pd.read_csv("/home/jeewantha/Project/dataSte/title-ratings.tsv", sep='\t')

# Merge the dataframes on the "tconst" column
merged_data = pd.merge(metadata, crew, on="tconst")
merged_data = pd.merge(merged_data, ratings, on="tconst")

# # Print the merged dataframe
print("---------------------------------------------------------")
print(merged_data)



