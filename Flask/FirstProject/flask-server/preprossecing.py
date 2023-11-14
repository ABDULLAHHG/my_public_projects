import pandas as pd 
import streamlit as st 
import re 
import numpy as np

df = pd.read_csv('mobile_recommendation_system_dataset.csv')

# Remove the rows with missing values 
df = df.dropna()

# Extract the storage capacity from the corpus.
def extract_storage(corpus):
    match = re.search(r'Storage(\d+)',corpus)
    if match:
        return int(match.group(1))
    return np.NaN 

# Extract the RAM from the corpus
def extract_ram(corpus):
    pass

# Extract the operating System from the corpus
def extract_system(corpus):
    match = re.search(r'System(.*?)Processor')
    if match:
        return match.group(1).strip()
    return np.NaN


# Apply the function to the 'corpurs'
df['Storage'] = df['corpus'].apply(extract_storage)

# Extract the storage capacity from the corpus.
# df['StorageOne'] = df['corpus'].apply(lambda x: re.search(r'Storage(\d+)',x).group(1) if re.search(r'Storage(\d+)',x) else np.NaN)
# df['StorageTwo'] = df['corpus'].apply(lambda x: re.search(r'Storage(\d+)',x).group(2) if re.search(r'Storage(\d+)',x)[4] else np.NaN)
# st.text( if re.search(r'Storage(\d+)',df['corpus'][1]))


st.dataframe(df)

