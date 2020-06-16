virtenv:
	source ~/.StockTrader/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
test:
	python -m pytest -vv test_grab_function.py

lint:
	pylint --disable=R,C test_grab_function.py

all: install lint test