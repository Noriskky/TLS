.PHONY: all clean install run

all: clean install run
clean:
	rm -rf dist
build:
	python -m build
run:
	./venv/bin/tls
install:
	./venv/bin/pip3 install .

