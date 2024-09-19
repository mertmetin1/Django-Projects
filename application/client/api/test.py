import requests

def login_as_admin(admin_username, admin_password):
    # URL for the admin login endpoint
    admin_login_url = 'http://127.0.0.1:8000/api/client/login/'

    # Admin user credentials
    admin_credentials = {
        'username': admin_username,
        'password': admin_password
    }

    # Perform login to get the token
    login_response = requests.post(admin_login_url, data=admin_credentials)
    if login_response.status_code == 200:
        token = login_response.json().get('token')
        return token
    else:
        print("Failed to login as admin")
        print(login_response.json())
        return None

def get_clients(token):
    # URL for the clients endpoint
    clients_url = 'http://127.0.0.1:8000/api/clients/'

    # Headers with the token
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }

    # Perform the GET request to retrieve the list of clients
    get_response = requests.get(clients_url, headers=headers)
    
    # Check the response status code
    if get_response.status_code == 200:
        clients = get_response.json()
        return clients
    else:
        print("Failed to retrieve clients")
        print(get_response.json())
        return None

# Replace with your admin credentials
admin_username = 'mert'  # Replace with your admin username
admin_password = 'mert'  # Replace with your admin password

# Get the admin token
token = login_as_admin(admin_username, admin_password)

# If the token is retrieved successfully, get the clients
if token:
    clients = get_clients(token)
    if clients:
        print("List of clients:")
        print(clients)


# import requests

# # URL for the clients endpoint
# clients_url = 'http://127.0.0.1:8000/api/clients/'

# # Perform the GET request to retrieve the list of clients
# get_response = requests.get(clients_url)

# # Check the response status code
# if get_response.status_code == 200:
#     clients = get_response.json()
#     print("List of clients:")
#     print(clients)
# else:
#     print("Failed to retrieve clients")
#     print(get_response.json())
