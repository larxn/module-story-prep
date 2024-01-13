import streamlit as st
import streamlit.components.v1 as components
import os

# Custom CSS to make iframe responsive.
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Application.
api_key = os.environ['CLARIFAI_PAT'] 
components.iframe(f"https://storyprep.vercel.app/?api_key={api_key}", scrolling=True)
