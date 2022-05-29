import pandas as pd
import streamlit as st
import pickle
from PIL import Image

disney_dict = pickle.load(open('disney_dict (1).pkl', 'rb'))
dataset1 = pickle.load(open('gdka_dataset.pkl', 'rb'))
dataset2 = pickle.load(open('bert_dataset.pkl', 'rb'))
dataset3 = pickle.load(open('top_shows.pkl', 'rb'))
dataset4 = pickle.load(open('top_movies.pkl', 'rb'))
dataset5 = pickle.load(open('top_episodes.pkl', 'rb'))


shows = pd.DataFrame(disney_dict)
ds1 = pd.DataFrame(dataset1)
ds2 = pd.DataFrame(dataset2)
ds3 = pd.DataFrame(dataset3)
ds4 = pd.DataFrame(dataset4)
ds5 = pd.DataFrame(dataset5)
st.subheader('Disney+  is the home for your favorite movies and TV shows.')
image = Image.open('Disney.png')
st.image(image, caption=None, width=None, use_column_width="always", clamp=False, channels="RGB", output_format="auto")

indices = pd.Series(ds1['title'])
cosine_sim = pickle.load(open('gdka.pkl', 'rb'))
cos_sim = pickle.load(open('bert.pkl', 'rb'))


def recommend(title):
    recommended_shows = []
    idx = indices[indices == title].index[0]  # to get the index of the movie title matching the input movie
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)  # similarity scores in descending order
    top_10_indices = list(score_series.iloc[1:6].index)  # to get the indices of top 10 most similar movies
    # [1:11] to exclude 0 (index 0 is the input movie itself)
    for i in top_10_indices:  # to append the titles of top 10 similar movies to the recommended_movies list
        recommended_shows.append(list(ds1['title'])[i])
    return recommended_shows


def recommenddd(title):
    recommended = []
    idx = indices[indices == title].index[0]  # to get the index of the movie title matching the input movie
    similarity_scores = pd.Series(cos_sim[idx]).sort_values(ascending=False)  # similarity scores in descending order
    top_10_indices = list(similarity_scores.iloc[1:6].index)  # to get the indices of top 10 most similar movies
    # [1:11] to exclude 0 (index 0 is the input movie itself)
    for i in top_10_indices:  # to append the titles of top 10 similar movies to the recommended_movies list
        recommended.append(list(ds2['title'])[i])
    return recommended

st.subheader('Popular movies on Disney+')
ds4['title']
st.subheader('Popular episodes on Disney+')
ds5['title']
my_bar = st.progress(100)
st.header('Recommendation Engine')
select1 = st.selectbox('Select a movie', ds1['title'].values)
if st.button('Recommend'):
    recommended_shows = recommend(select1)
    for i in recommended_shows:
        st.subheader(i)
my_bar = st.progress(100)
st.header('Recommendation based on plot')
bselect = st.selectbox('Select a movie', ds2['title'].values, key = "<uniquevalueofsomesort>")
if st.button('Recommenddd'):
    recommended = recommenddd(bselect)
    for i in recommended:
        st.subheader(i)



# st.balloons()