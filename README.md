# CS591L1_Final_Project

# Introduction:
Hello! Welcome to our wonderful project for our Embedded Languages and Frameworks class.

In this project, we will be utilizing and applying skills and programming paradigms that we learned from the course in order to read and detect tail-end recursion from a user's code and modify it such that instead of using recursion, it will use loops.

We have more details on the motivations and methodologies in the project proposal pdf included in the docs file within this repository! Please read it!

# Compilation and Running Instructions:
To utilize our project, please clone the repo and then navigate to wherever you saved it!
Please put the file that contains the code that you would like to have transformed from tail-end recursion to iterative loops into the "userCode" directory.
Then go to the "src" directory and run "main.py <insert your file name>" without the quotes. This will either raise an error if something went wrong and will print to the console the issue.
If such error occurs, please resolve the issue and then continue!
If everything went well, the transformed code will be written to or will overwrite a file named "<your file name>\_instrumented.py" within the "resultUser" directory.
Then please navigate to the result directory to then run and examine the newly transformed code!

# Testing:
We have three test files within the "test" directory.
These test that functionality works for tail recursion on factorial and reversing an array. The third test tests for if there are multiple functions with tail recursion and that it still works as intended. The results of the tests can be found in the "result"

Thanks,
Leo Chau & Jachen Liu -
Computer Science students at Boston University.
