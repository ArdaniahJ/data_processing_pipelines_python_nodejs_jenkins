import pandas as pd

def transform_data(data):
    df = pd.DataFrame(data)
    print(df.columns)
    transformed_df = df[["name", "state-province", "domains", "web_pages"]]
    return transformed_df
 
