VENV = venv-ex-rudimentar
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

.PHONY: run install clean

run:
	$(PYTHON) exemplo_rudimentar.py

install: venv-ex-rudimentar requirements.txt
	$(PIP) install -r requirements.txt

venv-ex-rudimentar:
	python3 -m venv $(VENV)

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
