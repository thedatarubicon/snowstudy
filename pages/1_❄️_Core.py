# Exam Study Guide
# Last Updated: August 9, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.ds import links, links2

# Page Layout
st.set_page_config(layout="wide")

# App code
st.header("SnowPro Core")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    ebd = {"Domain": ["Snowflake Cloud Data Platform and Features", "Account Access and Security", "Performance Concepts", "Data Loading and Unloading", "Data Transformations", "Data Protection and Data Sharing"],
           "Estimated Percentage Range": ["20-25%", "20-25%", "10-15%", "5-10%", "20-25%", "5-10%"]}
    df = pd.DataFrame(data=ebd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Snowflake Cloud Data Platform and Features", "Account Access and Security", "Performance Concepts", "Data Loading and Unloading", "Data Transformations", "Data Protection and Data Sharing"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Snowflake Cloud Data Platform and Features
        with tab6:
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
        with tab7:
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
        with tab8:
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
        with tab9:
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
        with tab10:
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
            - Directory tables
            - SQL file functions
            - Rest API
            - Create User-Defined Functions (UDFs) for data analysis
            """)
        
        # Data Protection and Data Sharing
        with tab11:
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

# Study Resources
with tab3:
    st.subheader("Study Resources")
    for i in links:
        st.write(i)

# Randomizer
with tab4:
    st.subheader("Randomizer")
    if st.button("Generate Study Topic"):
        link = random.choice(links2)
        components.iframe(link, width=715, height=550, scrolling=True)
    else:
        st.write("")

# Sample Questions
with tab5:
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