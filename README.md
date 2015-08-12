[![Circle CI](https://circleci.com/gh/OneStopSource/cz.pycon.org-2015.svg?style=svg)](https://circleci.com/gh/OneStopSource/cz.pycon.org-2015)

PyCon CZ 2015 -- early adopters version
=======================================

Welcome! It's really going to happen this year. The Czech PyCon, local python conference for anyone interested in Python programming language.

Join us
-------

PyCons are community events. Everybody is welcome, anyone can contribute. You can join us on following channels:

- Google Group -- [pycon-cs@googlegroups.com](https://groups.google.com/forum/#!forum/pycon-cs)
- [Trello](https://trello.com/czechpycon2015)
- [Slack](https://pyconcz.slack.com) -- request invite at tomas.ehrlich@gmail.com

Google Group mailing list is available for everyone. Trello is read-only for public and Slack is private. Send email to tomas.ehrlich@gmail.com if you want access them.

Contribute
----------

1. Setup development environment:

    ```
    npm install -g gulp bower
    
    cd static
    npm install
    bower install
    ```

2. Run *watcher* (it opens browser at http://localhost:3000):

    ```
    cd static && gulp
    ```

3. Commit changes and submit pull-request

Publish to AWS S3 (authorization required)
------------------------------------------

1. Copy `aws.json.example` to `aws.json` and provide credentials for your
   AWS IAM role.

2. Build all static assets and publish them to S3:

    ```
    gulp publish
    ```

License
-------

MIT

Planning
========

1. Name -- Czech only (PyCon CZ) or Czech+Slovak (PyCon CS)?
2. Duration
3. Date
4. Location

Duration - 2 days
-----------------

- 1 day of talks
- 1 day of sprints and/or workshops

Possible dates
--------------

See calendar at http://www.pycon.org for "PyCon free" weekends.

- 14-15/11/2015 - only one week after Django Under the Hood
- **21-22/11/2015**
- 28-29/11/2015
- december -- too late, too cold?

Location
--------

- Brno, VUT FIT
- Prague, ?
- ?

