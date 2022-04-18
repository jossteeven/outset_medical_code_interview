# outset_medical_code_interview
Coding Exercises During Technical Interview (Outset Medical)


To test each of the exercises in this repo I recommend you to build up a virtual environment with the libraries listed in the requerements.txt file


Local Set Up Steps

	1. Install Virtualenv
		pip install virtualenv
	2. Create python virtual env
		virtualenv .venv -p python
	3. Install libraries in requerements.txt
		pip install -r requerements.txt

Run Python Project (3 Options)

	1. At the root path of the repository and check all tests execute:
		pytest
	3. At the root path an check each "test_*.py" file with unittest execute:
		python -m unittest test.test_[name_of_the_src_file]
	4. At the root path an check each "test_*.py" file with nose execute:
		nosetests ./test_[name_of_the_src_file].py