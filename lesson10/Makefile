launch:
	@echo 'setting up'
	pip install -r requierments.txt
	@echo 'done setting up'
	@echo 'launching files'
	python main.py library.py test_main.py
	@echo 'running tests'
	mypy  test_main.py main.py library.py
	flake8 --ignore=E501 main.py test_main.py library.py
	pytest test_main.py
	@echo 'done running tests'
	@echo 'finished makefile deploy. thanks for your attention'


