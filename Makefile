install:
	#install commands
	pip install -r requirements.txt

test:
	#test commands
	python -m pytest -vv --cov=src/ app/tests/

start:
	#start commands
	python app/main.py