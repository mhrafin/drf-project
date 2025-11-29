PYTHON = .venv/bin/python
MANAGE = $(PYTHON) manage.py

.PHONY: server refresh-db save-db

server:
	$(MANAGE) migrate
	$(MANAGE) loaddata mock_data
	$(MANAGE) runserver

refresh-db:
	$(MANAGE) flush --no-input
	$(MANAGE) loaddata mock_data

save-db:
	$(MANAGE) dumpdata watchlist_app --indent 2 > watchlist_app/fixtures/mock_data.json
