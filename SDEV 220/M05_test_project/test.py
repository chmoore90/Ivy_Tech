import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()


"""
COMMAND LINE TESTS:

python -m unittest test
    executes the test.py file, just from the command line
    gives same result as running this file directly from VS Code

python -m unittest -v test
    executes the test.py file and gives more detail in results
    gives a readout of which tests failed and passed, then gives details on the failure paths

python -m unittest discover
    searches current directory for all files beginning with the word "test", and tests them (this directly has four)

python -m unittest discover -s M05_test_project
(changed directory name to match my files, tutorial instructions had "tests" here)
    searchs directory named after "-s" for files beginning with the word "test", and tests them
    "-s" seems to indicate "subdirectory", when I moved to this directory's parent folder and gave the it gave the same results as the previous test

python -m unittest discover -s M05_test_project -t ???
    I couldn't figure out what the tutorial was talking about and eventually gave up

"""
