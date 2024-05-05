.PHONY: run

# Python Code
clean:
	rm -rf dist
build:
	python -m build
run:
	py Temp-Linux-Shell/test.py
install:
	pip install .

