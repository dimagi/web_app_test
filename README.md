Web App Test
============

This is a proof of concept to see whether we can use Microsoft
Playwright as a robust way to test an CommCare app via Web Apps.


Installation
------------

1. Create a virtual environment

       $ mkvirtualenv -p python3.8 web_app_test

2. Install requirements

       $ pip install -r requirements.txt

3. Install browsers for Playwright

       $ python -m playwright install


Running tests
-------------

1. Start your local CommCare HQ instance in a separate Terminal window.
   (Your method is sure to be different from mine.)

      $ workon cchq36
      $ cchq-tmux

2. Run tests

    $ pytest


Creating tests
--------------

1. Get Playwright to open a browser, and generate test code:

       $ python -m playwright codegen

2. Copy and paste the code into a Python test module.

3. The Playwright pytest plugin allows you to create test functions
   that accept `page` as a fixture parameter. You can remove the
   generated code at the start and end that instantiates the `page`
   object. See [test_mnch_app.py](test_mnch_app.py) as an example.


More info
---------

* [Microsoft Playwright for Python](https://github.com/microsoft/playwright-python)
* [Microsoft blog announcement](https://devblogs.microsoft.com/python/announcing-playwright-for-python-reliable-end-to-end-testing-for-the-web/)

