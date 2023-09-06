from sqlalchemy import create_engine
import pyodbc
import psycopg2

def load_to_sql_server(transformed_df):
    # Configure your SQL Server connection string (Windows Authentication)
    conn_str = 'DSN=dania;DATABASE=Malaysia;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)  # Create a connection object
    # Use the connection object to create the SQLAlchemy engine
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={conn_str}")
    
    table_name = "UniversitiesInMY"
    # Load the DataFrame into 'UniversitiesInMY'
    transformed_df.to_sql(table_name, engine, if_exists='replace', index=False)

    # Close the connection when done
    conn.close()

    return transformed_df


def load_to_postgresql(transformed_df):
    # Configure your PostgreSQL connection string
    conn_str = "postgresql://diana:12345@localhost:5432/Malaysia"
    engine = create_engine(conn_str)
    table_name = "UniversitiesInMY"
    transformed_df.to_sql(table_name, engine, if_exists='replace', index=False)

    return transformed_df

 
