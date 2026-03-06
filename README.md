# COP4533
This is for the algo-abstraction coding assignments

Programming Assignment 2: Greedy Algorithms
------------------------------------------------
Yonash Petit: 6698-2151
HOW TO RUN: 
This is a python application so you should be able to go in to the directory of Programming Assignment 2 Greedy Algorithms and find the file "Assignment2.py" within the src folder. In the terminal, within the correct directory, run "py .\Assignment2.py" and it should output the results of the current tests that have been set up. You can make/look at test files in the "tests" folder, and you will also see an "example.out" file which shows the output for the tests cases that I personally tested. To test additional new testcases or alter the test cases currently active, there should be a "files" array in Assignments2.py on line 97 in which you can add or delete the files you want to test. If you want to test new files, you must first make the file in the "tests" folder, and append the name of the test file you create in the "files" variable within "Assignment2.py."

It should be noted that the caching algorithm are all in the "Assignment2.py" file. When this file is ran, the FIFO(), LRU(), and OPTFF() fucntions are ran in that order. Every file in the "files" array has their parameters passed into the run_benchmarks() function. The results of how many misses occuring in each algorithm are printed in the console.

ASSUMPTIONS:
It is assumed you have a relatively new version of python and you replace the py in "py .\Assignment2.py" with your personal path variable for python. It's also assumed the input will be formatted as the assignment instruction details, and the output of the program will be printed into the console/terminal.

Written Portion:
The written content is in the "writen_component.md" file within the "Programming Assignment 2 Greedy Algorithms" folder.



Programming Assignment 1: Matching and Verifying
------------------------------------------------
Yonash Petit: 6698-2151
HOW TO RUN: 
This is a python application so you should be able to go in to the directory of Programming Assignment 1: Matching and Verifying and find the file "Assignment1.py". In the terminal, within the correct directory, run "py .\Assignment1.py" and it should output the matches of the current tests that have been set up. You can make/look at test files in the "tests" folder, and you will also see an "output.txt" file which shows the output for the tests cases that I personally tested. To test additional new testcases or alter the test cases currently active, there should be a "test_files" array in Assignments1.py on line 164 in which you can add or delete the files you want to test. If you want to test new files, you must first make the file in the "tests" folder, and append the name of the test file you create in the "test_files" variable within "Assignment1.py."

It should be noted that the matching and verification algorithm are all in the "Assignment1.py" file. When this file is ran, the load_input(), get_ranked(), print_output(), and check_valid() fucntions are ran in that order. Every file in the "test_files" array is passed into the load_input() function where it's parsed and then validated as a "correct" matching schema. The parsed input is put into get_ranked() where the matching algorithm occurs, and then check_valid() checks if there are any unstable assignments.

ASSUMPTIONS:
It is assumed you have a relatively new version of python and you replace the py in "py .\Assignment1.py" with your personal path variable for python. It's also assumed the input will be formatted as the assignment instruction details, and the output of the program will be printed into the console/terminal.

TASK_C:
The Task C content is in the Task C folder within the "Programming Assignment 1: Matching and Verifying" folder.
