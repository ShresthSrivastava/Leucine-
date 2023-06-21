import requests #To handle API request
import logging #To implement Logging

# Get logger
logger = logging.getLogger("my logger")
file_handler = logging.FileHandler('App.log',mode='w')
# Create a handler
c_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - Line: %(lineno)d - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
c_handler.setFormatter(formatter)

# link handler to logger
logger.addHandler(file_handler)
logger.addHandler(c_handler)

# Set logging level to the logger
logger.setLevel(logging.DEBUG)

###########################################     Post Request to Create resource Function     ##########################################

def post(URL,para): #Function to Post request
    try:
        Respon = requests.post(URL,json=para) #Posting Request to API

        logger.info("Response Status Code " + str(Respon.status_code)) #Logging the Info for better debugging

        logger.info("Response Data " + str(Respon.text)) #Logging the Info for better debugging

        return Respon.status_code #Returning the status code value
    except Exception as e:
        logger.exception(e)

###########################################     Put Request to update resource Function     ##########################################

def put(URL,DATA): #Function to put request
    try:
        Respon = requests.put(URL,data=DATA) #putting Request to API

        logger.info("Response Status Code " + str(Respon.status_code)) #Logging the Info for better debugging

        logger.info("Response Data " + str(Respon.text)) #Logging the Info for better debugging

        return Respon.status_code #Returning the status code value
    except Exception as e:
        logger.exception(e)

###########################################    Get Request to Fetch ID Function     ###################################################

def fetchID(URL,TITLE): #Function to fetch ID request
    try:
        Respon = requests.get(URL) #Posting Request to API

        logger.info("Response Status Code " + str(Respon.status_code)) #Logging the Info for better debugging

        # logger.info("Response Data " + str(Respon.text)) #Logging the Info for better debugging
        
        J = Respon.json()
        for i in J:
            if TITLE == i.get("title"):
                print("Title Found == " + TITLE)
                id = i.get("id")
                return id,Respon.status_code
            else:
                logger.error("Tittle Not Found")
                raise Exception("Tittle Not Found")

        
    except Exception as e:
        logger.exception(e)
        return 0,Respon.status_code


###########################################    Get Request to User Data Function     ###################################################

def fetchUser(URL): #Function to fetch ID request
    try:
        Respon = requests.get(URL) #Posting Request to API

        logger.info("Response Status Code " + str(Respon.status_code)) #Logging the Info for better debugging

        logger.info("Response Data " + str(Respon.text)) #Logging the Info for better debugging
        
        return Respon.status_code
    except Exception as e:
        logger.exception(e)


###########################################    Get Request to User Data Comment Function     ###########################################

def fetchComnt(URL): #Function to fetch ID request
    try:
        Respon = requests.get(URL) #Posting Request to API

        logger.info("Response Status Code " + str(Respon.status_code)) #Logging the Info for better debugging

        logger.info("Response Data " + str(Respon.text)) #Logging the Info for better debugging
        
        return Respon.status_code
    except Exception as e:
        logger.exception(e)


###########################################    Fucntion Calls  ########################################################################


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/posts"
    para = {"title": 'Shresth',"body": 'Srivastava',"userId": 12}
    code_post = post(URL,para) #function call for checking the result of the function

    URL = "https://jsonplaceholder.typicode.com/posts/1"
    DATA = {"id": 101,"title": 'Ansh',"body": 'Srivastava',"userId": 12}
    code_put = put(URL,DATA) #function call for checking the result of the function

    URL = "https://jsonplaceholder.typicode.com/posts"
    Title = "Ansh"
    id,code_fetch = fetchID(URL,Title) #function call for checking the result of the function

    URL = "https://jsonplaceholder.typicode.com/posts/"+str({id})
    fetchUser(URL) #function call for checking the result of the function

    URL = "https://jsonplaceholder.typicode.com/post/"+str({id})+"/comments"
    fetchComnt(URL) #function call for checking the result of the function