import requests

# URL for the admin login endpoint
admin_login_url = 'http://127.0.0.1:8000/api/client/login/'

# Admin user credentials
admin_credentials = {
    'username': 'mertmetinmert',  # Replace with your admin username
    'password': 'mert007metin'   # Replace with your admin password
}

# Perform login to get the token
login_response = requests.post(admin_login_url, data=admin_credentials)

if login_response.status_code == 200:
    token = login_response.json().get('token')
    print(f" token: {token}")
else:
    print("Failed to login")
    print(login_response.json())
    exit()

# import requests

# # API endpoint
# url = "http://127.0.0.1:8000/api/clients/13/"

# # Headers
# headers = {
#     "Authorization": f"Token {token}",
#     "Content-Type": "application/json"
# }

# # Data to update
# data = {
    
#     "username": "measdarasdomedo",
#     "email": "newemaasdil@example.com",
#     "country": "NewCountry",
#     "bio": "This is the updated bio.",
#     "organization": "New Organization",
#     "phone_code": "+1",
#     "phone_number": "1234567890"
# }

# # Sending the PUT request to update the client
# response = requests.put(url, headers=headers, json=data)

# # Check the response
# if response.status_code == 200:
#     print("Client updated successfully:", response.json())
# else:
#     print("Failed to update client:", response.status_code, response.text)



# # API endpoint for the client to be deleted
# client_id = 5 # Replace with the actual client ID you want to delete
# url = f"http://127.0.0.1:8000/api/clients/{client_id}/"

# # Headers
# headers = {
#     "Authorization": f"Token {token}",
#     "Content-Type": "application/json"
# }

# # Sending the DELETE request to remove the client
# response = requests.delete(url, headers=headers)

# # Check the response
# if response.status_code == 204:
#     print("Client deleted successfully")
# else:
#     print(f"Failed to delete client: {response.status_code}")




# # API endpoint for creating a new client
# url = "http://127.0.0.1:8000/api/clients/"

# # Headers
# headers = {
#     "Authorization": f"Token {token}",
#     "Content-Type": "application/json"
# }

# # Data for the new client
# data = {
#     "username": "newusasdasder",
#     'password': 'mert007metin' ,
#     "first_name": "apsdpaskdp",
#     "last_name": "poaspdasdk",
#     "email": "newuasdasdser@example.com",
#     "country": "NewCountry",
#     "bio": "This is the bio of the new user.",
#     "organization": "New Organization",
#     "phone_code": "+1",
#     "phone_number": "1234567890"
# }

# # Sending the POST request to create a new client
# response = requests.post(url, headers=headers, json=data)

# # Check the response
# if response.status_code == 201:
#     print("Client created successfully:", response.json())
# else:
#     print(f"Failed to create client: {response.status_code}")
#     print(response.text)