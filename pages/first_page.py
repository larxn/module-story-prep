import streamlit as st
import streamlit.components.v1 as components

# Custom CSS to make iframe responsive.
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Application.
components.iframe("https://storyprep.vercel.app/", scrolling=True) 