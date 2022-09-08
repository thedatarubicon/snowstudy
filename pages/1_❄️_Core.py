# Exam Study Guide
# Last Updated: June 30, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.core import links

# Page Layout
st.set_page_config(layout="wide")

# App code
st.header("SnowPro Core")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    ebd = {"Domain": ["Account & Security", "Virtual Warehouses", "Data Movement", "Performance Management", "Snowflake Overview and Architecture", "Storage and Protection"],
           "Estimated Percentage Range": ["10-15%", "15-20%", "10-20%", "5-10%", "25-30%", "10-15%"]}
    df = pd.DataFrame(data=ebd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Account & Security", "Virtual Warehouses", "Data Movement", "Performance Management", "Snowflake Overview and Architecture", "Storage and Protection"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
        # Account & Security
        with tab6:
            st.markdown("""
            ##### 1.1 Explain how to manage Snowflake accounts.
            - Account usage
            - Account access
            - Account views
            - Information schema
            ##### 1.2 Outline security principles.
            - Multi-factor Authentication (MFA)
            - Data Encryption
            - Network Security and Policies
            - Access Control
            - Federated Authentication
            - Single Sign-On (SSO)
            ##### 1.3 Define the entities and roles that are used in Snowflake.
            - Outline how privileges can be granted and revoked
            - Explain Role Hierarchy and Privilege Inheritance
            ##### 1.4 Explain the security capabilities associated with each Snowflake edition.
            - Column-level security
            ##### 1.5 Outline data governance capabilities in Snowflake.
            - Data masking
            - Account usage views
            - External tokenization
            - Secure views
            """)
        
        # Virtual Warehouses
        with tab7:
            st.markdown("""
            ##### 2.1 Outline compute principles.
            - Credit usage and billing
            - Concurrency
            - Caching
            - Virtual warehouse characteristics and parameters
            - Query profiler
            ##### 2.2 Explain Virtual Warehouse best practices.
            - Scale up compared to scale out
            - Types of virtual warehouses
            - Management/monitoring
            """)
      
        # Data Movement
        with tab8:
            st.markdown("""
            ##### 3.1 Outline different commands used to load data and when they should be used.
            - COPY
            - INSERT
            - PUT
            - GET
            - VALIDATE
            - SNOWPIPE
            - COPY INTO
            ##### 3.2 Define bulk as compared to continuous data loading methods.
            - COPY
            - Snowpipe
            - Parameters types
            ##### 3.3 Define best practices that should be considered when loading data.
            - File size
            - File Formats
            - Folders
            ##### 3.4 Outline how data can be unloaded from Snowflake to either local storage or cloud storage locations.
            - Define formats supported for unloading data from Snowflake
            - Define commands that help when unloading data
            - Define best practices that should be considered when unloading data
            ##### 3.5 Explain how to work and load semi-structured data.
            - Supported file formats, data types, and sizes
            - VARIANT column
            - Flattening the nested structure
            """)
        
        # Performance Management
        with tab9:
            st.markdown("""
            ##### 4.1 Outline best practices for Snowflake performance management on storage.
            - Clustering
            - Materialized views
            - Search Optimization Service
            ##### 4.2 Outline best practices for Snowflake performance management on virtual warehouses.
            - Query performance and analysis
            - Query profiles
            - Query history and activity
            - SQL optimization
            - Caching
            """)

        # Snowflake Overview and Architecture
        with tab10:
            st.markdown("""
            ##### 5.1 Outline key components of Snowflake's Cloud data platform.
            - Data types
            - Optimizer
            - Continuous data protection
            - Cloning
            - Types of Caching
            - User-defined Functions (UDFs)
            - Web Interface (UI)
            - Data Cloud/Data Sharing/Data Marketplace/Data Exchange
            ##### 5.2 Outline Snowflake data sharing capabilities.
            - Account types
            - Data Marketplace and Exchange
            - Access control options
            - Shares
            ##### 5.3 Explain how Snowflake is different compared to legacy warehouse solutions.
            - Elastic Storage
            - Elastic Compute
            - Account Management
            ##### 5.4 Outline the different editions that are available, and the functionality associated with each edition.
            - Pricing
            - Features
            ##### 5.5 Identify Snowflake's Partner Ecosystem.
            - Cloud Partners
            - Connectors
            ##### 5.6 Outline and define the purpose of Snowflake's three distinct layers.
            - Storage Layer
            - Compute Layer
            - Cloud Services Layer
            ##### 5.7 Outline Snowflake's catalog and objects.
            - Accounts
            - Database
            - Schema
            - Table Types
            - View Types
            - Data Types
            - External Functions
            - Stored Procedures
            """)
        
        # Storage and Protection
        with tab11:
            st.markdown("""
            ##### 6.1 Outline Snowflake Storage Concepts.
            - Micropartitions
            - Metadata Types
            - Clustering
            - Data Storage
            - Stage Types
            - File Formats
            - Storage Monitoring
            ##### 6.2 Outline Continuous Data Protection with Snowflake.
            - Time Travel
            - Fail Safe
            - Data Encryption
            - Cloning
            - Replication
            - Master keys
            """)

# Study Resources
with tab3:
    st.subheader("Study Resources")
    df = pd.DataFrame(links, columns=["Link"])
    st.write(df.to_html(escape=False, index=False, header=False), unsafe_allow_html=True)

# Randomizer
with tab4:
    st.subheader("Randomizer")
    if st.button("Generate Study Topic"):
        link = random.choice(links)
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