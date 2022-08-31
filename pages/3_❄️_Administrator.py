# Exam Study Guide
# Last Updated: March 1, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.adm import links

# App Code
st.header("SnowPro Advanced: Administrator")

tab1, tab2, tab3 = st.tabs(["Exam Breakdown", "Randomizer", "Sample Questions"])

with tab1:
    st.subheader("Exam Breakdown")
    adbd = {"Domain": ["Snowflake Security, RBAC, & User Administration", "Account Management & Data Governance", "Performance Monitoring & Tuning", "Data Sharing, Data Exchange, & Data Marketplace", "Disaster Recovery, Backup, & Data Replication"],
           "Estimated Percentage Range": ["25-30%", "25-30%", "20-25%", "10-15%", "10-15%"]}
    df = pd.DataFrame(data=adbd)
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
    q1 = st.radio("An Administrator at a healthcare company needs to share data with a university medical institute. \
                  There is no Protected Health Information (PHI) in the data. The healthcare company is running a \
                  Business Critical edition of Snowflake and the Institute is running an Enterprise edition. \
                  How can this data share be accomplished?", 
                  ("The Administrator will need to change the institute's Snowflake edition to Business Critical while the data is being shared",
                   "The healthcare company will need to change its Snowflake edition to Enterprise temporarily while the data is being shared.",
                   "The Administrator of the institute needs to raise a support ticket authorizing Snowflake Support to execute the share request.",
                   "The Administrator needs to set share_restrictions on the shared object to FALSE."))
    if q1 == "The Administrator needs to set share_restrictions on the shared object to FALSE.":
        st.write("✅")
    else:
        st.write("❌")  
    q2l1 = st.write("Two different roles are running queries on a production database. The queries are similar in complexity and duration, \
                    and there is generally about 3 minutes of idle time between queries. Typically, there are 2 or 3 queries running at a time \
                    for each role.")
    q2l2 = st.write("Users in the Finance role are querying one set of tables, and users in the Engineering role are querying a different set of tables.")
    q2 = st.radio("What is the optimal approach to set up the virtual warehouse(s) based on this scenario?",
                  ("Each role should have its own virtual warehouse to make efficient use of caching.",
                   "The two roles should share a warehouse since each role's queries are similar in complexity and duration.",
                   "The two roles should share a warehouse with a short auto-suspend (less than 10 seconds) to reduce compute costs.",
                   "Each role should have its own warehouse with a short auto-suspend (less than 10 seconds) to save on compute costs."))
    if q2 == "Each role should have its own virtual warehouse to make efficient use of caching.":
       st.write("✅")
    else:
        st.write("❌")
    q3l1 = st.write("Which of the following objects within a database are replicated to the secondary database during database replication?")
    q3l2 = st.write("A. Sequences")
    q3l3 = st.write("B. Pipes")
    q3l4 = st.write("C. Streams")
    q3l5 = st.write("D. Stored Procedures")
    q3l6 = st.write("E. Policies")
    q3l7 = st.write("F. Tasks")
    q3 = st.text_input("Choose 3 answers by typing in their letters.", key=0)
    if q3 == "A, D, E" or q3 == "A, D, and E" or q3 == "A, D and E" or q3 == "A, D & E":
        st.write("✅")
    else:
        st.write("❌")
    q4l1 = st.write("An Administrator has been asked to create a developer environment off of the prod database with complete isolation \
                    for a team of dev users. Using zero-copy cloning, the Administrator issues the following command:")
    q4l2 = st.write("CREATE OR REPLACE DATABASE dev CLONE prod;")
    q4l3 = st.write("create or replace warehouse dev_wh with warehoues_size = 'SMALL';")
    q4l4 = st.write("The prod database has views and tables only, and grants on any other first-class objects exist.")
    q4 = st.radio("Based on this scenario, what combination of GRANTS need to be issued to create a role with the access controls to process \
                  workload isolation? (Select 2)", ("grant all on database dev to role devrole;", "grant usage on dev to warehouse dev_wh;",
                  "grant all on database dev to role devrole; grant all on all schemas in database dev to role devrole; grant all on all tables in database dev to role devrole; grant all on all views in database dev to role devrole",
                  "grant all on warehouse dev_wh to role devrole;",
                  "grant all on database dev to role devrole with grant option;",
                  "grant all on database dev to role devrole; grant all on all schemas in database dev to role devrole;"))
    if q4 == "C, D" or q4 == "C and D" or q4 == "C & D":
       st.write("✅")
    else:
        st.write("❌")
    q5l1 = st.write("A table has a dynamic data masking policy defined on its cc_num column. The masking policy allows the role SECURE_ROLE \
                    to view the credit card number; all other roles will see just a series of asterisks.")
    q5 = st.radio("What will happen if a Snowflake Administrator shares this table with another Snowflake account?",
                    ("If the consumer account has a role named SECURE_ROLE, only that role will be able to see the unmasked value in cc_num.",
                    "The consumer account will only see asterisks in the cc_num column, regardless of which role is used to access the data.",
                    "The Administrator cannot share a table that has a dynamic data masking policy applied to one of its columns.",
                    "Any queries against the table will completely omit the cc_num column from the result set that is returned."))
    if q5 == "The consumer account will only see asterisks in the cc_num column, regardless of which role is used to access the data.":
        st.write("✅")
    else:
        st.write("❌")