import http
import requests
import json
import pytest


## defined functions to process http requests   
def postRequest(key,val):
    r = requests.post('http://localhost:5000/keyval', json = {"key":key,"value":val})
    return r.text, r.status_code
def putRequest(key,val):
    r = requests.put('http://localhost:5000/keyval', json = {"key":key,"value":val})
    return r.text, r.status_code
def getRequest(key):
    r = requests.get('http://localhost:5000/keyval/'+key)
    text = r.text
    return text, r.status_code
def deleteRequest(key):
    r = requests.delete('http://localhost:5000/keyval/'+key)
    return r.text, r.status_code



class TestClass:
    base_json = {
        "input": "foo",
        "output": "foo1"
    }
    md5_tester = {
        "test": "098f6bcd4621d373cade4e832627b4f6",
        "testytesty": "18941a6bbd113c75cac218d2d3346fc6",
        "tester": "f5d1278e8109edd94e1e4197e04873b9"
    }
    factorial_tester = {
     1: 1,
     2: 2,
     6: 720,
     7: 5040,
     10: 3628800 
    }
    fibonacci_tester = {
        56: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
        18: [0, 1, 1, 2, 3, 5, 8, 13],
        10: [0, 1, 1, 2, 3, 5, 8]
    }

    prime_tester = {
        2:True,
        3:True,
        5:True,
        73:True,
        1:False,
        149:True,
        "test":False
    }
   
    ##md5 tests
    def test_md5_test(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[0]
        base_json["output"] = list(TestClass.md5_tester.values())[0]
        r = requests.get('http://localhost:5000/md5/'+str(list(TestClass.md5_tester.keys())[0]))
        assert base_json == json.loads(r.text)
    def test_md5_testytesty(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[1]
        base_json["output"] = list(TestClass.md5_tester.values())[1]
        r = requests.get('http://localhost:5000/md5/'+str(list(TestClass.md5_tester.keys())[1]))
        assert base_json == json.loads(r.text)
    def test_md5_tester(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[2]
        base_json["output"] = list(TestClass.md5_tester.values())[2]
        r = requests.get('http://localhost:5000/md5/'+str(list(TestClass.md5_tester.keys())[2]))
        assert base_json == json.loads(r.text)

    ##factorial testers
    def test_factorial_1(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.factorial_tester.keys())[0]
        base_json["output"] = list(TestClass.factorial_tester.values())[0]
        r = requests.get('http://localhost:5000/factorial/'+str(list(TestClass.factorial_tester.keys())[0]))
        assert base_json == json.loads(r.text)
    def test_factorial_2(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.factorial_tester.keys())[1]
        base_json["output"] = list(TestClass.factorial_tester.values())[1]
        r = requests.get('http://localhost:5000/factorial/'+str(list(TestClass.factorial_tester.keys())[1]))
        assert base_json == json.loads(r.text)
    def test_factorial_6(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.factorial_tester.keys())[2]
        base_json["output"] = list(TestClass.factorial_tester.values())[2]
        r = requests.get('http://localhost:5000/factorial/'+str(list(TestClass.factorial_tester.keys())[2]))
        assert base_json == json.loads(r.text)
    def test_factorial_7(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.factorial_tester.keys())[3]
        base_json["output"] = list(TestClass.factorial_tester.values())[3]
        r = requests.get('http://localhost:5000/factorial/'+str(list(TestClass.factorial_tester.keys())[3]))
        assert base_json == json.loads(r.text)
    def test_factorial_6(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.factorial_tester.keys())[4]
        base_json["output"] = list(TestClass.factorial_tester.values())[4]
        r = requests.get('http://localhost:5000/factorial/'+str(list(TestClass.factorial_tester.keys())[4]))
        assert base_json == json.loads(r.text)


    ##fibonacci testers
    def test_fibonacci_56(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.fibonacci_tester.keys())[0]
        base_json["output"] = list(TestClass.fibonacci_tester.values())[0]
        r = requests.get('http://localhost:5000/fibonacci/'+str(list(TestClass.fibonacci_tester.keys())[0]))
        assert base_json == json.loads(r.text)
    def test_fibonacci_18(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.fibonacci_tester.keys())[1]
        base_json["output"] = list(TestClass.fibonacci_tester.values())[1]
        r = requests.get('http://localhost:5000/fibonacci/'+str(list(TestClass.fibonacci_tester.keys())[1]))
        assert base_json == json.loads(r.text)
    def test_fibonacci_10(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.fibonacci_tester.keys())[0]
        base_json["output"] = list(TestClass.fibonacci_tester.values())[0]
        r = requests.get('http://localhost:5000/fibonacci/'+str(list(TestClass.fibonacci_tester.keys())[0]))
        assert base_json == json.loads(r.text)

    ## prime testers
    def test_prime_2(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[0]
        base_json["output"] = list(TestClass.prime_tester.values())[0]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[0]))
        assert base_json == json.loads(r.text)
    def test_prime_3(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[1]
        base_json["output"] = list(TestClass.prime_tester.values())[1]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[1]))
        assert base_json == json.loads(r.text)
    def test_prime_5(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[2]
        base_json["output"] = list(TestClass.prime_tester.values())[2]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[2]))
        assert base_json == json.loads(r.text)
    def test_prime_73(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[3]
        base_json["output"] = list(TestClass.prime_tester.values())[3]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[3]))
        assert base_json == json.loads(r.text)
    def test_prime_1(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[4]
        base_json["output"] = list(TestClass.prime_tester.values())[4]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[4]))
        assert base_json == json.loads(r.text)
    def test_prime_string(self):
        base_json = TestClass.base_json
        base_json["input"] = list(TestClass.prime_tester.keys())[5]
        base_json["output"] = list(TestClass.prime_tester.values())[5]
        r = requests.get('http://localhost:5000/is-prime/'+str(list(TestClass.prime_tester.keys())[5]))
        assert base_json == json.loads(r.text)

    slack_base_json ={
        "input":"foo",
        "posted":True
    }

    ##slack tester
    def test_slack_test(self):
        base_json = TestClass.slack_base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[0]
        r = requests.get('http://localhost:5000/slack-alert/'+str(list(TestClass.md5_tester.keys())[0]))
        assert base_json == json.loads(r.text)
    def test_slack_testytesty(self):
        base_json = TestClass.slack_base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[1]
        r = requests.get('http://localhost:5000/slack-alert/'+str(list(TestClass.md5_tester.keys())[1]))
        assert base_json == json.loads(r.text)
    def test_slack_tester(self):
        base_json = TestClass.slack_base_json
        base_json["input"] = list(TestClass.md5_tester.keys())[2]
        r = requests.get('http://localhost:5000/slack-alert/'+str(list(TestClass.md5_tester.keys())[2]))
        assert base_json == json.loads(r.text)






    #base json to test POST, PUT, GET, DELETE
    base_json_HTTP = {
    "key": "foo",
    "value": "some value",
    "command": "DELETE",
    "result": True,
    }
    #Testing json for get, delete
    base_json_error_GD = {
        "key": "foo",
        "command": "DELETE",
    }   
    def test_keyval_get_sprite(self):
        testCase = "sprite"
        x = getRequest(testCase)
        base_json = TestClass.base_json_error_GD
        base_json["key"] = testCase
        base_json["command"] = "GET " + testCase
        base_json["error"]="Key value pair doesn't exist, cannot get/delete record."
        assert json.loads(x[0])==base_json
        assert x[1]==404
    def test_keyval_post_sprite_quenching(self):
        testCase = ["sprite","quenching"]
        x = postRequest(testCase[0],testCase[1])
        base_json = TestClass.base_json_HTTP
        base_json["key"] = testCase[0]
        base_json["value"] = testCase[1]
        base_json["result"]=True
        base_json["command"] = "CREATE " + testCase[0]+"/"+testCase[1]
        assert json.loads(x[0])==base_json
        assert x[1]==200
    def test_keyval_put_sprite_thirsty(self):
        testCase = ["sprite","thirsty"]
        x = putRequest(testCase[0],testCase[1])
        base_json = TestClass.base_json_HTTP
        base_json["key"] = testCase[0]
        base_json["value"] = testCase[1]
        base_json["result"]=True
        base_json["command"] = "UPDATE " + testCase[0]+"/"+testCase[1]
        assert json.loads(x[0])==base_json
        assert x[1]==200
    def test_keyval_put_num_346(self):
        testCase = [3,6]
        x = putRequest(testCase[0],testCase[1])
        base_json = TestClass.base_json_HTTP
        base_json["key"] = testCase[0]
        base_json["value"] = testCase[1]
        base_json["result"]=False
        base_json["command"] = "UPDATE " + str(testCase[0])+"/"+str(testCase[1])
        base_json["error"] = "Key doesn't exist, cannot update record."
        assert json.loads(x[0])==base_json
        assert x[1]==404
    def test_keyval_get_sprite(self):
        testCase = "sprite"
        x = getRequest(testCase)
        base_json = TestClass.base_json_error_GD
        base_json["key"] = testCase
        base_json["command"] = "GET " + testCase
        base_json["result"] = True
        base_json["value"] = "thirsty"
        assert json.loads(x[0])==base_json
        assert x[1]==200
    def test_keyval_delete_sprite(self):
        testCase = "sprite"
        x = deleteRequest(testCase)
        base_json = TestClass.base_json_error_GD
        base_json["key"] = testCase
        base_json["value"]="thirsty"
        base_json["command"] = "DELETE " + testCase
        assert json.loads(x[0])==base_json
        assert x[1]==200
