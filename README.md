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



Description
-----------

/event/report endpoint can handle requests having FE's actions.

Each action is splitted one by one, and stored as a one line log in the local storage.

Event log files are managed in the timed rotation manner and the retention period is set to 10 days, so before the end of the retention period, it's necessary to dump them.

These event logs need to be dumped to other permanent and analysis purposes storage like S3 or kafka using fluentd. And then events processing systems can be attached to post-process them. 



![Production Diagram](https://github.com/CreatorOh/events-collector/blob/main/production_diagram.jpeg)

To make the production system using this repository, it's necessary to set up the infrastructure like the above Diagram.

With a monitoring system to check the status of each collector instance, we can optimize the instance size according to the occurrence of events.

And also these kinds of systems can be easily leaked and targeted to be attacked, additional systems like anti ddos layer can be added in front of load balancer.








