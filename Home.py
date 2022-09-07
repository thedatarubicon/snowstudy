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
st.header("SnowPro Study Guide Randomizer")

# Page Content
st.markdown("""
#### Table of Contents
- SnowPro Core
- SnowPro Advanced: Architect
- SnowPro Advanced: Administrator
- SnowPro Advanced: Data Engineer
- SnowPro Advanced: Data Scientist
- Feedback
#### Page Overview
Each page contains the following tabs:
- Exam Breakdown
- Domains & Objectives
- Selector
- Randomizer
- Sample Questions
#### References
[Snowflake Certifications](https://www.snowflake.com/certifications/)
""")