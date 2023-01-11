# Exam Study Guide
# Last Updated: May 3, 2022

# Import package dependencies
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import random
from PIL import Image
from links.da import links

# Page Layout
st.set_page_config(layout="wide")

# App Code
st.header("SnowPro Advanced: Data Analyst")

# Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Exam Breakdown", "Domains & Objectives", "Study Resources", "Generator", "Randomizer", "Sample Questions"])

# Exam Breakdown
with tab1:
    st.subheader("Exam Breakdown")
    st.markdown("The study guide was last updated on: December 9, 2022")
    abd = {"Domain": ["Data Ingestion and Data Preparation", "Data Transformation and Data Modeling", "Data Analysis", "Data Presentation and Data Visualization"], 
           "Estimated Percentage Range": ["15-20%", "20-25%", "30-35%", "25-30%"]}
    df = pd.DataFrame(data=abd)
    st.table(df)

# Domains & Objectives
with tab2:
    st.subheader("Domains & Objectives")
    with st.container():
        tab7, tab8, tab9, tab10 = st.tabs(["Data Ingestion and Data Preparation", "Data Transformation and Data Modeling", "Data Analysis", "Data Presentation and Data Visualization"])
        st.markdown('''
                    <style>
                    [data-testid="stMarkdownContainer"] ul{
                        padding-left:40px;
                    }
                    </style>
                    ''', unsafe_allow_html=True)

        # Data Ingestion and Data Preparation
        with tab7:
            st.markdown("""
            ##### 1.1 Use a collection system to retrieve data.
            - Assess how often data needs to be collected
            - Identify the volume of data to be collected
            - Identify data sources
            - Retrieve data from a source
            ##### 1.2 Perform data discovery to identify what is needed from the available datasets.
            - Query tables in Snowflake
            - Evaluate which transformations are required
            ##### 1.3 Enrich data by identifying and accessing relevant data from the Snowflake Marketplace.
            - Find external data sets that correlate with available data
            - Use data shares to join data with existing data sets
            - Create tables, views, etc.
            ##### 1.4 Outline and use best practice considerations relating to data integrity structures.
            - Primary keys for tables
            - Perform table joins between parent/child tables
            - Constraints
            ##### 1.5 Implement data processing solutions.
            - Aggregate and enrich data
            - Automate and implement data processing
            - Respond to processing failures
            - Use logging and monitoring solutions
            ##### 1.6 Given a scenario, prepare data and load into Snowflake.
            - Load files
            - Load data from external/internal stages into a Snowflake table
            - Load different types of data
            - Perform general DML (insert, update, delete)
            - Manually add or delete data from a table
            - Identifying and resolving data import errors
            ##### 1.7 Given a scenario, use Snowflake functions.
            - Scalar functions
            - Aggregate functions
            - Window functions
            - Table functions
            - System functions
            """)

        # Data Transformation and Data Modeling
        with tab8:
            st.markdown("""
            ##### 2.1 Prepare different data types into a consumable format.
            - CSV
            - JSON (query and parse)
            - Parquet
            ##### 2.2 Given a dataset, clean the data.
            - Identify and analyze data anomalies
            - Remove corrupted data
            - Remove duplicates
            - Remove nulls
            - Validate data types
            - Use clones as required by specific use-cases
            ##### 2.3 Given a dataset or scenario, work with and query the data.
            - Aggregate and validate the data.
            - Apply analytic functions
            - Perform pre-math calculations (examples, randomization, ranking, grouping, min/max)
            - Perform classifications
            - Perform casting - change data types to ensure data can be presented consistently
            - Enrich the data
            - Use cartesian joins, sub-queries, CTEs, and union queries
            - Work with hierarchical data
            - Use sampling, approximation, and estimation features
            - Perform partition pruning
            - Use Time Travel and cloning features
            - Use different data source formats (for example, structured, semi-structured, etc.)
            - Support native data types
            - Perform SQL operations (for example, grouping, sorting, etc., )
            ##### 2.4 Use data modeling to manipulate the data to meet BI requirements.
            - Use a dimensional model
            - Compare the use of a dimensional model to the use of a flattened data set
            - Use modeling techniques for the consumption layer
            ##### 2.5 Optimize query performance.
            - Use the Query Profile
            - Troubleshoot query performance
            - Use the result, metadata, and warehouse caching
            - Use of different types of tables, objects, and views
            """)

        # Data Analysis
        with tab9:
            st.markdown("""
            ##### 3.1 Use SQL extensibility features.
            - User-Defined Functions (UDFs)
            - Stored Procedures
            - Regular, secured, and materialized views
            ##### 3.2 Perform a descriptive analysis.
            - Summarize large data sets using Snowsight dashboards
            - Perform exploratory ad-hoc analyses
            ##### 3.3 Perform a diagnostic analysis.
            - Find reasons/causes of anomalies or patterns in historical data
            - Collect related data
            - Identify demographics and relationships
            - Analyze statistics and trends
            ##### 3.4 Perform forecasting.
            - Use statistics and built in functions
            - Make predictions based on data
            """)

        # Data Presentation and Data Visualization
        with tab10:
            st.markdown("""
            ##### 4.1 Given a use case, create reports and dashboards to meet business requirements. 
            - Evaluate and select the data for building dashboards 
            - Compare and contrast different chart types (for example, bar charts, scatter plots, heat grids, scorecards) 
            - Connect BI tools to Snowflake 
            - Create charts and dashboards in Snowsight 
            ##### 4.2 Given a use case, maintain reports and dashboards to meet business requirements. 
            - Build automated and repeatable tasks 
            - Operationalize data 
            - Store and update data 
            - Manage and share Snowsight dashboards 
            - Sorting and filtering 
            - Use and naming of tiles 
            - Configure subscriptions and updates 
            ##### 4.3 Given a use case, incorporate visualizations for dashboards and reports. 
            - Present data for business use analyses 
            - Identify patterns and trends 
            - Identify correlations among variables 
            - Customize data presentations using filtering and editing techniques
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
            for i in links:
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
    **Q1: A retail company needs to run a marketing campaign targeting customers in specific sales regions.
    A Data Analyst needs to support this campaign using the necessary data in Snowflake.
    How can the Analyst meet this requirement?**
    - A. Use Snowsight to load the region table (region_id, name, comment).
    - B. Use Snowsight to load the customer table (id, name, address, region_id, phone_number).
    - C. Use the COPY command to load the region table (region_id, name, comment).
    - D. Use the COPY command to load the customer table (id, name, address, region_id, phone_number).
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
    **Q2: The following JSON object is stored in a VARIANT column called src in a table called car_sales:**
    ```
    {"vehicle" : [
    {"make": "Honda", "model": "Civic", "year": "2019",
    "price": "20275", "extras":["ext warranty", "paint
    protection"]},
    {"make": "Toyota", "model": "Camry", "year": "2021",
    "price": "28375", "extras":["ext warranty", "paint
    protection", "rust proofing"]}
    ]}
    ```
    Which query would return the following result?
    | Make       | Model      | Extras            |
    | ---------- | ---------- | ----------------- |
    | Honda      | Civic      | ext warranty      |
    | Honda      | Civic      | paint protection  |
    | Toyota     | Camry      | ext warranty      |
    | Toyota     | Camry      | paint protection  |
    | Toyota     | Camry      | rust proofing     |

    - A. 
    ``` 
    SELECT
        src:vehicle.make::string AS make,
        src:vehicle.model::string AS model,
        src:vehicle.extras::string AS extras
    FROM car_sales
    ORDER BY make, model, extras;
    ```
    - B. 
    ``` 
    SELECT
        vm.value:make::string AS make,
        vm.value:model::string AS model,
        ve.value::string AS extras
    FROM car_sales
        ,lateral flatten(input => src:vehicle) AS vm
        ,lateral flatten(input => vm.value:extras) AS ve
    ORDER BY make, model, extras;
    ```
    - C. 
    ```
    SELECT
        vm.value:make::string AS make,
        vm.value:model::string AS model,
        vm.value:extras::string AS extras
    FROM car_sales
        ,lateral flatten(input => src:vehicle) AS vm
    ORDER BY make, model, extras;
    ```
    - D. 
    ``` 
    SELECT
        src:vehicle.make::string AS make,
        src:vehicle.model::string AS model,
        vm.value::string AS extras
    FROM car_sales
        ,lateral flatten(input => src:vehicle.extras) AS vm
    ORDER BY make, model, extras;
    ```
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
    **Q3: A Data Analyst created a schema named PUBLIC. This schema contains two permanent tables as shown below:**
    ```
    CREATE TABLE TABLE1 (NAME VARCHAR)
    DATA_RETENTION_TIME_IN_DAYS = 10;

    CREATE TABLE TABLE2 (NAME VARCHAR);
    ```
    The following command is run:
    ```
    ALTER SCHEMA PUBLIC SET DATA_RETENTION_TIME_IN_DAYS = 15;
    ```
    What will be the result of running this command?

    - A. The attempt to set the data retention limit at the schema level will cause the statement to fail.
    - B. The retention time on TABLE1 does not change. The retention time on TABLE2 will be set to 15 days.
    - C. The retention time on both tables will be set to 15 days.
    - D. The retention time will be unchanged for both tables.
    """)
    q3 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=2)
    if q3 == "B":
        st.write("✅ That's correct!")
    elif q3 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q4
    q4_text = st.markdown("""
    **Q4: A Data Analyst has a sequence of numeric values that could represent some quantity or amount of values. The Analyst tries to label the values using ranking windows functions as shown below:**
    """)
    
    sql_query_result_grid = Image.open("./img/sql_query_result_grid.PNG")
    st.image(sql_query_result_grid, output_format="PNG")

    q4_text2 = st.markdown("""
    What are the hidden values (as indicated by the green circles) in the SQL query result grid? (Select TWO).
    
    - A. 2 for the hidden NTILE cell
    - B. 3 for the hidden RANK cell
    - C. 4 for the hidden RANK cell
    - D. 3 for the hidden DENSE_RANK cell
    - E. 1 for the hidden NTILE cell
    """)
    q4 = st.selectbox("Answer(s):", ("", "A & B", "A & C", "A & D", "A & E", "B & C", "B & D", "B & E", "C & D", "C & E", "D & E"), key=3)
    if q4 == "C & E":
        st.write("✅ That's correct!")
    elif q4 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")

    # Q5
    q5_text = st.markdown("""
    **Q5: A Data Analyst has been asked to produce a tile in a dashboard using Snowsight.
    The chart should always show orders for the last 30 days excluding partial days based on the order_date field.
    Which notation will meet this requirement?**
    """)
    q5 = st.selectbox("Answer:", ("", "A", "B", "C", "D"), key=4)
    if q5 == "D":
        st.write("✅ That's correct!")
    elif q5 == "":
        st.write("Please input your answer above.")
    else:
        st.write("❌ That's incorrect. Please try again.")