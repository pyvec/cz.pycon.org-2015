<!-- [![Circle CI](https://circleci.com/gh/pyvec/cz.pycon.org-2015.svg?style=svg)](https://circleci.com/gh/pyvec/cz.pycon.org-2015) -->

PyCon IL 2016 -- early adopters version
=======================================

<!-- Welcome! It's really going to happen this year. The Czech PyCon, local Python conference for anyone interested in Python programming language. -->
Welcome! This is the early repository of PyCon IL, the first Israeli PyCon.

Join us
-------

PyCons are community events. Everybody is welcome, anyone can contribute. You can join us on following channels:

- Google Group -- [pycon-israel@googlegroups.com](https://groups.google.com/forum/#!forum/pycon-israel)

Google Group mailing list is available for everyone. 
We also have a private Slack instanec. Send email to edanm@btlms.com if you want access to it.

Contribute
----------

1. Setup development environment:

    ```
    npm install -g gulp bower

    cd static
    npm install
    bower install
    ```

  (If you don't want to install system-wide, run e.g. `npm config set prefix ~/.local/npm_prefix` beforehand; then run the tools from `~/.local/npm_prefix/bin`.)

2. Run *watcher*:

    ```
    cd static && gulp
    ```

3. Visit http://localhost:3000/2016/

 This is needed because the development version doesn't have the 2016 redirect set up.

4. Commit changes and submit pull-request

5. If you're looking to make content changes, start in the
   static/jade/ directory (main page is index.jade). 

Publish to AWS S3 (Manual Process)
------------------------------------------

Currently, the only way to publish the site to our temporary staging url is
manually, and can be done by edanm.

Send in a pull request, and assuming all is well, he'll deploy it ASAP.

If you need to get in touch for any reason, feel free to send a message via
any means you feel like (email is edanm@btlms.com)


Attribution 
------------

This project is gratefully built on PyCon CZ's 2015 website.

License
-------

MIT
