import requests

url = 'http://localhost:8000/api/auth/registration/'

data = {
    "username": "newblogger",
    "password1": "mert007metin",
    "password2": "mert007metin",
    "email": "merasd2t2@gmail.com"
}

response = requests.post(url, json=data)

print(f'Status Code: {response.status_code}')

#response edilen bişey yok o yüzden sadece status code çekilebilir