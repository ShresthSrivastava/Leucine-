import pytest
import API

ID=0 #Global Variable to store ID fetched

def test_Post():
    URL = "https://jsonplaceholder.typicode.com/posts" #URL To post request 
    para = {"title": 'Shresth',"body": 'Srivastava',"userId": 12} #API parameters
    assert API.post(URL,para) == 201 #Testing Passing or Failing of the the Function


def test_put():
    URL = "https://jsonplaceholder.typicode.com/posts/1" #URL to put an update request
    DATA = {"id": 101,"title": 'Ansh',"body": 'Srivastava',"userId": 12} #API parameters
    assert API.put(URL,DATA) == 200 #Testing Passing or Failing of the the Function


def test_fetchID():
    global ID
    URL = "https://jsonplaceholder.typicode.com/posts" #URL To fetch request 
    Title = "Ansh"
    ID,code = API.fetchID(URL,Title)
    assert code == 200 #Testing Passing or Failing of the the Function

def test_fetchUser():
    URL = "https://jsonplaceholder.typicode.com/posts/"+str({ID}) #URL To fetch request 
    assert API.fetchUser(URL) == 200,"User Not Found" #Testing Passing or Failing of the the Function

def test_fetchComnt():
    URL = "https://jsonplaceholder.typicode.com/post/"+str({ID})+"/comments" #URL To fetch request 
    assert API.fetchComnt(URL) == 200,"User Not Found" #Testing Passing or Failing of the the Function