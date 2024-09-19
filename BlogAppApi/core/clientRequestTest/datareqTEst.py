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


def get_bloggers():
    token = login('newblogger', 'mert007metin')
    #print(token)
    
    headers={
        'Authorization':f'Token {token}'
    }
    
    response =requests.get(
        
        url='http://127.0.0.1:8000/api/bloggers/',
        headers=headers,
    )
    
    print('status code : ',response.status_code)
    response_data=response.json()
    return response_data

print(get_bloggers())


def get_instance(id):
    token = login('mert24', 'mert007metin')
    headers={
        'Authorization':f'Token {token}'
    }
    
    response =requests.get(
        
        url=f'http://127.0.0.1:8000/api/bloggers/{id}',
        headers=headers,
    )
    
    print('status code : ',response.status_code)
    response_data=response.json()
    return response_data

print(get_instance(1))



