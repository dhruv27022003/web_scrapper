import requests

def make_api_call(url, method, headers=None, params=None, data=None):
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data)
        response.raise_for_status()  
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None



api_url = "https://api.example.com/data"
api_method = "GET"
api_headers = {
    "Authorization": "Bearer your_access_token",
    "User-Agent": "YourApp/1.0"
}
api_params = {
    "param1": "value1",
    "param2": "value2"
}


response_data = make_api_call(api_url, api_method, headers=api_headers, params=api_params)

if response_data:
    print("API response:", response_data)
else:
    print("API call failed.")
