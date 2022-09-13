# Exam Study Guide
# Last Updated: March 1, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.adm import links, links2

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Administrator")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: March 1, 2022")
    adbd = {"Domain": ["Snowflake Security, RBAC, & User Administration", "Account Management & Data Governance", "Performance Monitoring & Tuning", "Data Sharing, Data Exchange, & Data Marketplace", "Disaster Recovery, Backup, & Data Replication"],
           "Estimated Percentage Range": ["25-30%", "25-30%", "20-25%", "10-15%", "10-15%"]}
    df = pd.DataFrame(data=adbd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10, tab11 = st.tabs(["Snowflake Security, RBAC, & User Administration", "Account Management & Data Governance", "Performance Monitoring & Tuning", "Data Sharing, Data Exchange, & Data Marketplace", "Disaster Recovery, Backup, & Data Replication"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
    
    # Snowflake Security, RBAC, & User Administration
    with tab7:
        st.markdown("""
        ##### 1.1 Set up and manage Snowflake authentication
        - Establish federated authentication and Single Sign-on (SSO)
          + Implement federated authentication/SSO as it relates to Snowflake
          + Configure an Identity Provider (IdP) for Snowflake
          + Configure, use, and manage federated authentication with Snowflake.
        - Implement Multi-Factor Authentication (MFA)
          + Enroll a Snowflake user in MFA
          + Use MFA with different Snowflake drivers (such as Web UI, SnowSQL, JDBC, ODBC, etc.)
          + Monitor users who do not have MFA enabled
          + Reset passwords and temporarily disable or permanently remove MFA from a user
        - Perform key pair authentication and key pair rotation
          + Create, set up, and configure a Snowflake user for key pair authentication
          + Configure key pair rotation
        - Configure and use OAuth
          + How does OAuth 2.0 work as it relates to Snowflake?
          + Configure Snowflake OAuth for custom clients
          + Configure Snowflake OAuth for technology partners (such as, Tableau, Looker, Microsoft Power BI)
          + Outline how Snowflake OAuth is impacted by federated authentication, network policies, and private connectivity
        ##### 1.2 Set up and manage network and private connectivity
        - Establish network policies
          + Configure and manage network policies at the account level and user level
          + Describe network level inheritance when both account-level and user-level
        network policies exist
        - Establish private connectivity to Snowflake internal stages
          + Implement and manage cloud provider interfaces and private endpoints for internal stages (for example, AWS VPC, Azure)
        - Establish private connectivity to the Snowflake service
          + Implement and manage private link connectivity between cloud providers and Snowflake
        - Access the Snowflake SQL API
        - Use IP address whitelists/allowed lists and blocked lists for access using network access policies
        ##### 1.3 Set up and manage security administration and authorization
        - Use and monitor SCIM
          + Describe SCIM and its use cases as they relate to Snowflake
          + Manage users and groups with SCIM
          + Enable, configure, and manage SCIM integration
        - Prevent data exfiltration with PREVENT_UNLOAD_TO_INLINE_URL/REQUIRE_STORAGE_INTEGRATION_FOR_STAGE_CREATION
        - Manage service accounts, API integration, and automated authentication (for example, key pair)
        ##### 1.4 Given a set of business requirements, establish access control architecture
        - Access control framework
        - Securable objects
        - Describe the uses for, and hierarchy of, system-defined roles such as ORGADMIN, ACCOUNTADMIN, SYSADMIN, SECURITYADMIN, and USERADMIN.
          + Use cases for custom security roles
        - Privilege inheritance
        - Use an enforcement model
        - Demonstrate how to grant access to specific objects within a database that requires privilege inheritance
        ##### 1.5 Given a scenario, create and manage access control
        - List and and use the different privileges available for each object type in Snowflake
        - Custom security roles and users (for example, include related SHOW commands)
        - Audit user activity history and query activity history across a Snowflake account 
        ##### 1.6 Given a scenario, configure access controls
        - Use system-defined roles
        - Create custom roles
        - Implement inheritance and nesting of system-defined roles
        - Follow best practices for using and securing the ACCOUNTADMIN role
        - Align usage of object access with business functions
        - Describe cloned objects and their impact on granted privileges
        - Designate additional administrators in Snowflake
        - View granted privileges to users, roles, and ON objects
        - Implement and manage future grants including restrictions and limitations
        - Evaluate the various scenarios using warehouse grants (for example, USAGE, OPERATE, MODIFY, MONITOR)
        - Implement and manage managed access schemas
        - Provide access to a non-account administrator to monitor billing and usage information
        - Manage account-level permissions 
        """)
    
    # Account Management & Data Governance
    with tab8:
        st.markdown("""
        ##### 2.1 Manage organizations and accounts
        - Describe the benefits of an organization
        - Describe organizational tasks
          + Create and name an organization
          + Name various types of organization accounts
          + Identify what regions are available for a given organization
        - Understand account tasks
          + View, create, and list accounts
          + Change account names
          + Enable replication for accounts
          + Delete accounts
          + Describe the implications of the timing related to adopting Snowflake releases
        ##### 2.2 Manage organization security and access control
        - Follow best practice when using the ORGADMIN role
        - Compare the differences between ORGADMIN and ACCOUNTADMIN roles
        ##### 2.3 Implement and manage data governance in Snowflake
        - Mask column data in Snowflake
          + Implement and manage column-level security using Dynamic Data Masking policies
          + Use external tokenization to protect Personally Identifiable Information (PII)
            + Describe the difference between data masking and external tokenization
          + Manage security for advanced column level security
        - Implement and manage row access policies
          + Configure a row access policy on a table and map the flow
          + Compare row access policies to secure views when mapping tables
        - Perform auditing of access history
          + Audit access history details using the access history views
        - Use tagging in Snowflake
          + Identify use cases where tagging would be beneficial
          + Implement and manage tagging
        ##### 2.4 Given a scenario, manage account identifiers
        - Describe the differences between account names and account locators
        - Identify when a given account identifier needs to be used
        - Use region groups
        ##### 2.5 Given a scenario, manage databases, tables, and views
        - Implement Snowflake table structures
        - Establish and use temporary and transient tables
        - Establish and use external tables
        - Implement and manage views, secure views, and materialized views 
        - Outline table design considerations
        - Outline the use cases when cloning is beneficial
        - Outline data storage and data retention considerations
        ##### 2.6 Perform queries in Snowflake
        - Use Snowflake sequences
        - Use persisted query results
        - Demonstrate the ability to cancel statements for both a single user as well as for other users
        - Use query history filters including client-generated queries and queries executed by user tasks
        - Visualize query results with Snowsight
          + Use Snowsight dashboards to monitor activity
          + Share worksheets and dashboards
          + Generate and share Snowsight charts
        ##### 2.7 Given a scenario, stage data in Snowflake
        - Stage data files from a local file system
        - Create, manage, and maintain Snowflake internal and external stages
          + Data exfiltration, storage integrations, etc.
        ##### 2.8 Given a scenario, manage database streams and tasks
        - Outline database tasks and associated use cases
          + Schedule tasks
          + Warehouse assignments
          + Permissions required for creating and executing tasks
          + Troubleshoot task historical runs
        - Outline database streams and associated use cases
          + Create, monitor and consume streams
        """)

    # Performance Monitoring & Tuning
    with tab9:
        st.markdown("""
        ##### 3.1 Given business requirements, design, manage, and maintain virtual warehouses
        - Outline the impact on billing, data loading, and query processing based on warehouse sizes
          + Assigning access to virtual warehouses
          + Auto-suspension
          + Auto-resumption
        - Given a scenario, manage warehouse usage in sessions and size the warehouse accordingly
        - Given a scenario, manage a multi-cluster warehouse
          + Describe use cases and benefits
          + Describe, establish, and maintain a scaling policy
          + Monitor effects on billing and costs
          + Monitor multi-cluster warehouses
        ##### 3.2 Monitor Snowflake performance
        - Evaluate and interpret query profiles to improve performance
          + Describe the components of the query profilers:
            + Steps
            + Operator tree
            + Operator nodes
            + Operator types
          + Compare compile versus runtime optimizations
          + Identify/create efficient queries
            + Articulate the execution path
            + Use effective joining conditions
            + Perform grouping, sorting, and ordering
          + Troubleshoot common errors in the query profiler
          + If data spilling is present, describe its impact and remediation tactics
          + If data pruning is present, describe its impact and remediation tactics
          + Describe the various timeout parameters
        - Use an explain plan
        - Compare and contrast different caching techniques available in Snowflake and the impact of caching on performance
        - Resultset cache
        - Local disk (warehouse) cache
          + What is the impact of warehouse resumption/suspension on local disk cache?
        - Remote disk cache
        - Metadata cache
        - Implement performance improvements
          + Recommend the use of materialized views and use cases
          + Use the search optimization service
          + Create external tables
          + Assign cluster keys
          + Use data caching
        ##### 3.3 Manage DML locking and concurrency in Snowflake
        - Describe DML concurrency considerations
        - Follow best practices for DML locking and concurrency
        - Monitor transaction activity
          + Abort transactions, etc.
        ##### 3.4 Given a scenario, implement resource monitors
        - Create, manage, modify, and remove resource monitors based on use cases and business requirements
          + Set up notifications for resource monitors
        ##### 3.5 Interpret and make recommendations for data clustering
        - Configure and maintain cluster keys
          + Articulate effective strategies and system tools to support system$clustering_information, and cardinality
          + Create and enable cluster keys
            + outline a methodology for explicit clustering
          + Use the automatic clustering service
            + monitor and assess usage
          + Follow best practices for clustering
            + Lowest cardinality column first
            + Fewer columns is generally better
            + Verify table scan is the problem - otherwise a cluster key will not help
        - Describe micro-partitions, their benefits, and their impact
        - Retrieve clustering information
          + Clustering depth
          + Clustering ratio
          + Clustering histogram
        ##### 3.6 Manage costs and pricing
        - Manage organization costs
          + Describe the differences between account_usage and organization_usage
          + Monitor accounts and usage
            + Use the SNOWFLAKE_ORGANIZATION_USAGE command
        - Forecast and monitor costs and pricing
          + Enable resource monitor notifications
          + When should warehouses be suspended or resumed based on cost and pricing?
        - Describe the use cases for the account_usage and information_schema
          + What views are available from the information_schema?
        - Monitor and calculate data storage usage/credit
        - Monitor and calculate data transfer costs
        - Monitor and calculate data replication costs
        - Monitor and calculate warehouse usages/credits
          + Demonstrate cost saving strategies
          + Use resource monitors
        - Describe how Snowflake credits are consumed by service layer activities such as Snowpipe, materialized views, and automatic clustering
        - Apply techniques for reducing costs
        """)

    # Data Sharing, Data Exchange, & Data Marketplace 
    with tab10:
        st.markdown("""
        ##### 4.1 Manage and implement data sharing
        - Given a scenario, implement sharing solutions and impacts
          + Types of sharing (one to one/one to many, private exchange, Data Marketplace)
          + Sharing among different editions of Snowflake
          + Sharing cross-regions or cross-clouds
            + The role of replications
          + Configure data sharing programmatically
            + Share different types of data objects including secure functions
            + Describe the role of context functions in data sharing
        - Manage data providers and consumers
          + Create, manage, and maintain an outbound data share
          + Share objects securely in a data share (for example, what type to use)
          + Use secure objects to share data
            + Secure views
            + Secure User-defined Functions (UDFs)
          + Create, manage and maintain readers accounts
            + Create user and role for access
            + Create resource monitors
            + Create objects
            + Determine if there is a need to store data (CREATE DATABASE)
          + Enable access from Business Critical to non-Business Critical accounts
          + Import, manage, and maintain inbound data shares
        ##### 4.2 Use the Snowflake Data Exchange
        - Manage administration and membership
        - Access the Data Exchange
        - Outline the process of becoming a data provider
          + Create, edit or delete provider profiles
        - Manage data listings
          + Publish, edit, unpublish, or republish data listings
        ##### 4.3 Use the Snowflake Data Marketplace
        - Access Snowflake Data Marketplace to browse listings
          + Request access to a Snowflake Data Marketplace listing (as a consumer)
        - Request that new data or a data provider be added to the Snowflake Data Marketplace
          + Create and manage data provider profiles
          + Create, submit, manage, and modify a data listing
        - Manage listing requests
          + View and manage pending listing requests
        - Manage data listings
        """)

    # Disaster Recovery, Backup, & Data Replication
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
        ##### 5.5 Outline different data schemas.
        - Star
        - Data lake
        - Data vault
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
    **Q1: An Administrator at a healthcare company needs to share data with a university medical institute. \
          There is no Protected Health Information (PHI) in the data. The healthcare company is running a \
          Business Critical edition of Snowflake and the Institute is running an Enterprise edition. \
          How can this data share be accomplished?**
    - A. The Administrator will need to change the institute's Snowflake edition to Business Critical while the data is being shared.
    - B. The healthcare company will need to change its Snowflake edition to Enterprise temporarily while the data is being shared.
    - C. The Administrator of the institute needs to raise a support ticket authorizing Snowflake Support to execute the share request.
    - D. The Administrator needs to set share_restrictions on the shared object to FALSE.
    """)
    q1 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=0)
    if q1 == "D":
        st.write("✅ That's correct!")
    elif q1 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q2
    q2_text = st.markdown("""
    **Q2: Two different roles are running queries on a production database. The queries are similar in complexity and duration, \
          and there is generally about 3 minutes of idle time between queries. Typically, there are 2 or 3 queries running at a time \
          for each role. Users in the Finance role are querying one set of tables, and users in the Engineering role are querying a different set of tables. \
          What is the optimal approach to set up the virtual warehouse(s) based on this scenario?**
    - A. Each role should have its own virtual warehouse to make efficient use of caching.
    - B. The two roles should share a warehouse since each role's queries are similar in complexity and duration.
    - C. The two roles should share a warehouse with a short auto-suspend (less than 10 seconds) to reduce compute costs.
    - D. Each role should have its own warehouse with a short auto-suspend (less than 10 seconds) to save on compute costs.
    """)
    q2 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=1)
    if q2 == "A":
        st.write("✅ That's correct!")
    elif q2 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q3
    q3_text = st.markdown("""
    **Q3: Which of the following objects within a database are replicated to the secondary database during database replication? (Select 3)**
    - A. Sequences
    - B. Pipes
    - C. Streams
    - D. Stored Procedures
    - E. Policies
    - F. Tasks
    """)
    q3 = st.selectbox("Answers:", ("", "A, B, C", "A, C, D", "A, D, E", "A, E, F", "B, C, D", "B, D, E", "B, E, F", "C, D, E", "C, E, F", "D, E, F"), key=2)
    if q3 == "A, D, E":
        st.write("✅ That's correct!")
    elif q3 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: An Administrator has been asked to create a developer environment off of the prod database with complete isolation \
          for a team of dev users. Using zero-copy cloning, the Administrator issues the following command: \
          ```CREATE OR REPLACE DATABASE dev CLONE prod; create or replace warehouse dev_wh with warehoues_size = 'SMALL';``` \
          The prod database has views and tables only, and grants on any other first-class objects exist. \
          Based on this scenario, what combination of GRANTS need to be issued to create a role with the access controls to process \
          workload isolation? (Select 2)**
    - A. ```grant all on database dev to role devrole;```
    - B. ```grant usage on dev to warehouse dev_wh;```
    - C. ```grant all on database dev to role devrole; grant all on all schemas in database dev to role devrole; grant all on all tables in database dev to role devrole; grant all on all views in database dev to role devrole;```
    - D. ```grant all on warehouse dev_wh to role devrole;```
    - E. ```grant all on database dev to role devrole with grant option;```
    - F. ```grant all on database dev to role devrole; grant all on all schemas in database dev to role devrole;```
    """)
    q4 = st.selectbox("Answers:", ("", "A, B", "A, C", "A, D", "A, E", "A, F", "B, C", "B, D", "B, E", "B, F", "C, D", "C, E", "C, F", "D, E", "D, F", "E, F"), key=3)
    if q4 == "C, D":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q5
    q5_text = st.markdown("""
    **Q5: A table has a dynamic data masking policy defined on its cc_num column. The masking policy allows the role SECURE_ROLE \
          to view the credit card number; all other roles will see just a series of asterisks. What will happen if a Snowflake Administrator \
          shares this table with another Snowflake account?**
    - A. If the consumer account has a role named SECURE_ROLE, only that role will be able to see the unmasked value in cc_num.
    - B. The consumer account will only see asterisks in the cc_num column, regardless of which role is used to access the data.
    - C. The Administrator cannot share a table that has a dynamic data masking policy applied to one of its columns.
    - D. Any queries against the table will completely omit the cc_num column from the result set that is returned.
    """)
    q5 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=4)
    if q5 == "B":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")