# Environmental Setup
I understand I'm a bit of an oddity, as I tend to avoid most IDEs, and
I tend to prefer to work from the commandline. As such, I may do things
a bit differently than most others.

This document hopes to give folks an idea of my general preferred
working environment.

Note: I'm generally a fan of Debian/Ubuntu, Cygwin, and WSL2 (pretty
much in that order). Windows System Linux 2 is my "newest" working
enviroment and, as such, may have a few odd caveats.


## Current Environment
Please always verify these against the `requirements` files for the
latest information.

* Python: 3.13.0
* Django: 5.1.3
* Selenium: 4.26.1


## Source Code Control
Note that I am intending to use both `Mercurial` and `github` for this
run-through... mostly because I tend to enjoy pain. I also tend to use
`vim` with things like `pylint` and `pyflakes` attached to it - so things
may be a little chaotic at times to clean-up "lazy" code.


## Python via PyEnv
I'm using [pyenv](https://github.com/pyenv/pyenv) to manage separate
Python versions. Unlike the `pyenv` method, I'll generally try to use
Python's built-in `venv` module to manage Virtual Environments. I use
the the [Basic GitHub Checkout](https://github.com/pyenv/pyenv#basic-github-checkout)
method for installing (mostly because I don't want my startup files
edited for me).

Essentially:

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"

The version of Python I used for this project is stored in in the usual
`pyenv` location: [.python-version](.python-version)

If you have sourced the `pyenv init --path` (as above), PyEnv will
automatically attempt to use it when you change in to this directory.


## Python Virtual Environment
Instead of using `pyenv-virtualenv`, I'm using the typical Python `venv`
module that is packaged with later versions of Python 3. The initial
setup is fairly routine:

    python3 -m venv venv-ottg-3.13.0
    . ./venv-ottg-3.13.0/bin/activate
    pip install pip setuptools wheel --upgrade

You should also install everything in the `requirements.txt` file:

    pip install -r requirements.txt

For development, you will likely also want the `requirements-dev.txt' file:

    pip install -r requirements-dev.txt

