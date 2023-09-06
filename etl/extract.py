import requests

def extract_data():
    API_URL = "http://universities.hipolabs.com/search?country=Malaysia"
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"API request failed with status code: {response.status_code}")
            data = None
    
    except Exception as e:
        print(f"An error occured during data extraction: {str(e)}")
        data = None
    
    return data
