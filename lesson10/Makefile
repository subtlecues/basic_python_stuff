launch:
	@echo 'setting up'
	pip install -r requirements.txt
	@echo 'done setting up'
	@echo 'running tests'
	mypy  test_main.py main.py library.py
	flake8 --ignore=E501 main.py test_main.py library.py
	pytest test_main.py
	@echo 'done running tests'
	@echo 'opening files'
	python main.py
	python library.py
	python test_main.py
	@echo 'finished makefile deploy. thanks for your attention'


