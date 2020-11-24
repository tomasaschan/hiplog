# hiplog

helping @el-hult make delicious rose hip wine

## using the tool

this is currently not published to pypi, so you'll have to clone it. then, install it with `pip`:

```sh
git clone https://github.com/tomasaschan/hiplog
pip install ./hiplog
```

you now have `hiplog` on your path; check `hiplog --help` for usage.

## dev environment setup

you'll need python 3.9+ and `pip` to install packages. you'll also want to install a type checker; for vs code, probably [pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).

you can set your environment it up however you want, but this is a way that works:

1. install `pyenv` and `pyenv-virtualenv`:

       curl https://pyenv.run | bash

   once installed, you'll also want to add this to your profile initialization, typically `~/.bashrc`:

       export PATH="$HOME/.pyenv/bin:$PATH"
       eval "$(pyenv init -)"
       eval "$(pyenv virtualenv init -)"

2. install python 3.9:

       pyenv install 3.9.0

3. create a virtual environment for this project

       pyenv virtualenv 3.9.0 hiplog

4. configure this folder to use your new virtual environment:

       pyenv local hiplog

5. install the build tooling:

       pip install -U pip setuptools wheel

6. install dev dependencies. this pulls in all project dependencies, plus things we need to build/test/work, but not to run, the project:

       pip install -r dev-requirements.txt

7. if you're using pylance, tell it to use this virtual environment, by using the "select python interpreter" from the command palette and browsing to `~/.pyenv/versions/hiplog/bin/python`
