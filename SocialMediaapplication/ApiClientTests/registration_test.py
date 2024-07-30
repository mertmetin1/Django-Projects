import requests



def client2():
    name='merdoaaasdsdasdamedino'
    email ='merdoasdasdameasddino@gmail.com'
    password='Mert008Metin.'


    register_data = {
                "username": name,
                "email": email,
                "password1": password,
                "password2": password
                    }


    response = requests.post(
        url='http://localhost:8000/api/auth/registration/',
        data=register_data)

    #register işleminden sonra token response etmiyor!!!!
    print(" register status code:",response.status_code)

    
    # Login request örneği

    login_data = {
        'username': name,
        'password':password
    }

    response1 = requests.post(
        url= 'http://localhost:8000/api/dj_rest_auth/login/'
        , data=login_data)


    print(" login status code:",response1.status_code)

    response_data=response1.json()
    print(response_data)
    
client2()