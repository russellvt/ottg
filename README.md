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

Tests (All / Lists / Functional):
  * python manage.py test
  * python manage.py test lists
  * python manage.py test functional_tests

The unit-test/code cycle
* We write a test, and see it fail ("Red").
* We cycle between code and tests until the test passes: "Green".
* Then, we look for opportunities to refactor.
* Repeat as required!

![TDD Process as a Flow Chart](https://www.obeythetestinggoat.com/book/images/tdd-process-unit-tests-only-excalidraw.png)
![Red, Green, Refactor](https://www.obeythetestinggoat.com/book/images/red-green-refactor-excalidraw.png)

![Double Loop TDD](https://www.obeythetestinggoat.com/book/images/double-loop-tdd-simpler.png)


## References
Direct references that may later be useful.

* [Appendix Links](https://www.obeythetestinggoat.com/book/appendix_github_links.html)

### Future Reading
Some things referenced in the TDD book, worth a further look.

* [Python Testing with PyTest](https://refactoring.com/)
* [Refactoring](https://refactoring.com/)
* [Security Engineering](https://www.cl.cam.ac.uk/archive/rja14/book.html)
* [Code Smells](https://blog.codinghorror.com/code-smells/)
* [MMMSS](https://www.geepawhill.org/2021/09/29/many-more-much-smaller-steps-first-sketch/)
* [Selenium: Avoid Implicit Waits](https://www.selenium.dev/documentation/webdriver/waits/)
* [False Positives in Tests](https://martinfowler.com/articles/nonDeterminism.html)
