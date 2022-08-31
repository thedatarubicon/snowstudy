# Exam Study Guide
# Last Updated: May 3, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.sa import links

# App Code
st.header("SnowPro Advanced: Architect")

tab1, tab2, tab3 = st.tabs(["Exam Breakdown", "Randomizer", "Sample Questions"])

with tab1:
    st.subheader("Exam Breakdown")
    abd = {"Domain": ["Accounts & Security", "Snowflake Architecture", "Data Engineering", "Performance Optimization"], 
           "Estimated Percentage Range": ["25-30%", "20-25%", "15-20%", "20-25%"]}
    df = pd.DataFrame(data=abd)
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
    q1 = st.radio("Which of the following ALTER commands will impact a column's availability in Time Travel?",
                 ("ALTER TABLE ... SET DATA TYPE ...", "ALTER TABLE ... RENAME COLUMN ...", "ALTER TABLE ... SET NOT NULL ...", "ALTER TABLE ... DROP COLUMN ..."))
    if q1 == "ALTER TABLE ... SET DATA TYPE ...":
        st.write("✅")
    else:
        st.write("❌")
    q2 = st.radio("A user has a table named CURRENT_EMPLOYEE and would like to create a new table named CURRENT_EMPLOYEE_COPY_DATA, copying only the table structure from the CURRENT_EMPLOYEE table. Which query should be run?", 
                 ("CREATE TABLE current_employee_copy_data COPY current_employee;", "CREATE TABLE current_employee_copy_data LIKE current_employee;", "CREATE TABLE current_employee_copy_data CLONE current_employee;", "CREATE TABLE current_employee_copy_data as SELECT * from current_employee;"))
    if q2 == "CREATE TABLE current_employee_copy_data LIKE current_employee;":
        st.write("✅")
    else:
        st.write("❌")
    q3 = st.radio("Person1 is using the role SECURITYADMIN. Person 1 creates a role named DBA_ROLE that will manage the warehouses in the Snowflake account. Person1 now needs to switch to that role. What commands are needed to be executed in order to switch the context of this worksheet?",
                  ("USE ROLE DBA_ROLE;", "GRANT ROLE DBA_ROLE TO ROLE SECURITYADMIN;", "The SECURITYADMIN role is not allowed to GRANT permissions to a role.", "GRANT ROLE DBA_ROLE TO USER PERSON1; USE ROLE DBA_ROLE;"))
    if q3 == "GRANT ROLE DBA_ROLE TO USER PERSON1; USE ROLE DBA_ROLE;":
        st.write("✅")
    else:
        st.write("❌")
    q4 = st.radio("A table is created using the following syntax: CREATE TABLE MY_TABLE (NAME STRING(100)); What would the command DESC TABLE MY_TABLE; display as the column type?",
                  ("String", "Char", "Text", "Varchar"))
    if q4 == "Varchar":
        st.write("✅")
    else:
        st.write("❌")  
    q5l1 = st.write("How can data sharing be used across regions and cloud platforms?")
    q5l2 = st.write("A. Data can be shared across regions using database replication, but not across different cloud providers.")
    q5l3 = st.write("B. Data can be replicated to a different region and a share can be created on that replica.")
    q5l4 = st.write("C. A share cannot be created on a replica, so sharing across regions and cloud platforms is not possible.")
    q5l5 = st.write("D. Data can be cloned across regions and a share can be created on the clone.")
    q5l6 = st.write("E. Data can be replicated to a different cloud provider and a share can be created on the replica.")
    q5 = st.text_input("Choose 2 answers by typing in their letters.", key=1)
    if q5 == "B, E" or q5 == "B and E" or q5 == "B & E":
        st.write("✅")
    else:
        st.write("❌")   