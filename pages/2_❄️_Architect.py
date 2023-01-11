# Exam Study Guide
# Last Updated: May 3, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.sa import links, links2, lg, ra, sd, as_dict, dict

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Architect")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: May 3, 2022")
    abd = {"Domain": ["Accounts & Security", "Snowflake Architecture", "Data Engineering", "Performance Optimization"], 
           "Estimated Percentage Range": ["25-30%", "20-25%", "15-20%", "20-25%"]}
    df = pd.DataFrame(data=abd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10 = st.tabs(["Accounts & Security", "Snowflake Architecture", "Data Engineering", "Performance Optimization"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Accounts & Security
        with tab7:
            st.markdown("""
            ##### 1.1 Design a Snowflake account and database strategy, based on business requirements.
            - Create and configure Snowflake parameters based on a central account and any additional accounts.
            - List the benefits and limitations of one Snowflake account as compared to multiple Snowflake accounts.
            ##### 1.2 Design an architecture that meets data security, privacy, compliance, and governance requirements.
            - Configure Role Based Access Control (RBAC) hierarchy
            - System roles and associated best practices
            - Data Access
            - Data Security
            - Compliance
            ##### 1.3 Outline Snowflake security principles and identify use cases where they should be applied.
            - Encryption
            - Network security
            - User, Role, Grants provisioning
            - Authentication
            """)

        # Snowflake Architecture
        with tab8:
            st.markdown("""
            ##### 2.1 Outline the benefits and limitations of various data models in a Snowflake environment.
            - Data Models
            ##### 2.2 Design data sharing solutions, based on different use cases
            - Use Cases
              + Sharing within the same organization/same Snowflake account
              + Sharing within a cloud region
              + Sharing across cloud regions
              + Sharing between different Snowflake accounts
              + Sharing to a non-Snowflake customer
              + Sharing across platforms
            - Data Marketplace
            - Data Exchange
            - Data Sharing Methods
            ##### 2.3 Create architecture solutions that support Development Lifecycles as well as workload requirements.
            - Data Lake and Environments
            - Workloads
            - Development Lifecycle Support
            ##### 2.4 Given a scenario, outline how objects exist within the Snowflake Object hierarchy and how the hierarchy impacts an architecture.
            - Roles
            - Warehouses
            - Object hierarchy
            - Database
            ##### 2.5 Determine the appropriate data recovery solution in Snowflake and how data can be restored.
            - Backup/Recovery
            - Disaster Recovery
            """)

        # Data Engineering
        with tab9:
            st.markdown("""
            ##### 3.1 Determine the appropriate data loading or data unloading solution to meet business needs.
            - Data sources
            - Ingestion of the data
            - Architecture Changes
            - Data unloading
            ##### 3.2 Outline key tools in Snowflake's ecosystem and how they interact with Snowflake.
            - Connectors
              + Kafka
              + Spark
              + Python
            - Drivers
              + JDBC
              + ODBC
            - API endpoints
            - SnowSQL
            ##### 3.3 Determine the appropriate data transformation solution to meet business needs.
            - Materialized Views, Views, and Secure Views
            - Staging layers and tables
            - Querying semi-structured data
            - Data processing
            - Stored Procedures
            - Streams and Tasks
            - Functions
              + External Functions
              + User-Defined Functions (UDFs)
            """)

        # Performance Optimization
        with tab10:
            st.markdown("""
            ##### 4.1 Outline performance tools, best practices, and appropriate scenarios where they should be applied.
            - Query profiling
            - Virtual warehouse configuration
            - Clustering
            - Search Optimization
            - Caching
            - Query rewrite
            ##### 4.2 Troubleshoot performance issues with existing architectures.
            - JOIN explosions
            - Warehouse selection (scaling up as compared to scaling out)
            - Best practices and optimization techniques
            - Duplication of data
            - Monitoring and Alerting
              + Statistics
              + Resource Monitoring
              + Account Usage and Information Schema
            """)
            
# Study Resources - maybe all and domain-specific?
with tab3: 
    st.subheader("Study Resources")
    for i in links:
        st.write(i)

# Generator
with tab4:
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            # for i in links:
            #     st.write(i)
            # option = st.selectbox("Resource Type", option=as_dict)
            # if option == option:
            #     st.write(as_dict)
            # st.write(as_dict)
            opt = st.selectbox("Study Resource Topic", options=dict.keys())
            if opt:
                opt2 = st.selectbox("Study Resource Type", options=as_dict.keys())
                for key, value in as_dict.items():
                    if opt2 == key:
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
    **Q1: Which of the following ALTER commands will impact a column's availability in Time Travel?**
    - A. ALTER TABLE ... SET DATA TYPE ...
    - B. ALTER TABLE ... RENAME COLUMN ...
    - C. ALTER TABLE ... SET NOT NULL ...
    - D. ALTER TABLE ... DROP COLUMN ...
    """)
    q1 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=0)
    if q1 == "A":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q2
    q2_text = st.markdown("""
    **Q2: A user has a table named CURRENT_EMPLOYEE and would like to create a new table named CURRENT_EMPLOYEE_COPY_DATA, copying only the table structure from the CURRENT_EMPLOYEE table. Which query should be run?**
    - A. CREATE TABLE current_employee_copy_data COPY current_employee;
    - B. CREATE TABLE current_employee_copy_data LIKE current_employee;
    - C. CREATE TABLE current_employee_copy_data CLONE current_employee;
    - D. CREATE TABLE current_employee_copy_data as SELECT * from current_employee;
    """)
    q2 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=1)
    if q2 == "B":
        st.write("✅ That's correct!")
    elif q2 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")    

    # Q3
    q3_text = st.markdown("""
    **Q3: Person1 is using the role SECURITYADMIN. Person 1 creates a role named DBA_ROLE that will manage the warehouses in the Snowflake account. Person1 now needs to switch to that role. What commands are needed to be executed in order to switch the context of this worksheet?**
    - A. USE ROLE DBA_ROLE;
    - B. GRANT ROLE DBA_ROLE TO ROLE SECURITYADMIN;
    - C. The SECURITYADMIN role is not allowed to GRANT permissions to a role.
    - D. GRANT ROLE DBA_ROLE TO USER PERSON1; USE ROLE DBA_ROLE;
    """)
    q3 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=2)
    if q3 == "D":
        st.write("✅ That's correct!")
    elif q3 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: A table is created using the following syntax: ```CREATE TABLE MY_TABLE (NAME STRING(100));``` What would the command ```DESC TABLE MY_TABLE;``` display as the column type?**
    - A. String
    - B. Char
    - C. Text
    - D. Varchar
    """)
    q4 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=3)
    if q4 == "D":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q5
    q5_text = st.markdown("""
    **Q5: How can data sharing be used across regions and cloud platforms? (Select 2)**
    - A. Data can be shared across regions using database replication, but not across different cloud providers.
    - B. Data can be replicated to a different region and a share can be created on that replica.
    - C. A share cannot be created on a replica, so sharing across regions and cloud platforms is not possible.
    - D. Data can be cloned across regions and a share can be created on the clone.
    - E. Data can be replicated to a different cloud provider and a share can be created on the replica.
    """)
    q5 = st.selectbox("Answers:", ("", "A, B", "A, C", "A, D", "A, E", "B, C", "B, D", "B, E", "C, D", "C, E", "D, E"), key=4)
    if q5 == "B, E":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.") 