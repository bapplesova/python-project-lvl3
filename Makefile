install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install dist/*.whl --force-reinstall
reinstall:
	rm -r dist
	poetry build
	python3 -m pip install dist/*.whl --force-reinstall
asci:
	clear
	asciinema rec
push:
	git push -u origin main
page-loader:
    poetry run page-loader