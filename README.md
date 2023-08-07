# sphinx-gallery-test

This repository gives a minimal example of the building and publishing documentation for a Python module using Sphinx, GitHub actions and github-pages.

Key points are:
 - automatic and recursive building of the documentation from documented Python modules using [sphinx autosummary](https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html)
 - working [sphinx-gallery](https://sphinx-gallery.github.io/stable/index.html) -- see for exemple [matplotlib's gallery](https://matplotlib.org/stable/gallery/index).
 - automatic building and publishing using GitHub actions when committing changes to repo.

## Short guide

1. clone the repository
2. install requirements `pip install -r requirements.txt`
3. build the documentation locally `cd` docs && make html` and check the files in `_build/html` (open `index.html` in a browser)
4. push the repo on a github repo. Check that the github actions worked fine.
5. enable github pages, with source `gh-pages/(root)`
6. you should be able to see the documentation at `https://user.github.io/repo/`


## Adapt it to your module

1. be sure to have some docstrings written inside your python module (see [here](https://www.datacamp.com/tutorial/docstrings-python).)
2. create a `docs` folder, and run inside `sphinx-quickstart`
3. tune your `conf.py` as you may wish. Note that it must include everything linked to `sphinx-gallery` if you wish to include one
4. run `make.html` and pray.

Important things:

- Look at `api.rst` and `index.rst` file structures, it is important.
- If you wish to document imports inside `__init__.py` files, set `autosummary_imported_members = True` in your `conf.py`.

## Resources

- Sphinx documentation:
  - https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html

- building and publishing using github actions:
  - https://coderefinery.github.io/documentation/gh_workflow/
  - https://github.com/peaceiris/actions-gh-pages#%EF%B8%8F-set-another-github-pages-branch-publish_branch
  - https://redandgreen.co.uk/sphinx-to-github-pages-via-github-actions/
