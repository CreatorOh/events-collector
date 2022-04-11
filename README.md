Events Collector
======

The simple REST endpoint to collect events.


Install
-------

Clone the repository:

    $ git clone https://github.com/CreatorOh/events-collector
    $ cd events-collector

Create a virtualenv and activate it:

    $ python3 -m venv venv
    $ . venv/bin/activate

Install Events Collector:

    $ pip install -e .

Run
---

:

    $ export FLASK_APP=collector_backend
    $ export FLASK_ENV=development
    $ flask run


Open http://127.0.0.1:5000/api-docs in a browser.

And you can also try api calls with changing payloads.


Test
----

:

    $ pip install '.[test]'
    $ pytest






