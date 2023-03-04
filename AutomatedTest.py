#Automated Testing Suite for API
import requests, sys

base_url = 'http://localhost:4000'

#test banks
is_prime_bank = ['2', '8', '3912390210', '37', 'three']
is_prime_expected = [True, False, False, True, 'Input is not a valid integer. Please input a valid integer'] #status code is returned as integer
#make more test value lists

test_outcomes = []

def test_func (uri_to_test, value):
    response = requests.get(base_url+'/'+uri_to_test+"/"+value).json()
    output = response['output']
    print ('Testing /'+uri_to_test+"/"+value,"... Output:",output)
    return output

#testing is-prime
for i in is_prime_bank:
    result = test_func ('is-prime', i)
    if result == is_prime_expected[is_prime_bank.index(i)]:
        print ("pass")
        test_outcomes.append('pass')
    else:
        print ("fail")
        test_outcomes.append('fail')
        
print (test_outcomes)
exit_code = all(i == 'pass' for i in test_outcomes) #still need to figure out how to return Unix 0, will test on linux vm
if exit_code == True:
    sys.exit(0) 
