# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import random
from links import links

# App Code
st.header("SnowPro Advanced Architect")
st.subheader("Study Guide Randomizer")
if st.button("Generate Study Topic"):
    link = random.choice(links)
    components.iframe(link, width=1000, height=675, scrolling=True)
else:
    st.write("")