import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://localhost:8000" 
    
    def test_create_keyval_success(self):
        payload = {"storage-key": "new key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["storage-key"], payload["storage-key"])
        self.assertEqual(json_data["storage-val"], payload["storage-val"])
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_create_keyval_invalid_json(self):
        payload = {"storage-key": "new key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", data=payload) # Sending data instead of JSON
        self.assertEqual(response.status_code, 400)
    
    def test_create_keyval_already_exists(self):
        payload = {"storage-key": "existing key", "storage-val": "new value"}
        response = requests.post(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 409)
        json_data = response.json()
        self.assertEqual(json_data["storage-key"], payload["storage-key"])
        self.assertEqual(json_data["storage-val"], payload["storage-val"])
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Unable to add pair: key already exists.")
    
    def test_read_keyval_success(self):
        key = "existing key"
        response = requests.get(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["storage-key"], key)
        self.assertEqual(json_data["storage-val"], "new value")
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_read_keyval_invalid_json(self):
        key = "existing key"
        response = requests.get(f"{self.BASE_URL}/keyval/{key}", data=key) # Sending data instead of JSON
        self.assertEqual(response.status_code, 400)
    
    def test_read_keyval_key_not_found(self):
        key = "nonexistent key"
        response = requests.get(f"{self.BASE_URL}/keyval/{key}")
        self.assertEqual(response.status_code, 404)
        json_data = response.json()
        self.assertEqual(json_data["storage-key"], key)
        self.assertEqual(json_data["storage-val"], "")
        self.assertEqual(json_data["result"], False)
        self.assertEqual(json_data["error"], "Key does not exist.")
    
    def test_update_keyval_success(self):
        payload = {"storage-key": "existing key", "storage-val": "updated value"}
        response = requests.put(f"{self.BASE_URL}/keyval", json=payload)
        self.assertEqual(response.status_code, 200)
        json_data = response.json()
        self.assertEqual(json_data["storage-key"], payload["storage-key"])
        self.assertEqual(json_data["storage-val"], payload["storage-val"])
        self.assertEqual(json_data["result"], True)
        self.assertEqual(json_data["error"], "")
    
    def test_update_keyval_invalid_json(self):
        payload = {"storage-key": "existing key", "storage-val": "updated value"}
        response = requests.put(f"{self.BASE_URL}/keyval", data=payload) # Sending data instead of JSON
        self.assertEqual(response.status_code, 400
