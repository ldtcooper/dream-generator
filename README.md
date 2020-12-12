# README

This is a text generator trained off of posts from r/DreamInterpretation. It consists of several parts:

- `dream-catcher` a data scraper to get posts from the sub
    - `dream-catcher.py` is the actual scraper that gets the reddit posts.
    - `test.sh` is a debugging script for `dream-catcher.py`. It backs up `dreams.tsv`, deletes it and `dreams.json`, and then runs `dream-catcher.py`. It's most useful when used in conjunction with the debug functions in `dream-catcher.py`
    - `dream-cleaner.ipynb` is a Jupyter notebook to clean `dreams.tsv`

## Installation
Each part of this project has its own venv due to requirement conflicts between the two parts of the project.

### `dream-catcher`
You can run the scraper without any external dependencies, although the to run the cleaner, you will want to install a venv in the `dream-catcher` directory from `dream-catcher/requirements.txt`.