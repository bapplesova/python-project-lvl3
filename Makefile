page-loader:
	page-loader --output /var/tmp https://ru.hexlet.io/courses
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
lint:
	poetry run flake8 page_loader
test:
	poetry run pytest -vv