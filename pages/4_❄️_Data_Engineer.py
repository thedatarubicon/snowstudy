# Exam Study Guide
# Last Updated: June 23, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.de import links

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Data Engineer")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    debd = {"Domain": ["Data Movement", "Performance Optimization", "Storage and Data Protection", "Security", "Data Transformation"], 
           "Estimated Percentage Range": ["25-30%", "20-25%", "10-15%", "10-15%", "25-30%"]}
    df = pd.DataFrame(data=debd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab6, tab7, tab8, tab9, tab10 = st.tabs(["Data Movement", "Performance Optimization", "Storage and Data Protection", "Security", "Data Transformation"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Data Movement
        with tab6:
            st.markdown("""
            ##### 1.1 Given a data set, load data into Snowflake.
            - Outline considerations for data loading
            - Define data loading features and potential impact
            ##### 1.2 Ingest data of various formats through the mechanics of Snowflake.
            - Required data formats
            - Outline Stages
            ##### 1.3 Troubleshoot data ingestion.
            ##### 1.4 Design, build and troubleshoot continuous data pipelines.
            - Design a data pipeline that forces uniqueness but is not unique.
            - Stages 
            - Tasks
            - Streams
            - Snowpipe
            - Auto ingest as compared to Rest API
            ##### 1.5 Analyze and differentiate types of data pipelines.
            - Understand Snowpark architecture (client vs server)
            - Create and deploy UDFs and Stored Procedures using Snowpark
            - Design and use the Snowflake SLQ API
            ##### 1.6 Install, configure, and use connectors to connect to Snowflake.
            ##### 1.7 Design and build data sharing solutions. 
            - Implement a data share
            - Create a secure view
            - Implement row level filtering
            ##### 1.8 Outline when to use an External Table and define how they work.
            - Partitioning external tables
            - Materialized views
            - Partitioned data unloading
            """)

        # Performance Optimization
        with tab7:
            st.markdown("""
            ##### 2.1 Troubleshoot underperforming queries.
            - Identify underperforming queries
            - Outline telemetry around the operation
            - Increase efficiency
            - Identify the root cause
            ##### 2.2 Given a scenario, configure a solution for the best performance.
            - Scale out vs. scale in
            - Cluster vs. increase warehouse size
            - Query complexity
            - Micro partitions and the impact of clustering
            - Materialized views
            - Search optimization
            ##### 2.3 Outline and use caching features.
            ##### 2.4 Monitor continuous data pipelines.
            - Snowpipe 
            - Stages
            - Tasks
            - Streams
            """)

        # Storage and Data Protection
        with tab8:
            st.markdown("""
            ##### 3.1 Implement data recovery features in Snowflake. 
            - Time Travel
            - Fail-safe
            ##### 3.2 Outline the impact of Streams on Time Travel. 
            ##### 3.3 Use System Functions to analyze Micro-partitions. 
            - Clustering depth
            - Cluster keys
            ##### 3.4 Use Time Travel and Cloning to create new development environments.
            - Backup databases
            - Test changes before deployment
            - Rollback
            """)

        # Security
        with tab9:
            st.markdown("""
            ##### 4.1 Outline Snowflake security principles. 
            - Authentication methods (Single Sign On, Key Authentication, Username/Password, MFA)
            - Role Based Access Control (RBAC)
            - Column Level Security and how data masking works with RBAC to secure sensitive data
            ##### 4.2 Outline the System Defined Roles and when they should be applied.
            - The purpose of each of the System Defined Roles including best practices usage in each case
            - The primary differences between SECURITYADMIN and USERADMIN roles
            - The difference between the purpose and usage of the USERADMIN/SECURITYADMIN roles and SYSADMIN
            ##### 4.3 Manage Data Governance.
            - Explain the options available to support column level security including Dynamic Data Masking and External Tokenization
            - Explain the options available to support row level security using Snowflake Row Access Policies
            - Use DDL required to manage Dynamic Data Masking and Row Access Policies
            - Use methods and best practices for creating and applying masking policies on data
            - Use methods and best practices for Object Tagging 
            """)

        # Data Transformation
        with tab10:
            st.markdown("""
            ##### 5.1 Define User-Defined Functions (UDFs) and outline how to use them.
            - Secure UDFs
            - SQL UDFs
            - JavaScript UDFs
            - Returning Table Value vs. Scalar Value
            ##### 5.2 Define and create External Functions. 
            - Secure External Functions
            ##### 5.3 Design, Build, and Leverage Stored Procedures.
            - Transaction management 
            ##### 5.4 Handle and transform semi-structured data.
            - Traverse and transform semi-structured data to structured data
            - Transform structured to semi-structured data
            ##### 5.5 Use Snowpark for data transformation.
            - Query and filter data using the Snowpark library
            - Perform data transformations using Snowpark (ie., aggregations)
            - Join Snowpark dataframes 
            """)

# Study Resources
with tab3:
    st.subheader("Study Resources")
    data = links
    df = pd.DataFrame(data, columns=['Link'])
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
    q1l1 = st.write("Running the below clustering information analysis function:")
    q1l2 = st.write("SELECT SYSTEM$CLUSTERING_INFORMATION('table1", "(col1, col2)")
    q1 = st.radio("On Table1, that is not clustered, will return which of the following?", 
                    ("An error: this function works only on clustered tables.",
                     "Clustering information on all tables: this function clusters all tables by default.",
                     "Clustering information: the information will be presented as if the table was clustered by col1, col2.",
                     "An error: this function does not accept lists of columns as a second parameter."))
    if q1 == "Clustering information on all tables: this function clusters all tables by default.":
        st.write("✅")
    else:
        st.write("❌")
    # q2l1 = st.write("A Data Engineer has inherited a database and is monitoring a table with the below query every 30 days:")
    # q2l2 = st.write("SELECT SYSTEM$CLUSTERING_INFORMATION('orders', '(o_orderdate)');")
    # q2l3 = st.write("The Engineer gets the first two results (e.g., Day 0 and Day 30).")
    # st.image("img\day0.PNG")
    # st.image("img\day30p1.PNG")
    # st.image("img\day30p2.PNG")
    # q2 = st.radio("How should the Engineer interpret these results?",
    #              ("The table is well organized for queries that range over column o_orderdate. Over time, this organization is degrading.",
    #               "The table was initially well organized for queries that range over column o_orderdate. Over time, this organization has improved further.",
    #               "The table was initially not organized for queries that range over column o_orderdate. Over time, this organization has changed.",
    #               "The table was initially poorly organized for queries that range over column o_orderdate. Over time, this organization has improved."))
    # if q2 == "The table is well organized for queries that range over column o_orderdate. Over time, this organization is degrading.":
    #     st.write("✅")
    # else:
    #     st.write("❌")
    q3 = st.radio("A Data Engineer is preparing to load staged data from an external stage using a task object. \
                  Which of the following practices will provide the MOST efficient load performance?",
                  ("Store the files on the external stage to ensure caching is maintained.",
                   "PUT all files in a single directory",
                   "Limit file names to under 30 characters",
                   "Organize files into logical paths that reflect a scheduling pattern"))
    if q3 == "Organize files into logical paths that reflect a scheduling pattern":
        st.write("✅")
    else:
        st.write("❌")
    q4 = st.radio("A Data Engineer is working on a project that requires data to be moved directly from an internal stage to an external stage. \
                  Which of the following is the QUICKEST way to accomplish that?", 
                  ("COPY INTO @myExtStage from (SELECT $1, $2, ... @myInternalStage);",
                   "Copy the data from the internal stage to a table and then unload the data to an external stage",
                   "COPY INTO @myExtStage from @myInternalStage;",
                   "Write a custom script to move the data"))
    if q4 == "COPY INTO @myExtStage from (SELECT $1, $2, ... @myInternalStage);":
        st.write("✅")
    else:
        st.write("❌")
    q5l1 = st.write("The S1 schema contains two permanent tables that were created as shown below:")
    q5l2 = st.write("CREATE TABLE table_a (c1 INT)")
    q5l3 = st.write("DATA_RETENTION_TIME_IN_DAYS = 10;")
    q5l4 = st.write("CREATE TABLE table_b (c1 INT);")
    q5 = st.radio("What will be the impact of running the following command: ALTER SCHEMA S1 SET DATA_RETENTION_TIME_IN_DAYS = 20;",
                 ("The retention time on table_a does not change; table_b is set to 20 days.",
                  "An error will be generated; a data retention time on a schema cannot be set.",
                  "The retention time on both tables will be set to 20 days.",
                  "The retention time will not change on either table."))
    if q5 == "The retention time on table_a does not change; table_b is set to 20 days.":
        st.write("✅")
    else:
        st.write("❌")