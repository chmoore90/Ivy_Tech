M05 Testing Lab. https://realpython.com/python-testing/#toc


COMMAND LINE TESTS:

python -m unittest test
    executes the test.py file, just from the command line
    gives same result as running this file directly from VS Code

python -m unittest -v test
    executes the test.py file and gives more detail in results
    gives a readout of which tests failed and passed, then gives details on the failure paths

python -m unittest discover
    searches current directory for all files beginning with the word "test", and tests them (this directly has four)

python -m unittest discover -s M05_testing
(changed directory name to match my files, tutorial instructions had "tests" here)
    searchs directory named after "-s" for files beginning with the word "test", and tests them
    "-s" seems to indicate "subdirectory", when I moved to this directory's parent folder and gave the it gave the same results as the previous test

python -m unittest discover -s M05_testing -t ???
    I couldn't figure out what the tutorial was talking about and eventually gave up
