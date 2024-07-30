import requests



def client():
    
    # Login request örneği
    login_url = 'http://localhost:8000/api/rest-auth/login/'
    login_data = {
        'username': 'testuser',
        'password': 'Testing321..'
    }

    response = requests.post(login_url, data=login_data)


    print("status code:",response.status_code)

    response_data=response.json()
    print(response_data)