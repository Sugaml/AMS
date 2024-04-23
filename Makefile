createvenv:
	python -m venv venv

activate:
	source venv/bin/activate

run:
	python manage.py runserver