import requests, unittest, sys, redis

base_url = 'http://34.135.137.212:4000'

#test value bank and expected lists

md5_bank = ['hello world', '219jjk21n312', '%20%20%wahwgahwahaw', None]
md5_expected = ['5eb63bbbe01eeed093cb22bb8f5acdc3', 'f74e179c00bae8bf831335e2ea719934', '59ef20692ba6601dbb42950ac0b26779', 'No input detected. Please input a string to be hashed']

fact_bank = ['0','4','10','hello', ' ', None, '-4']
fact_expected = [1,24,3628800,'Input is not a valid integer. Please input a valid integer','Input is not a valid integer. Please input a valid integer', 'No input detected. Please input a number to be factorialized', 'Input is a negative number. Please input a positive integer']

fibo_bank = ['21','35','hello', ' ', None, '-4', '1', '0']
fibo_expected = [[0, 1, 1, 2, 3, 5, 8, 13, 21],[0, 1, 1, 2, 3, 5, 8, 13, 21, 34],'Input is not a valid integer. Please input a valid integer', 'Input is not a valid integer. Please input a valid integer', 'Please input a positive integer', 'Input is a negative number. Please input a positive integer', [0,1,1], [0]]

is_prime_bank = ['2', '8', '3912390210', '37', 'three', ' ', None, '-4']
is_prime_expected = [True, False, False, True, 'Input is not a valid integer. Please input a valid integer','Input is not a valid integer. Please input a valid integer', 'Please input a valid positive integer', 'Input is a negative number. Please input a positive integer'] #status code is returned as integer

slack_bank = ['Hello', 'Testing', '83']
slack_expected = [True, True, True]

#make more test value lists

def test_func (uri_to_test, value): #use this to test and retrieve json output
    if value == None:
        response = requests.get(base_url+'/'+uri_to_test).json()
        output = response['output']
        print ('Testing /'+uri_to_test+"/","... Output:",output)
    else:
        response = requests.get(base_url+'/'+uri_to_test+"/"+value).json()
        output = response['output']
        print ('Testing /'+uri_to_test+"/"+value,"... Output:",output)
    return output

class TestMethods(unittest.TestCase):
    def test_md5(self):
        for i in md5_bank:
            self.assertEqual(test_func('md5', i),md5_expected[md5_bank.index(i)]) 
    def test_fact(self):
        for i in fact_bank:
            self.assertEqual(test_func('factorial', i),fact_expected[fact_bank.index(i)])
    def test_fibo(self):
        for i in fibo_bank:
            self.assertEqual(test_func('fibonacci', i),fibo_expected[fibo_bank.index(i)])            
    def test_is_prime(self):
        for i in is_prime_bank: #can manually add test values using self.assertEqual(URI, expected value) outsdide of the loop
            self.assertEqual(test_func('is-prime', i),is_prime_expected[is_prime_bank.index(i)])
        #self.assertEqual(requests.get(base_url+'/is-prime/72').json()['output'],True,'Failed') <-- example
    def test_slack(self):
        for i in slack_bank:
            self.assertEqual(test_func('slack-alert',i),slack_expected[slack_bank.index(i)])
    
if __name__ == '__main__':
    unittest.main()
