import requests

def login(username, password):
    login_url = 'http://localhost:8000/api/rest-auth/login/'
    credentials={
        
        'username':'mert',
        'password':'mert'
    }
    
    response = requests.post(login_url, data=credentials)
    print("Login response status code:", response.status_code)
    print("Login response body:", response.text)

    if response.status_code == 200:
        response_data = response.json()
        key = response_data.get('key')
        return key
    else:
        print("Login failed:", response.text)
        return None
    
    
login('mert','mert')