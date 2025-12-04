PYTHON = .venv/bin/python
MANAGE = $(PYTHON) manage.py

.PHONY: server refresh-db save-db

server:
	$(MANAGE) migrate
	$(MANAGE) flush --no-input
	$(MANAGE) loaddata mock_data
	$(MANAGE) runserver

refresh-db:
	$(MANAGE) flush --no-input
	$(MANAGE) loaddata mock_data

save-db:
	mkdir -p fixtures
	$(MANAGE) dumpdata --exclude contenttypes --exclude sessions --indent 2 > fixtures/mock_data.json
