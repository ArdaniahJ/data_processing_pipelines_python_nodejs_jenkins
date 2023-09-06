# Malaysian Universities Information Dashboard
Techstack: Python, Pandas, SQLAlchemy, SQL Server MSSQL), PostgreSQL, (__In the soonest future:__ _Node.js, HTML5, Jenkins_)

This project demonstrates a data processing pipeline that involves:
1. ETL (Extract, Transform, Load) using Python
2. performs data analysis calculations
3. designs and interacts with a MSSQL database
4. develops a web portal using Node.js and HTML5.
5. A Jenkins-based CI/CD pipeline will also be used to automate testing and deployment.

ETL stands for Extract, Transform, and Load. ETL is a type of data integration that extracts data from one or more sources (API, DB, or a file), transforms it to match the destination system's requirements, and loads it into the destination system.

## Objective
The primary objective of this project is to __demonstrate how to streamline the ETL process using Python__. The process involves efficiently:
+ extracting data from multiple sources
+ performing necessary transformations
+ loading it into an optimized database/storage layer.

## Key Features
 - [x] Extract data from various sources (APIs, databases, files).
 - [x] Transform and clean the extracted data to match the destination system's requirements.
 - [x] Load the transformed data into an optimized database/storage system.
 - [ ] Perform data analysis calculations on the loaded data.
 - [ ] Design and interact with a MSSQL database.
 - [ ] Develop a web portal using Node.js and HTML5.
 - [ ] Implement a Jenkins-based CI/CD pipeline for automation.

## Prerequisite
1. __Python:__ https://www.python.org/downloads/
2. __Python Libraries:__ Install the necessary Python libraries using `pip`:
   ```
   pip install requests pandas sqlalchemy pyodbc psycopg2
    ```
  - `requests`: For making HTTP requests to extract data from APIs.
  - `pandas`: For data manipulation and transformation.
  - `sqlalchemy`: For database connections and interactions.
  - `pyodbc`: For SQL Server database connections.
  - `psycopg2`: For PostgreSQL database connections.
3. __Database Servers:__
  + Ensure that MSSQL and PostgreSQL are installed and running
4. __API Access:__ To extract data from an API, make sure you have the access of the API and its documentation.
4. ODBC Driver: As a bridge between Python codes and the SQL Server database (specific to the DB system)
