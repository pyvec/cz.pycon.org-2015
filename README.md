> ⚠ This repository is archived 🗄
>
> [https://cz.pycon.org/2015/](https://cz.pycon.org/2015/) is now served as a static website. Look for it in the [repo for PyCon CZ 2019](https://github.com/pyvec/cz.pycon.org-2019/) (or further years).


[![Circle CI](https://circleci.com/gh/pyvec/cz.pycon.org-2015.svg?style=svg)](https://circleci.com/gh/pyvec/cz.pycon.org-2015)

PyCon CZ 2015 -- early adopters version
=======================================

Welcome! It's really going to happen this year. The Czech PyCon, local Python conference for anyone interested in Python programming language.

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

  (If you don't want to install system-wide, run e.g. `npm config set prefix ~/.local/npm_prefix` beforehand; then run the tools from `~/.local/npm_prefix/bin`.)

2. Run *watcher*:

    ```
    cd static && gulp
    ```

3. Visit http://localhost:3000/2015/

 This is needed because the development version doesn't have the 2015 redirect set up.

4. Commit changes and submit pull-request

Publish to AWS S3 (authorization required)
------------------------------------------

`master` branch is published automatically to [][cz.pycon.org] and `dev` branch
to [][dev.pycon.cz] in CircleCI. If you want to do it manually, you need to:

1. Copy `aws.json.example` to `aws.json` and provide credentials for your
   AWS IAM role.

2. Build all static assets and publish them to S3 (domain [][dev.pycon.cz]):

    ```
    gulp publish
    ```

Running `gulp publish --production` will publish static assets to
[][cz.pycon.org].

License
-------

MIT
