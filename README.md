# Obey the Testing Goat
Another new walk-through (for me) of [Test Driven Development with
Python](https://www.obeythetestinggoat.com/book/chapter_01.html).

There is a [Github Repo](https://github.com/hjwp/book-example), but this
will be from scratch, and may have provisions for my own development
environments (mostly Vim, Pyenv, and/or PyCharm).

Current Python: 3.13.0


## My Environment
Note that I am intending to use both `Mercurial` and `github` for this
run-through... mostly because I tend to enjoy pain. I also tend to use
`vim` with things like `pylint` and `pyflakes` attached to it - so things
may be a little chaotic at times to clean-up "lazy" code.

### PyEnv
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
