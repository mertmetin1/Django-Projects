import requests

# Define the URL for the registration endpoint
url = 'http://localhost:8000/api/register/'

# Define the payload for the registration request
payload = {
    "username": "newusasder1",
    "email": "newu1ser@example.com",
    "password": "passwoasdadrd123",
    "password_confirmation": "passwoasdadrd123",
    "country": "USA",
    "phone_code": "15",
    "phone_number": "5061058792",
    "organization": "NewOrg",
    "bio": "This is a new user."
}

# Make the POST request
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 201:
    print("Registration successful!")
    print("Response:", response.json())
else:
    print("Registration failed!")
    print("Status code:", response.status_code)
    print("Response:", response.json())
