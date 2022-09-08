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

# Page Content
st.markdown("""
#### Table of Contents
- SnowPro Core (Last Updated: August 9, 2022)
- SnowPro Advanced: Architect (Last Updated: May 3, 2022)
- SnowPro Advanced: Administrator (Last Updated: March 1, 2022)
- SnowPro Advanced: Data Engineer (Last Updated: June 23, 2022)
- SnowPro Advanced: Data Scientist (Last Updated: May 17, 2022)
- Feedback
#### Page Overview
Each page contains the following tabs:
- Exam Breakdown
- Domains & Objectives
- Study Resources
- Randomizer
- Sample Questions
#### References
[Snowflake Certifications](https://www.snowflake.com/certifications/)
""")