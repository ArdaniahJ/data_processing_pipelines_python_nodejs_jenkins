import extract
import transform
import load

# Extract data
data = extract.extract_data()

# Transform data
transformed_df = transform.transform_data(data)

# Load data into SQL Server
load.load_to_sql_server(transformed_df)

# Load data into PostgreSQL
load.load_to_postgresql(transformed_df)