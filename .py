import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

sns.set(style="whitegrid")

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

uploaded_file = st.file_uploader("Upload metadata.csv", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("Dataset Overview")
        st.write("Shape:", df.shape)
        st.dataframe(df.head())
        st.write("Missing values per column:")
        st.write(df.isnull().sum())

        df_clean = df.dropna(subset=['title', 'abstract', 'publish_time'])
        df_clean['publish_time'] = pd.to_datetime(df_clean['publish_t_]()_]()_
