# README

This is a text generator trained on posts from r/DreamInterpretation. It is built off of [Textgenrnn](https://github.com/minimaxir/textgenrnn). It consists of several parts:

- `dream-catcher` a data scraper to get posts from the sub
    - `dream-catcher.py` is the actual scraper that gets the reddit posts.
    - `test.sh` is a debugging script for `dream-catcher.py`. It backs up `dreams.tsv`, deletes it and `dreams.json`, and then runs `dream-catcher.py`. It's most useful when used in conjunction with the debug functions in `dream-catcher.py`
    - `dream-cleaner.ipynb` is a Jupyter notebook to clean `dreams.tsv`
- `generator` is the neural network that actually gnerates the dreams
    - `textgen.ipynb` is a notebook that has the NN code.
    - `dreamgen_config.json`, `dreamgen_vocab`, and `dreamgen_weights.hdf5` are files for the trained model that I've come up with.

## Installation
Each part of this project has its own conda enviornment due to requirement conflicts between the two parts of the project.

### `dream-catcher`
You can run the scraper without any external dependencies, although the to run the cleaner, you will want to install a conda enviornment from `dream-catcher/enviornment.yml`.

### `generator`
`generator.ipynb` requires the enviornment from the get-go. You'll need to install that first. You may also need to make some edits to the source code for `textgenrnn` depending on what versions of Keras and TensorFlow you have.

