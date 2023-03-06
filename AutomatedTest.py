#Automated Testing Suite for API
import requests
import unittest

class TestAPI(unittest.TestCase): # idk if these will be useful
    base_url = "http://localhost:4000" 
    
    def test_endpoint_1(self):
        url = self.base_url + "/endpoint1"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        # add more tests for this endpoint
    
    def test_endpoint_2(self):
        url = self.base_url + "/endpoint2"
        response = requests.post(url, data={"param1": "value1", "param2": "value2"})
        self.assertEqual(response.status_code, 200)
        # add more tests for this endpoint
    
    def test_endpoint_3(self):
        url = self.base_url + "/endpoint3"
        response = requests.get(url, params={"param1": "value1"})
        self.assertEqual(response.status_code, 200)
        # add more tests for this endpoint
        
    # add more tests for other endpoints
    
if __name__ == '__main__':
    unittest.main()
###########################################################
############# END OF ENDPOINT TEST ###########################
###########################################################


# Now here is a test we could do for factorials 
def test_factorial():
    app.testing = True
    client = app.test_client()
    
    # Test for empty input
    response = client.get('/factorial/')
    assert response.status_code == 404
    expected_output = {"input": "", "output": "No input detected. Please input a string to be hashed"}
    assert response.get_json() == expected_output
    
    # Test for non-integer input
    response = client.get('/factorial/abc')
    assert response.status_code == 400
    expected_output = {"input": "abc", "output": "Input is not a valid integer. Please input a valid integer"}
    assert response.get_json() == expected_output
    
    # Test for negative input
    response = client.get('/factorial/-1')
    assert response.status_code == 400
    expected_output = {"input": "-1", "output": "Input is a negative number. Please input a positive integer"}
    assert response.get_json() == expected_output
    
    # Test for zero input
    response = client.get('/factorial/0')
    assert response.status_code == 200
    expected_output = {"input": 0, "output": 1}
    assert response.get_json() == expected_output
    
    # Test for positive input
    response = client.get('/factorial/5')
    assert response.status_code == 200
    expected_output = {"input": 5, "output": 120}
    assert response.get_json() == expected_output
