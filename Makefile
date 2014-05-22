export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=registration

.PHONY: test

test:
	flake8 registration --ignore=E124,E501,E127,E128
	coverage run --branch --source=registration `which django-admin.py` test tests
