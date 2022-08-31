# Exam Study Guide
# Last Updated: May 17, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.ds import links

# App Code
st.header("SnowPro Advanced: Data Scientist")

tab1, tab2, tab3 = st.tabs(["Exam Breakdown", "Randomizer", "Sample Questions"])

with tab1:
    st.subheader("Exam Breakdown")
    dsbd = {"Domain": ["Data Science Concepts", "Data Pipelining", "Data Preparation and Feature Engineering", "Model Development", "Model Deployment"],
           "Estimated Percentage Range": ["10-15%", "15-20%", "25-30%", "25-30%", "15-20%"]}
    df = pd.DataFrame(data=dsbd)
    st.table(df)

with tab2:
    st.subheader("Randomizer")
    if st.button("Generate Study Topic"):
        link = random.choice(links)
        components.iframe(link, width=715, height=550, scrolling=True)
    else:
        st.write("")

with tab3:
    st.subheader("Sample Questions")
    q1l1 = st.write("Where do the majority of Data Scientists spend the MOST time and effort during the Data Science workflow?")
    q1l2 = st.write("A. Building ETL pipelines")
    q1l3 = st.write("B. Visualizing data")
    q1l4 = st.write("C. Feature Engineering")
    q1l5 = st.write("D. Preparing Data")
    q1l6 = st.write("E. Deploying a data model")
    q1 = st.text_input("Choose 2 answers by typing in their letters.", key=0)
    if q1 == "C, D" or q1 == "C and D" or q1 == "C & D":
        st.write("✅")
    else:
        st.write("❌")
    q2l1 = st.write("Which programming languages can be used to perform data transformations and feature engineering natively within Snowflake?")
    q2l2 = st.write("A. Java")
    q2l3 = st.write("B. Go")
    q2l4 = st.write("C. SQL")
    q2l5 = st.write("D. Scala")
    q2l6 = st.write("E. R")
    q2l7 = st.write("F. Python")
    q2 = st.text_input("Choose 2 answers by typing in their letters.", key=1)
    if q2 == "A, C, D" or q2 == "A, C, and D" or q2 == "A, C, & D" or q2 == "A, C & D":
        st.write("✅")
    else:
        st.write("❌")
    q3 = st.radio("What is the correct sequence of activities that need to be performed when running a data science workload?",
                  ("Data Collection > Feature Engineering and Transformation > Data Visualization, Exploration and Understanding > Model Deployment > Model Training > Model Monitoring",
                  "Data Collection > Data Visualization, Exploration and Understanding > Feature Engineering and Transformation > Model Training > Model Monitoring > Model Deployment",
                  "Data Visualization, Exploration and Understanding > Data Collection > Feature Engineering and Transformation > Model Deployment > Model Monitoring > Model Training", 
                  "Data Collection > Data Visualization, Exploration and Understanding > Feature Engineering and Transformation > Model Training > Model Deployment > Model Monitoring"))
    if q3 == "Data Collection > Data Visualization, Exploration and Understanding > Feature Engineering and Transformation > Model Training > Model Deployment > Model Monitoring":
        st.write("✅")
    else:
        st.write("❌")
    q4 = st.radio("What is the correct way to interpret a linear regression model that has an R^2 of .85?", 
                 ("The model predicts that the response variable will change by approximately .85 as the explanatory variable changes by 1.",
                  "If the model was repeated multiple times, it would capture the true slope 85 percent of the time in various intervals.",
                  "There is a strong positive correlation between the response and explanatory variables.",
                  "85 percent of the variability in the response variable can be explained by the linear associate between the response and explanatory variables."))
    if q4 == "85 percent of the variability in the response variable can be explained by the linear associate between the response and explanatory variables.":
        st.write("✅")
    else:
        st.write("❌")
    q5 = st.radio("A Data Scientist at Snowbear Airlines has trained a classification model for predicting the overbooking of a flight. The Data Scientist sees the following for one of the flights: \
                  The flight was not overbooked, and the model classified the flight as not overbooked. \
                  On a confusion matrix, what is the correct category of this description?", 
                  ("True Negative", "True Positive", "False Negative", "False Positive"))
    if q5 == "True Negative":
        st.write("✅")
    else:
        st.write("❌")