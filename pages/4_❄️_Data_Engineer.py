# Exam Study Guide
# Last Updated: June 23, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from links.de import links

# App Code
st.header("SnowPro Advanced: Data Engineer")

tab1, tab2, tab3 = st.tabs(["Exam Breakdown", "Randomizer", "Sample Questions"])

with tab1:
    st.subheader("Exam Breakdown")
    debd = {"Domain": ["Data Movement", "Performance Optimization", "Storage and Data Protection", "Security", "Data Transformation"], 
           "Estimated Percentage Range": ["25-30%", "20-25%", "10-15%", "10-15%", "25-30%"]}
    df = pd.DataFrame(data=debd)
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