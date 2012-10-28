## What the Flask Kit is and what is not

**Flask Kit** is about [Flask](http://flask.pocoo.org/) project organization.
It's not yet another Python web-framework, it's not some kind of battery 
and it's not a layer on the top of original Flask.

*Flask Kit is extendable backbone for your new Flask projects
and the set of useful helpers to avoid some routine.* That's it.

And it looks like this:

```
/flaskit
    /blueprint
        __init__.py
        views.py
        models.py
        forms.py
        tests.py
        context_processors.py
        /static
        /templates
        ...
    app.py
    ext.py
    helpers.py
    settings.py
    manage.py
    testing.py
    reqs.pip
    ...
```

Flask doesn't teach us how to organize projects, there are (almost) no best practices for that and
there are real problems with circular imports sometimes.

Maybe you are already familiar with [Larger Applications](http://flask.pocoo.org/docs/patterns/packages/),
[Becoming Big](http://flask.pocoo.org/docs/becomingbig/) and
[Design Decisions in Flask](http://flask.pocoo.org/docs/design/) articles.
If not yet - spend a bit of time and read them to have more clear understanding of Flask internal design.

### The main idea of Flask Kit

Flask is not MVC framework but it's possible to bring some MVC experience with minimum set of background magic,
with nice and neat project structure and without circular import problems.

I hope, that you'll find this kit useful for your new Flask-based projects.


## Installation

Flask Kit installation process is trivial. I'm sure, everyone use `virtualenv`
and I don't have to explain how to setup and use it.

1. ```git clone git://github.com/semirook/flask-kit.git```
2. ```cd flask-kit```
3. ```pip install -r reqs.pip```


## Run

There is some demo data for you. Create it.  
1. ```./manage.py init_data```

Run development server, and go to http://127.0.0.1:5000  
2. ```./manage.py runserver```

Demo user login/password is john@doe.com/test.


## Configuration

Flask Kit consists of some helpers, demo blueprints,
`app.py`, `ext.py`, `helpers.py`, `manage.py`, `settings.py` and `testing.py` modules.

Let's take a look at each of them.


### app.py

There is your main app instance, created by `AppFactory`. Note, it's just a point for blueprints,
context processors and extensions binding. But don't bind them explicit, as usual. And don't bind any views
to the main app. Why?

You have at least two apps in your project – one as the basic app and one for testing.
Each of them is created at runtime with some individual settings for database, debug level etc.
And each of them has to have access to any views or extensions with their individual settings.
So dynamical application binding is much more flexible solution.


### ext.py

I've found it neat to define all extensions separately and bind them to the application at runtime.
Unfortunately, it's possible if extension provides init_app() method only. But for some not-so-smart
extensions there is some workaround. Look into the file for examples.


### helpers.py

There is the application factory and, maybe, something else (in the future) to avoid routine.


### testing.py

Simple basic TestCase for your tests. Note, that `nose` test runner is used (it's really good).

```
(flaskit)MacBook-Pro-Roman:flaskit semirook$ nosetests
...
----------------------------------------------------------------------
Ran 3 tests in 0.476s

OK
```


### settings.py

Note some Kit-specific settings.

`BLUEPRINTS` is a list of registered blueprints.  
`CONTEXT_PROCESSORS` is a list of registered context processors.  
`EXTENSIONS` is a list of registered extensions.  

Flask Kit will automatically register blueprints specified in the `BLUEPRINTS`
list for you. Behaviour for `CONTEXT_PROCESSORS` and `EXTENSIONS` lists is the same.

The notation is `package.module.object` or `package.object` if object is in the `__init__.py`.
Look into the file for examples.


### manage.py

A set of scripts that you may find useful. Amount of commands will constantly
grow. By now, there are:

**Command**           | **Result**                                             |
----------------------|--------------------------------------------------------|
runserver             | Runs the Flask development server i.e. app.run()       |
shell                 | Runs interactive shell, ipython if installed           |
init_data             | Creates some demo DB-tables and data                   |
clean_pyc             | Removes all *.pyc files from the project folder        |

Run `./manage.py -h` for the list of all available commands.

Run `./manage.py command_name -h` for the list of command arguments.
