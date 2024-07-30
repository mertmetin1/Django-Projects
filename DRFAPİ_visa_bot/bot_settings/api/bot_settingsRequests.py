import json
import requests

class BotSettingsAPI:
    def __init__(self, base_url='http://localhost:8000/api/bot_settings/'):
        self.base_url = base_url
        self.headers = {'Content-Type': 'application/json'}

    def get_bot_settings(self):
        url = self.base_url 
        response = requests.get(url)
        return response.json()

    def get_bot_setting(self, id):
        url = self.base_url + str(id) 
        response = requests.get(url)
        return response.json()
   
    def create_bot_setting(self, data):
        url = self.base_url 
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json, headers=self.headers)
        return response.json()
    
    def update_bot_setting(self, id, data):
        url = self.base_url + str(id)
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json, headers=self.headers)
        return response.json()
    
    def patch_bot_setting(self, id, data):
        url = self.base_url + str(id) 
        data_json = json.dumps(data)
        response = requests.patch(url, data=data_json, headers=self.headers)
        return response.json()

    def delete_bot_setting(self, id):
        url = self.base_url + str(id) 
        response = requests.delete(url, headers=self.headers)
        return response.status_code    

# Example usage
if __name__ == '__main__':
    bot_settings_api = BotSettingsAPI()

    # Test GET all bot_settings
    print("GET all bot_settings:")
    bot_settings = bot_settings_api.get_bot_settings()
    print(bot_settings)
    print()

    # Test GET bot_setting with id 30
    print("GET bot_setting with id 30:")
    bot_setting_2 = bot_settings_api.get_bot_setting(30)
    print(bot_setting_2)
    print()

    # Test CREATE multiple bot_settings
    print("Creating multiple bot_settings:")
    for i in range(10):
        data = {
        'isRunning': True, 
        'CheckFrequency': 33, 
        'CheckToDate': 92
        }
        created_bot_setting = bot_settings_api.create_bot_setting(data)
        print("Created bot_setting:")
        print(created_bot_setting)
        print()

    # Test UPDATE bot_setting with id 30
    print("Updating bot_setting with id 30:")
    updated_data = {
    
        'isRunning': True, 
        'CheckFrequency': 33, 
        'CheckToDate': 92
    }
    updated_bot_setting = bot_settings_api.update_bot_setting(30, updated_data)
    print("Updated bot_setting:")
    print(updated_bot_setting)
    print()

    # Test PATCH bot_setting with id 30
    print("Patching bot_setting with id 30:")
    patch_data = {  'isRunning': False}
    patched_bot_setting = bot_settings_api.patch_bot_setting(30, patch_data)
    print("Patched bot_setting:")
    print(patched_bot_setting)
    print()

    # Test GET bot_setting with id 30
    print("GET bot_setting with id 30:")
    bot_setting_6 = bot_settings_api.get_bot_setting(30)
    print(bot_setting_6)
    print()

    # Test DELETE bot_setting with id 30
    print("Deleting bot_setting with id 30:")
    delete_status = bot_settings_api.delete_bot_setting(30)
    print("Deleted bot_setting status code:", delete_status)
    print()

    # Re-fetch bot_settings to see if delete was successful
    print("GET all bot_settings after deletion:")
    bot_settings_after_deletion = bot_settings_api.get_bot_settings()
    print(bot_settings_after_deletion)
    print()
