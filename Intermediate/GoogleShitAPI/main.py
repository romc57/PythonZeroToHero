import requests
import json

APP_ID = 'b67516f0'
API_KEY = 'e2855ed5f2b72cd443c7fb40c3efcd90'

def get_nutrition_info(query):
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0",  # 0 for development
        "Content-Type": "application/json"
    }
    
    data = {
        "query": query
    }
    
    try:
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

# Example usage
if __name__ == "__main__":
    result = get_nutrition_info("ran 5 kilometer and did 5 pushups")
    if result:
        print(json.dumps(result, indent=2)) 