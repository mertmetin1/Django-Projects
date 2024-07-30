import requests



def client2():
    # Login request örneği
    login_url = 'http://localhost:8000/api/kullanici-profilleri/'

    token = 'Token aa8007abff300094be6b3aba95d66dd8bb89af6a'


    headers={
        'Authorization':token,
        
    }

    response = requests.get(
        url=login_url,
        headers=headers                            )


    print("status code:",response.status_code)

    response_data=response.json()
    print(response_data)
    
    
    
client2()