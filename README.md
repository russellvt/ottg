# Obey the Testing Goat
Another new walk-through (for me) of [Test Driven Development with
Python](https://www.obeythetestinggoat.com/book/chapter_01.html).

There is a [Github Repo](https://github.com/hjwp/book-example), but this
will be from scratch, and may have provisions for my own development
environments (mostly Vim, Pyenv, and/or PyCharm).


## Setup
Because "I'm weird," you can see instructions for my general setup in
the [SETUP](SETUP.md) file, here.


## Django Useful Commands and TDD Cycle

Running the Django dev server
    python manage.py runserver

Running the functional tests
    python functional_tests.py

Running the unit tests
    python manage.py test

The unit-test/code cycle
* Run the unit tests in the terminal.
* Make a minimal code change in the editor.
* Repeat!
