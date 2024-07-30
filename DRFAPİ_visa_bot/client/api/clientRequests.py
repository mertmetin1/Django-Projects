import json
import requests




class ClientAPI:
    def __init__(self, base_url='http://localhost:8000/api/'):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def get_clients(self):
        url = self.base_url + 'client/'
        response = requests.get(url)
        return response.json()

    def get_client(self,id):
        url =self.base_url +'client/'+ str(id)
        response =requests.get(url)
        return response.json()
   
   
    def create_client(self,data):
        url = self.base_url + 'client/'
        data_json = json.dumps(data)
        print(data_json)
        response =requests.post(url,data=data_json,headers=self.headers)
        return response.json()
    
    def update_client(self,id,data):
        url =self.base_url +'client/' + str(id)
        data_json = json.dumps(data)
        response = requests.put(url,data=data_json,headers=self.headers)
        return response.json()
    
    
    def patch_client(self,id,data):
        url =self.base_url +'client/' + str(id)
        data_json = json.dumps(data)
        response = requests.patch(url,data=data_json,headers=self.headers)
        return response.json()
    

    def delete_client(self, id):
        url = self.base_url + 'client/' + str(id)
        response = requests.delete(url, headers=self.headers)
        return response.status_code    
    
    
"""
# Example usage
if __name__ == '__main__':
    client_api = ClientAPI()

    # Test GET all clients
    print("GET all clients:")
    clients= client_api.get_clients()
    print(clients)
    print()
    client8=client_api.get_client(2)
    print(client8)
    print()
    data={
        
    "name": "aaaaaaaaaaaaaNew Client",
    "surname": "Surname",
    "email": "newclient@example.com",
    "password": "password",
    "location": "Location",
    "isActive": False,
    "visa": False,
    "priority": 99
        
    }
    created_client=client_api.create_client(data)
    print("created client")
    print(created_client)
    
    print()
    updated_client=client_api.update_client(6,data)
    print("updated client")
    print(updated_client)
    

    
    patch_data = {"isActive": True}
    patched_client = client_api.patch_client(6, patch_data)
    print("Patched client")
    print(patched_client)  # Corrected to print patched_client
    print()
    
    client6=client_api.get_client(6)
    print(client6)
    print()
    
    delete_status = client_api.delete_client(2)
    print("Deleted client status code:", delete_status)
    print()

    # Re-fetch clients to see if delete was successful
    clients = client_api.get_clients()
    print("GET all clients after deletion:")
    print(clients)
    print()
    
    """