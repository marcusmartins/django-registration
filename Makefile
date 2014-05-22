export DJANGO_SETTINGS_MODULE=tests.settings
export PYTHONPATH=registration

.PHONY: test

test:
	`which django-admin.py` test tests
