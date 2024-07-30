import json
import requests




class UserAPI:
    def __init__(self, base_url='http://localhost:8000/api/user/'):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def get_users(self):
        url = self.base_url 
        response = requests.get(url)
        return response.json()

    def get_user(self,id):
        url =self.base_url +str(id)
        response =requests.get(url)
        return response.json()
   
   
    def create_user(self,data):
        url = self.base_url 
        data_json = json.dumps(data)
        print(data_json)
        response =requests.post(url,data=data_json,headers=self.headers)
        return response.json()
    
    def update_user(self,id,data):
        url =self.base_url + str(id)
        data_json = json.dumps(data)
        response = requests.put(url,data=data_json,headers=self.headers)
        return response.json()
    
    
    def patch_user(self,id,data):
        url =self.base_url +str(id)
        data_json = json.dumps(data)
        response = requests.patch(url,data=data_json,headers=self.headers)
        return response.json()
    

    def delete_user(self, id):
        url = self.base_url +str(id)
        response = requests.delete(url, headers=self.headers)
        return response.status_code    
    
    
"""
# Example usage
if __name__ == '__main__':
    user_api = UserAPI()

    # Test GET all User
    print("GET all User:")
    User= user_api.get_users()
    print(User)
    print()
    print("get user with id 2")
    User2=user_api.get_user(30)
    print(User2)
    print()

    for i in range(10):
        data={
            

            'name': 'new mert '+str(i),
            'surname': 'new metin'+str(i),
            'email': 'erdmle@gmail.com',
            'username': ' new mert'+str(i),
            'password': 'new mert'+str(i),
            'isAdmin': True
            
            }
        created_User=user_api.create_user(data)
        print("created User")
        print(created_User)

    
    print()
    updated_User=user_api.update_user(30,data)
    print("updated User")
    print(updated_User)
    

    
    patch_data = {'isAdmin': False}
    patched_User = user_api.patch_user(6, patch_data)
    print("Patched User")
    print(patched_User)  # Corrected to print patched_User
    print()
    
    User6=user_api.get_user(6)
    print(User6)
    print()
    
    delete_status = user_api.delete_user(6)
    print("Deleted User status code:", delete_status)
    print()

    # Re-fetch Users to see if delete was successful
    Users = user_api.get_users()
    print("GET all Users after deletion:")
    print(Users)
    print()


"""