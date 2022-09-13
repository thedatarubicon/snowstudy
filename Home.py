# Import package dependencies
import streamlit as st

# Page Layout
st.set_page_config(layout="wide")
st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

# App Code
st.header("SnowPro SnowStudy")

tab1, tab2 = st.tabs(["Overview", "Release Notes"])

# Page Content

# Overview
with tab1:
    st.markdown("""
    #### SnowPro Study Guides
    - Core 
    - Advanced: Architect
    - Advanced: Administrator
    - Advanced: Data Engineer
    - Advanced: Data Scientist
    - Feedback
    #### Page Structure
    Each page contains the following tabs:
    - Exam Breakdown
    - Domains & Objectives
    - Study Resources
    - Randomizer
    - Sample Questions
    #### References
    - [Snowflake Certifications](https://www.snowflake.com/certifications/)
    """)

# Release Notes
with tab2:
    st.markdown("""
    ##### 9/13/22:
    - Fixed bug - iframe display is now placed within a container
    - Add new feature: Generator - render study resource URLs that you want
    - Update Core's Domain & Objectives tab
    ##### 9/8/22:
    - Update Core page's structure and content
    - Update Core page's list object references from links folder
    - Add "Last Updated" date to the Home page
    - Update the Home header
    - Update the README title
    - Add "Last Updated" date to each exam-specific page
    - Restructure/Rework Sample Questions tab
    - Restructure/Rework Randomizer tab to display URL along with iframe component
    - Update Home page structure to have the following tabs: Overview, Release Notes
    - Fix bugs in the "Sample Questions" tab for the following pages: Core and Data Engineer
    ##### 9/7/22:
    - Add Domains & Objectives tab to each exam-specific page
    - Add Feedback page to app
    - Add all exam-specific links to the Study Resources tab
    - Make all links into clickable links in Study Resources tab
    ##### 8/31/22: 
    - SnowPro SnowStudy's exam-specific pages were built out
    - Randomizer tab's iframe component's width and height was adjusted
    - Update README
    ##### 8/30/22: 
    - SnowPro SnowStudy app was created
    """)