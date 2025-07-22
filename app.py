

import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App title and layout
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# App header
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Select a movie and get top 5 recommendations instantly!</p>", unsafe_allow_html=True)
st.markdown("---")

# Dropdown to select movie
selected_movie = st.selectbox("🎞️ Choose a movie", movies['title'].values)

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Recommend button
if st.button("📽️ Recommend"):
    with st.spinner("Finding similar movies... 🎬"):
        recommendations = recommend(selected_movie)
        st.markdown("### 🎯 Top 5 Recommendations:")
        for i, movie in enumerate(recommendations, 1):
            st.markdown(f"**{i}. {movie}**")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 13px; color: grey;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
