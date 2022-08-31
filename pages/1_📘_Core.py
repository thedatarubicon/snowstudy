# Exam Study Guide
# Last Updated: June 30, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.core import links

# App code
st.header("SnowPro Core")

tab1, tab2, tab3 = st.tabs(["Exam Breakdown", "Randomizer", "Sample Questions"])

with tab1:
    st.subheader("Exam Breakdown")
    ebd = {"Domain": ["Account & Security", "Virtal Warehouses", "Data Movement", "Performance Management", "Snowflake Overview and Architecture", "Storage and Protection"],
           "Estimated Percentage Range": ["10-15%", "15-20%", "10-20%", "5-10%", "25-30%", "10-15%"]}
    df = pd.DataFrame(data=ebd)
    st.table(df)

with tab2:
    st.subheader("Randomizer")
    if st.button("Generate Study Topic"):
        link = random.choice(links)
        components.iframe(link, width=1000, height=675, scrolling=True)
    else:
        st.write("")

with tab3:
    st.subheader("Sample Questions")
    q1 = st.radio("Which type of Data Integration tools leverage Snowflake's scalable compute for data transformation?",("Database Replication", "ELT", "ETL", "Streaming"))
    if q1 == "ELT":
        st.write("✅")
    else:
        st.write("❌")
    q2 = st.radio("What is the maximum number of consumer accounts that can be added to a Share object?", ("One", "Unlimited", "10", "100"))
    if q2 == "Unlimited":
        st.write("✅")
    else:
        st.write("❌")
    q3 = st.radio("3. What technique does Snowflake use to limit the number of micro-partitions scanned by each query?", ("Pruning", "Indexing", "Map Reduce", "B-Tree"))
    if q3 == "Pruning":
        st.write("✅")
    else:
        st.write("❌")
    q4l1 = st.write("Which of the following are options when creating a Virtual Warehouse?")
    q4l2 = st.write("A. auto-suspend")
    q4l3 = st.write("B. storage size") 
    q4l4 = st.write("C. auto-resume")
    q4l5 = st.write("D. cache size")   
    q4l6 = st.write("E. default role")
    q4 = st.text_input("Choose 2 answers by typing in their letters.", key=0)
    if q4 == "A, C" or q4 == "A and C" or q4 == "A & C":
        st.write("✅")
    else:
        st.write("❌")  
    q5 = st.radio("Which role in Snowflake allows a user to administer users and manage all database objects?", ("SYSADMIN", "SECURITYADMIN", "ACCOUNTADMIN", "ROOT"))
    if q5 == "ACCOUNTADMIN":
        st.write("✅")
    else:
        st.write("❌")