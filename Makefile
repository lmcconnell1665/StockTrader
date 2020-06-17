setup:
	source ~/.StockTrader/bin/activate
	
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
test:
	python -m pytest -vv test_function.py

lint:
	pylint --disable=R,C grab_function.py &&\
		pylint --disable=R,C clear_function.py

all: install lint test