# Exam Study Guide
# Last Updated: August 9, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.core import links, links2

# Page Layout
st.set_page_config(layout="wide")

# App code
st.header("SnowPro Core")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: August 9, 2022")
    ebd = {"Domain": ["Snowflake Cloud Data Platform and Features", "Account Access and Security", "Performance Concepts", "Data Loading and Unloading", "Data Transformations", "Data Protection and Data Sharing"],
           "Estimated Percentage Range": ["20-25%", "20-25%", "10-15%", "5-10%", "20-25%", "5-10%"]}
    df = pd.DataFrame(data=ebd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10, tab11, tab12 = st.tabs(["Snowflake Cloud Data Platform and Features", "Account Access and Security", "Performance Concepts", "Data Loading and Unloading", "Data Transformations", "Data Protection and Data Sharing"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Snowflake Cloud Data Platform and Features
        with tab7:
            st.markdown("""
            ##### 1.1 Outline key features of the Snowflake Cloud Data Platform.
            - Elastic Storage
            - Elastic Compute
            - Snowflake’s three distinct layers
            - Data Cloud/ Data Exchange/ Partner Network
            - Cloud partner categories
            ##### 1.2 Outline key Snowflake tools and user interfaces.
            - Snowflake User Interfaces (UI)
            - Snowsight
            - Snowflake connectors
            - Snowflake drivers
            - SQL scripting
            - Snowpark
            ##### 1.3 Outline Snowflake’s catalog and objects.
            - Databases
            - Schemas
            - Tables Types
            - View Types
            - Data types
            - User-Defined Functions (UDFs) and User Defined Table Functions (UDTFs)
            - Stored Procedures
            - Streams
            - Tasks
            - Pipes
            - Shares
            - Sequences
            ##### 1.4 Outline Snowflake storage concepts.
            - Micro partitions
            - Types of column metadata clustering
            - Data Storage Monitoring
            - Search Optimization Service
            """)
        
        # Account Access and Security
        with tab8:
            st.markdown("""
            ##### 2.1 Outline security principles.
            - Network security and policies
            - Multi-Factor Authentication (MFA)
            - Federated authentication
            - Single Sign-On (SSO)
            ##### 2.2 Define the entities and roles that are used in Snowflake.
            - Outline how privileges can be granted and revoked
            - Explain role hierarchy and privilege inheritance
            ##### 2.3 Outline data governance capabilities in Snowflake.
            - Accounts
            - Organizations
            - Databases
            - Secure views
            - Information schemas
            - Access history and read support
            """)
      
        # Performance Concepts
        with tab9:
            st.markdown("""
            ##### 3.1 Explain the use of the Query Profile.
            - Explain plans
            - Data spilling
            - Use of the data cache
            - Micro-partition pruning
            - Query history
            ##### 3.2 Explain virtual warehouse configurations.
            - Multi-clustering
            - Warehouse sizing
            - Warehouse settings and access
            ##### 3.3 Outline virtual warehouse performance tools.
            - Monitoring warehouse loads
            - Query performance
            - Scaling up compared to scaling out
            - Resource monitors
            ##### 3.4 Optimize query performance.
            - Describe the use of materialized views
            - Use of specific SELECT commands 
            """)
        
        # Data Loading and Unloading
        with tab10:
            st.markdown("""
            ##### 4.1 Define concepts and best practices that should be considered when loading data.
            - Stages and stage types
            - File size
            - File formats
            - Folder structures
            - Adhoc/bulk loading using the Snowflake UI
            ##### 4.2 Outline different commands used to load data and when they should be used.
            - CREATE PIPE
            - COPY INTO
            - GET
            - INSERT/INSERT OVERWRITE
            - PUT
            - STREAM
            - TASK
            - VALIDATE
            ##### 4.3 Define concepts and best practices that should be considered when unloading data.
            - File formats
            - Empty strings and NULL values
            - Unloading to a single file
            - Unloading relational tables
            ##### 4.4 Outline the different commands used to unload data and when they should be used.
            - LIST
            - COPY INTO
            - CREATE FILE FORMAT
            - CREATE FILE FORMAT … CLONE
            - ALTER FILE FORMAT
            - DROP FILE FORMAT
            - DESCRIBE FILE FORMAT
            - SHOW FILE FORMAT
            """)

        # Data Transformations
        with tab11:
            st.markdown("""
            ##### 5.1 Explain how to work with standard data.
            - Estimating functions
            - Sampling
            - Supported function types
            - User-Defined Functions (UDFs) and stored procedures
            ##### 5.2 Explain how to work with semi-structured data.
            - Supported file formats, data types, and sizes
            - VARIANT column
            - Flattening the nested structure
            ##### 5.3 Explain how to work with unstructured data.
            - Define and use directory tables
            - SQL file functions
            - Outline the purpose of User-Defined Functions (UDFs) for data analysis
            """)
        
        # Data Protection and Data Sharing
        with tab12:
            st.markdown("""
            ##### 6.1 Outline Continuous Data Protection with Snowflake.
            - Time Travel
            - Fail-safe
            - Data Encryption
            - Cloning
            - Replication
            ##### 6.2 Outline Snowflake data sharing capabilities.
            - Account types
            - Data Marketplace and Data Exchange
            - Private data exchange
            - Access control options
            - Shares
            """)
# Feature Enhancement: Restructure Study Resources (Tabs within a tab)
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
    **Q1: Which type of Data Integration tools leverage Snowflake's scalable compute for data transformation?** 
    - A. Database Replication
    - B. ELT
    - C. ETL
    - D. Streaming
    """)
    q1 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=0)
    if q1 == "B":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")        

    # Q2
    q2_text = st.markdown("""
    **Q2: What is the maximum number of consumer accounts that can be added to a share object?**
    - A. 1
    - B. 10
    - C. 100
    - D. Unlimited
    """)
    q2 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=1)
    if q2 == "D":
        st.write("✅ That's correct!")
    elif q2 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q3
    q3_text = st.markdown("""
    **Q3: What technique does Snowflake use to limit the number of micro-partitions scanned by each query?**
    - A. Pruning
    - B. Indexing
    - C. Map Reduce
    - D. B-Tree
    """)
    q3 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=2)
    if q3 == "A":
        st.write("✅ That's correct!")
    elif q3 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: Which of the following are options when creating a Virtual Warehouse? (Select 2)**
    - A. auto-suspend
    - B. storage size
    - C. auto-resume
    - D. cache size  
    - E. default role
    """)
    q4 = st.selectbox("Answers:", ("", "A, B", "A, C", "A, D", "A, E", "B, C", "B, D", "B, E", "C, D", "C, E", "D, E"), key=3)
    if q4 == "A, C":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q5
    q5_text = st.markdown("""
    **Q5: Which role in Snowflake allows a user to administer users and manage all database objects?**
    - A. SYSADMIN
    - B. SECURITYADMIN
    - C. ACCOUNTADMIN
    - D. ROOT
    """)
    q5 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=4)
    if q5 == "C":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")