# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
from links.feedback import link

# Page Layout
st.set_page_config(layout="wide")

st.header("User Feedback")
components.iframe(link, width=715, height=1000, scrolling=True)