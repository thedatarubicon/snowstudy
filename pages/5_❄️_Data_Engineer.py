# Exam Study Guide
# Last Updated: September 27, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from PIL import Image
from links.de import links, dict

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Data Engineer")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: September 27, 2022")
    debd = {"Domain": ["Data Movement", "Performance Optimization", "Storage and Data Protection", "Security", "Data Transformation"], 
           "Estimated Percentage Range": ["25-30%", "20-25%", "10-15%", "10-15%", "25-30%"]}
    df = pd.DataFrame(data=debd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10, tab11 = st.tabs(["Data Movement", "Performance Optimization", "Storage and Data Protection", "Security", "Data Transformation"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Data Movement
        with tab7:
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
        with tab8:
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
        with tab9:
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
        with tab10:
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
        with tab11:
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
    for i in links:
        st.write(i)

# Generator
with tab4:
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
          opt = st.selectbox("Study Resource Topic", options=dict.keys(), key=0)
          for key, value in dict.items():
              if opt == key:
                  for i in value:
                      st.write(i)
        with col2:
            url = st.text_input("Input URL:", max_chars=1000)
            if url:
                st.write("Study Resource:", url)
                components.iframe(url, width=750, height=675, scrolling=True)

# Randomizer
with tab5:
    st.subheader("Randomizer")
    if st.button("Generate Study Resource"):
        link = random.choice(links)
        st.write("Study Resource:", link)
        components.iframe(link, width=715, height=550, scrolling=True)
    else:
        st.write("")

# Sample Questions
with tab6:
    st.subheader("Sample Questions")

    # Q1
    q1_text = st.markdown("""
    **Q1: Running the below clustering information analysis function: \
          ```SELECT SYSTEM$CLUSTERING_INFORMATION('table1', '(col1, col2)')``` \
          on ```TABLE1```, that is not clustered, will return which of the following?**
    - A. An error: this function works only on clustered tables.
    - B. Clustering information on all tables: this function clusters all tables by default.
    - C. Clustering information: the information will be presented as if the table was clustered by col1, col2.
    - D. An error: this function does not accept lists of columns as a second parameter.
    """)
    q1 = st.selectbox("Answers:", ("", "A", "B", "C", "D"), key=1)
    if q1 == "B":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q2
    q2_text = st.markdown("""
    **Q2: A Data Engineer has inherited a database and is monitoring a table with the below query every 30 days: \
          ```SELECT SYSTEM$CLUSTERING_INFORMATION('orders', '(o_orderdate)');```\
          The Engineer gets the first two results (e.g., Day 0 and Day 30).\
          How should the Engineer interpret these results?**
    """)
    day0 = Image.open("./img/day0.PNG")
    day30_p1 = Image.open("./img/day30p1.PNG")
    day30_p2 = Image.open("./img/day30p2.PNG")
    st.image(day0, output_format="PNG")
    st.image(day30_p1, output_format="PNG")
    st.image(day30_p2, output_format="PNG")
    q2_text_2 = st.markdown("""
    - A. The table is well organized for queries that range over column o_orderdate. Over time, this organization is degrading.
    - B. The table was initially well organized for queries that range over column o_orderdate. Over time, this organization has improved further.
    - C. The table was initially not organized for queries that range over column o_orderdate. Over time, this organization has changed.
    - D. The table was initially poorly organized for queries that range over column o_orderdate. Over time, this organization has improved.
    """)
    q2 = st.selectbox("Answers:", ("", "A", "B", "C", "D"), key=2)
    if q2 == "A":
        st.write("✅ That's correct!")
    elif q2 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q3
    q3_text = st.markdown("""
    **Q3: A Data Engineer is preparing to load staged data from an external stage using a task object. \
          Which of the following practices will provide the MOST efficient load performance?**
    - A. Store the files on the external stage to ensure caching is maintained.
    - B. PUT all files in a single directory
    - C. Limit file names to under 30 characters
    - D. Organize files into logical paths that reflect a scheduling pattern
    """)
    q3 = st.selectbox("Answers:", ("", "A", "B", "C", "D"), key=3)
    if q3 == "D":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: A Data Engineer is working on a project that requires data to be moved directly from an internal stage to an external stage. \
          Which of the following is the QUICKEST way to accomplish that?**
    - A. COPY INTO @myExtStage from (SELECT $1, $2, ... @myInternalStage);
    - B. Copy the data from the internal stage to a table and then unload the data to an external stage
    - C. COPY INTO @myExtStage from @myInternalStage;
    - D. Write a custom script to move the data
    """)
    q4 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=4)
    if q4 == "A":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # q5
    q5_text = st.markdown("""
    **Q5: The S1 schema contains two permanent tables that were created as shown below: \
           ```CREATE TABLE table_a (c1 INT); DATA_RETENTION_TIME_IN_DAYS = 10; CREATE TABLE table_b (c1 INT);``` \
           What will be the impact of running the following command: ```ALTER SCHEMA S1 SET DATA_RETENTION_TIME_IN_DAYS = 20;```**
    - A. The retention time on table_a does not change; table_b is set to 20 days.
    - B. An error will be generated; a data retention time on a schema cannot be set.
    - C. The retention time on both tables will be set to 20 days.
    - D. The retention time will not change on either table.
    """)
    q5 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=5)
    if q5 == "A":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")