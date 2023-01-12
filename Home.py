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
st.header("SnowStudy")

# Page Content

# Overview
st.markdown("""
#### SnowPro Study Guides
- Core 
- Advanced: Architect
- Advanced: Administrator
- Advanced: Data Analyst
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
- [Snowflake University](https://learn.snowflake.com/)
- [30-Day Free Trial Account](https://signup.snowflake.com/?referrer=snowpro-cert)
- [Release Notes](https://docs.snowflake.com/en/release-notes.html)
""")