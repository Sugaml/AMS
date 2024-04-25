createvenv:
	python -m venv venv

activate:
	source venv/bin/activate

dependencies:
	pip install -r requirements.txt

run:
	python manage.py runserver

superuser:
	python manage.py createsuperuser