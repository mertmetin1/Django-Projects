import json
import requests

class requestAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def get_items(self, endpoint):
        url = f"{self.base_url}/{endpoint}/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching items from {endpoint}: {e}")
            return None

    def get_item(self, endpoint, id):
        url = f"{self.base_url}/{endpoint}/{id}/"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching item {id} from {endpoint}: {e}")
            return None

    def create_item(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}/"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating item in {endpoint}: {e}")
            return None
    
    def update_item(self, endpoint, id, data):
        url = f"{self.base_url}/{endpoint}/{id}/"
        try:
            response = requests.put(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating item {id} in {endpoint}: {e}")
            return None
    
    def patch_item(self, endpoint, id, data):
        url = f"{self.base_url}/{endpoint}/{id}/"
        try:
            response = requests.patch(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error patching item {id} in {endpoint}: {e}")
            return None

    def delete_item(self, endpoint, id):
        url = f"{self.base_url}/{endpoint}/{id}/"
        try:
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error deleting item {id} in {endpoint}: {e}")
            return None

if __name__ == '__main__':
    # Örnek bir uygulama için API sınıfı oluşturulması
    api = requestAPI(base_url='http://localhost:8000/api')

    # Örnek 1: User endpoint'i için örnek kullanımlar
    print("User API:")
    # Tüm kullanıcıları almak
    print("GET all users:")
    users = api.get_items('user')
    print("Users:", users)
    print()

    # Belirli bir kullanıcıyı almak (id=1)
    print("GET user with id 1:")
    user = api.get_item('user', 1)
    print("User:", user)
    print()

    # Yeni bir kullanıcı oluşturmak
    print("Creating a new user:")
    new_user_data = {
                     
            'name': 'new mert ',
            'surname': 'new metin',
            'email': 'erdmle@gmail.com',
            'username': ' new mert',
            'password': 'new mert',
            'isAdmin': True
            
                     }
    created_user = api.create_item('user', new_user_data)
    print("Created user:", created_user)
    print()

    # Bir kullanıcıyı güncelleme (id=1)
    print("Updating user with id 1:")
    update_data = {'email': 'updated_email@example.com'}
    updated_user = api.update_item('user', 1, update_data)
    print("Updated user:", updated_user)
    print()

    # Bir kullanıcıyı silme (id=1)
    print("Deleting user with id 1:")
    delete_status = api.delete_item('user', 1)
    print("Delete status code:", delete_status)
    print()

    # Örnek 2: Client endpoint'i için örnek kullanımlar
    print("Client API:")
    # Tüm client'ları almak
    print("GET all clients:")
    clients = api.get_items('client')
    print("Clients:", clients)
    print()

    # Örnek 3: Bot Settings endpoint'i için örnek kullanımlar
    print("Bot Settings API:")
    # Tüm bot ayarlarını almak
    print("GET all bot settings:")
    bot_settings = api.get_items('bot_settings')
    print("Bot Settings:", bot_settings)
    print()
