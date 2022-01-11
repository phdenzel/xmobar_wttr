MODULE := xmobar_wttr

pkg: readme
	@pipenv run python setup.py sdist bdist_wheel

dev: readme
	@pipenv install --dev
	@pipenv install -e .

readme:
	@emacs --batch readme_src.org -f org-md-export-to-markdown
	@mv readme_src.md README.md

pytest:
	@pipenv run pytest -v --cov=xmobar_wttr --cov-report=html

clean:
	rm -rf .pytest_cache .coverage htmlcov README.md dist build
