# Exam Study Guide
# Last Updated: May 17, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.ds import links, links2

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Data Scientist")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: May 17, 2022")
    dsbd = {"Domain": ["Data Science Concepts", "Data Pipelining", "Data Preparation and Feature Engineering", "Model Development", "Model Deployment"],
           "Estimated Percentage Range": ["10-15%", "15-20%", "25-30%", "25-30%", "15-20%"]}
    df = pd.DataFrame(data=dsbd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10, tab11 = st.tabs(["Data Science Concepts", "Data Pipelining", "Data Preparation and Feature Engineering", "Model Development", "Model Deployment"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Data Science Concepts
        with tab6:
            st.markdown("""
            ##### 1.1 Define machine learning concepts for data science workloads.
            - Artificial Intelligence
            - Machine Learning
            ##### 1.2 Outline machine learning problem types.
            - Supervised Learning
              + Structured Data
                + Linear Regression
                + Binary Classification
                + Multi-class Classification
                + Time-Series Forecasting
              + Unstructured Data
                + Image Classification, segmentation, Language Modeling, QnA
                + Typical DNN architectures: CNN, RNN, Transformer, BERT
            - Unsupervised Learning
              + Clustering
            ##### 1.3 Summarize the machine learning lifecycle.
            - Data Collection
            - Data Visualization and Exploration
            - Feature engineering
            - Training models
            - Model deployment
            - Model monitoring and evaluation
            ##### 1.4 Outline data governance for data science.
            - Dynamic data masking
            - Row level security
            - Role Based Access Control (RBAC)
            ##### 1.5 Outline statistical concepts for data science.
            - Normal distribution
            - Central limit theorem
            - Z and T tests
            - Bootstrapping
            - Confidence intervals
            ##### 1.6 Define model governance for data science.
            - Model versioning
            - Lineage
            - Model explainability
            """)

        # Data Pipelining
        with tab7:
            st.markdown("""
            ##### 2.1 Source and collect data into Snowflake from multiple sources.
            - Data loading
              + Batch loading
              + Snowpipe
              + External tables
              + Materialized views
              + Streams
              + Tasks
            - Connecting ETL tools (Connectors)
            ##### 2.2 Enrich data by consuming data sharing sources.
            - Data Marketplace
            - Direct Sharing
            - Shared database considerations
            ##### 2.3 Create a development environment (e.g., sandbox) and maintain the environment.
            - Cloning
            - Levels or hierarchy
              + Table or schema or database
            - Automation to keep dataset updated
            - Time Travel
            ##### 2.4 Build a data science pipeline.
            - Automation of data transformation
            - Streams and tasks
            - Functions
            - Stored procedures
            - Connect Snowflake to machine learning platforms (e.g., connectors, ML partners, etc.)
            """)

        # Data Preparation and Feature Engineering
        with tab8:
            st.markdown("""
            ##### 3.1 Prepare and clean the data for analysis in Snowflake.
            - Use Snowflake native functions, SQL, and Snowpark
              + Aggregate
              + Joins
              + Common Table Expressions (CTEs)
              + Identify critical data
              + Remove duplicates
              + Remove irrelevant fields
              + Handle missing values
              + Data type casting
              + Sampling data
              + Tasks to automate repeatable jobs
              + Stored procedures
            ##### 3.2 Perform feature engineering on Snowflake data.
            - Preprocessing
            - Data transformations
              + Data Frames
              + Snowpark (preview)
            - Binarizing data
              + Binning continuous data into intervals
              + Label encoding
              + One hot encoding
            - Time Travel 
            ##### 3.3 Perform exploratory data analysis in Snowflake.
            - Snowsight and SQL
              + Identify initial patterns
              + Connect external machine learning platforms and/or notebooks (e.g., Jupyter)
            - Use Snowflake native statistical functions to analyze and calculate descriptive data statistics.
              + Window Functions
              + MIN/MAX/AVG/STDEV
              + VARIANCE
              + TOPn
              + Approximation/High Performing function
            - Linear Regression
              + Find the slope and intercept
              + Verify the dependencies on dependent and independent variables
            ##### 3.4 Visualize and interpret the data to present a business case.
            - Statistical summaries
              + Snowsight
              + Snowflake SQL
              + Functions
            - Charts and graphs
              + Identify data outliers
            """)

        # Model Development
        with tab9:
            st.markdown("""
            ##### 4.1 Connect data science tools directly to data in Snowflake.
            - Connectors
              + Python connector with panda support
              + Spark connector
              + R connector
            - Snowflake Best Practices
              + One platform, one copy of data, many workloads
              + Enrich datasets using the data marketplace
              + Stream and Tasks
              + External tables
              + External functions to trigger training
              + Zero-copy cloning for training snapshots
              + Materialized views for training and prediction
              + Snowflake SQL for aggregation and sampling
            ##### 4.2 Train a data science model.
            - Hyperparameter tuning
            - Optimization metric selection (e.g., log loss, AUC, RMSE)
            - Partitioning
              + Cross validation
              + Train, validation, holdout
            - Down/Up-sampling
            ##### 4.3 Validate a data science model.
            - ROC curve/confusion matrix
              + Calculate the expected payout of the model
            - Regression problems
            - Residuals plot
              + Interpret graphics with context
            - Model metrics

            ##### 4.4 Interpret a model.
            - Feature impact
            - Partial depedence plots
            - Confidence intervals
            """)

        # Model Deployment
        with tab10:
            st.markdown("""
            ##### 5.1 Move a data science model into production.
            - Deploy an external hosted model
              + External functions
              + Pre-generated models from third party vendors
            - Deploy a model in Snowflake
              + Java User Defined Functions (UDFs)
              + Pre-generated models from third party vendors
            ##### 5.2 Score the effectiveness of a model and retrain if necessary.
            - Metrics for model evaluation
              + Data drift /Model decay
                + Data distribution comparisons
                  + Does the data making predictions look similar to the training data?
                  + Do the same data points give the same predictions once a model is deployed?
            - External functions
            - User defined functions (UDFs)
            - Storing predictions
              + Stage commands
            - Use Snowsight to do distribution comparison
            ##### 5.3 Outline model lifecycle and validation tools.
            - Streams and Tasks
            - Metadata tagging
            - Partner model versioning
              + Source control
              + Git workflow
            - Automation of model retraining
            """)

# Study Resources
with tab3:
    st.subheader("Study Resources")
    for i in links:
        st.write(i)

# Generator
with tab4:
    col1, col2 = st.columns(2)
    with col1:
        for i in links:
            st.write(i)
    with col2:
      with st.container():
        url = st.text_input("Input URL:", max_chars=1000)
        if url:
            st.write("Study Resource:", url)
            components.iframe(url, width=920, height=675, scrolling=True)

# Randomizer
with tab5:
    st.subheader("Randomizer")
    if st.button("Generate Study Resource"):
        link = random.choice(links2)
        st.write("Study Resource:", link)
        components.iframe(link, width=715, height=550, scrolling=True)
    else:
        st.write("")

# Sample Questions
with tab6:
    st.subheader("Sample Questions")

    # Q1
    q1_text = st.markdown("""
    **Q1: Where do the majority of Data Scientists spend the MOST time and effort during the Data Science workflow? (Select 2)**
    - A. Building ETL pipelines
    - B. Visualizing data
    - C. Feature Engineering
    - D. Preparing Data
    - E. Deploying a data model
    """)
    q1 = st.selectbox("Answers:", ("", "A, B", "A, C", "A, D", "A, E", "B, C", "B, D", "B, E", "C, D", "C, E", "D, E"), key=0)
    if q1 == "C, D":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q2
    q2_text = st.markdown("""
    **Q2: Which programming languages can be used to perform data transformations and feature engineering natively within Snowflake? (Select 3)**
    - A. Java
    - B. Go
    - C. SQL
    - D. Scala
    - E. R
    - F. Python
    """)
    q2 = st.selectbox("Answers:", ("", "A, B, C", "A, C, D", "A, D, E", "A, E, F", "B, C, D", "B, D, E", "B, E, F", "B, F, A", "C, D, E", "C, E, F", "C, F, A", "D, E, F", "D, F, A"), key=1)
    if q2 == "A, C, D":
        st.write("✅ That's correct!")
    elif q2 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q3
    q3_text = st.markdown("""
    **Q3: What is the correct sequence of activities that need to be performed when running a data science workload?**
    - A. Data Collection > Feature Engineering and Transformation > Data Visualization, Exploration and Understanding > Model Deployment > Model Training > Model Monitoring
    - B. Data Collection > Data Visualization, Exploration and Understanding > Feature Engineering and Transformation > Model Training > Model Monitoring > Model Deployment
    - C. Data Visualization, Exploration and Understanding > Data Collection > Feature Engineering and Transformation > Model Deployment > Model Monitoring > Model Training
    - D. Data Collection > Data Visualization, Exploration and Understanding > Feature Engineering and Transformation > Model Training > Model Deployment > Model Monitoring
    """)
    q3 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=3)
    if q3 == "D":
        st.write("✅ That's correct!")
    elif q3 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: What is the correct way to interpret a linear regression model that has an R^2 of .85?**
    - A. The model predicts that the response variable will change by approximately .85 as the explanatory variable changes by 1.
    - B. If the model was repeated multiple times, it would capture the true slope 85 percent of the time in various intervals.
    - C. There is a strong positive correlation between the response and explanatory variables.
    - D. 85 percent of the variability in the response variable can be explained by the linear associate between the response and explanatory variables.
    """)
    q4 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=4)
    if q4 == "D":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q5
    q5_text = st.markdown("""
    **Q5: A Data Scientist at Snowbear Airlines has trained a classification model for predicting the overbooking of a flight. The Data Scientist sees the following for one of the flights: The flight was not overbooked, and the model classified the flight as not overbooked. On a confusion matrix, what is the correct category of this description?**
    - A. True Negative
    - B. True Positive
    - C. False Negative
    - D. False Positive
    """)
    q5 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=5)
    if q5 == "A":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")