# Mini RAG Demo (with Amazon Bedrock or OpenAI)

> Demo of a personal assistant with Langchain, Streamlit and using Amazon Bedrock or OpenAI

## Project requirements

### Pyenv and `Python 3.11.4` (Optional but highly recommended)

- Install [pyenv](https://github.com/pyenv/pyenv) to manage your Python versions and virtual environments:

  ```bash
  curl -sSL https://pyenv.run | bash
  ```

  - If you are on MacOS and experiencing errors on python install with pyenv, follow this [comment](https://github.com/pyenv/pyenv/issues/1740#issuecomment-738749988)
  - Add these lines to your `~/.bashrc` or `~/.zshrc` to be able to activate `pyenv virtualenv`:
    ```bash
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    eval "$(pyenv init --path)"
    ```
  - Restart your shell

- Install the right version of `Python` with `pyenv`:
  ```bash
  pyenv install 3.11.4
  ```

### Poetry

- Install [Poetry](https://python-poetry.org) to manage your dependencies and tooling configs:
  ```bash
  curl -sSL https://install.python-poetry.org | python - --version 1.5.1
  ```
  _If you have not previously installed any Python version, you may need to set your global Python version before installing Poetry:_
  ```bash
  pyenv global 3.11.4
  ```

## Installation

### Create a virtual environment

Create your virtual environment and link it to your project folder:

```bash
pyenv virtualenv 3.11.4 mini-rag-demo
pyenv local mini-rag-demo
```

Now, every time you are in your project directory your virtualenv will be activated thanks to `pyenv`!

### Install Python dependencies through poetry

```bash
poetry install --no-root
```

## Streamlit App

The project includes a Streamlit app in ./demo/main.py.

Run the app with the following command:

```bash
PYTHONPATH=. streamlit run demo/main.py
```

Make sure you have loaded your API key for OpenAI in your environment variables or for Bedrock in your `~/.aws/credentials` file.

Switch between using OpenAI or Amazon Bedrock in the sidebar.

Change model settings in `./demo/constants/settings.py`.
