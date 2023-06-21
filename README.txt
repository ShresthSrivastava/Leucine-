1. I have created an API.py file where for every Action regarding the API is written in and as different Function, hence it can be used just by calling then and passing the parameters.

2. For Testing these functions I have created TEST.py file which has pytest operations for every function and when executed with the command
"pytest -v TEST.py >TestLog.txt", it will create a TestLog.txt file giving the result of function passing the cases and failing the cases in a text file.

3. Logging has been used in the Python file for a better debugging and quicker turnaround from failure.

4. "__main__" is been used to call the function and check if they are giving the result and response, 
also from same file the functions can be imported directly to another file for reuseblity purpose.

5. Please Install Requests,Logging and pytest Library of python before running the file.
