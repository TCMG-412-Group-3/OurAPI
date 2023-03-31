import requests, unittest, sys, redis


class TestMethods(unittest.TestCase):
    BASE_URL = "http://localhost:4000" 
    
    def test_a_create_keyval_success(self):
        payload = {"storage-key": "new key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        print(json_data)
        self.assertEqual(json_data["key"], payload["storage-key"])
        self.assertEqual(json_data["value"], payload["storage-val"])
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_b_create_keyval_invalid_json(self):
        payload = {"storage-key": "new key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", data=payload) # Sending data instead of JSON
        self.assertEqual(response.status_code, 400)
    
    def test_c_create_keyval_already_exists(self):
        payload = {"storage-key": "new key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 409)
        json_data = response.json()
        self.assertEqual(json_data["key"], payload["storage-key"])
        self.assertEqual(json_data["value"], payload["storage-val"])
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Key already exists")
    
    def test_d_read_keyval_success(self):
        key = "new key"
        response = requests.get(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["key"], key)
        self.assertEqual(json_data["value"], "new value")
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    
    def test_e_read_keyval_key_not_found(self):
        key = "nonexistent key"
        response = requests.get(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 404)
        json_data = response.json()
        self.assertEqual(json_data["key"], key)
        self.assertEqual(json_data["value"], "")
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Key does not exist")
    
    def test_f_update_keyval_success(self):
        payload = {"storage-key": "new key", "storage-val": "new value2"}
        response = requests.put(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["key"], payload["storage-key"])
        self.assertEqual(json_data["value"], payload["storage-val"])
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_g_update_keyval_invalid_json(self):
        payload = {"key": "existing key", "value": "updated value"}
        response = requests.put(f"{self.BASE_URL}/keyval", data=payload) # Sending data instead of JSON
        self.assertEqual(response.status_code, 400)

    def test_h_update_keyval_key_not_found(self):
        payload = {"storage-key": "nonexistent key", "storage-val": "updated value"}
        response = requests.put(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 404)
        json_data = response.json()
        self.assertEqual(json_data["key"], payload["storage-key"])
        self.assertEqual(json_data["value"], payload["storage-val"])
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Key does not exist")
    
    def test_i_delete_keyval_success(self):
        key = "new key"
        response = requests.delete(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["key"], key)
        self.assertEqual(json_data["value"], "new value2")
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_j_delete_keyval_key_not_found(self):
        key = "nonexistent key"
        response = requests.delete(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 404)
        json_data = response.json()
        self.assertEqual(json_data["key"], key)
        self.assertEqual(json_data["value"], "")
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Key does not exist")

    
    

if __name__ == '__main__':
    #specify verbosity to 2 
    unittest.main(verbosity=2)

