# Flaskit
Flexible microkit for Flask microframework


## What the Flaskit is and what it is not

**Flaskit** is about [Flask](http://flask.pocoo.org/) project organization.
It's not yet another Python web-framework, it's not some kind of battery 
and it's not a layer on the top of original Flask.

*Flaskit is extendable backbone for your new Flask projects
and the set of useful helpers to avoid some routine.* That's it.

And it looks like this:

```
/flaskit
    /application
        __init__.py
        views.py
        models.py
        database.py
        context_processors.py
        /static
        /templates
        ...
    /blueprint
        __init__.py
        views.py
        models.py
        context_processors.py
        /static
        /templates
        ...
    settings.py
    manage.py
    reqs.pip
    ...
```

New versions of Flask give us the concept of [Blueprints](http://flask.pocoo.org/docs/blueprints/).
Blueprint encapsulates some logic, models, urls, templates etc. to keep your main app clean 
and your project simple to maintain and extend.

We can create rather big web projects with a set of blueprints because of separate entities and 
simpe plugging to the main application. It's architectural decision of Flask and it works cool.
Flask doesn't teach us how to organize our projects, there are no best practices for that and 
there are real problems with circular imports sometimes (when two modules depend on each other).

But. It's important to remember that Flask is the microframework for relatively
small projects and doesn't provide any way to build non-micro applications/sites.
Maybe you are already familiar with [Larger Applications](http://flask.pocoo.org/docs/patterns/packages/),
[Becoming Big](http://flask.pocoo.org/docs/becomingbig/) and
[Design Decisions in Flask](http://flask.pocoo.org/docs/design/) articles.
If not yet - spend a bit of time and read them to have more clear understanding
of Flask internal design.

### The main idea of Flaskit
The above file structure helps us to work around MVC/MTV pattern, which is a good
programming practice. Flask is not MVC framework but it's possible to bring some
MVC experience with a minimum set of background magic to support the suitable
project structure without circular import problems.

I hope, that you'll find this kit useful for your new Flask-based projects.


## Installation

Flaskit installation process is trivial. I'm sure, all of you use `virtualenv` 
and I don't have to explain how to setup and use it.

1. ```git clone git://github.com/semirook/flask-kit.git```
2. ```cd flask-kit```
3. ```pip install -r reqs.pip```

That's all!


## Configuration

Flaskit consists of the core `application` module, `blueprint` example module,
core `kit` module with some important helpers, `manage.py` and `settings.py` files in the
root of the folder.

If you have some experience with Django, you'll find this structure familiar and
intuitive. Write your logic in `views.py`, define your models in `models.py` and
so on. At the same time we have some stuff specific to Flask, such as explicit app
object, the concept of blueprints and some others. How can we work around it?


### settings.py
Notice a couple of Flaskit-specific attributes:

`APP_PACKAGE` attribute defines the name of the package which contains
your main application instance. It's necessary to run you project and to make some
background tricks. If you'll decide to rename `application` module to
`common` or something, rename the APP_PACKAGE attribute either.

`APP_PACKAGE = 'application'` is by default.

`INSTALLED_BLUEPRINTS` is a list of registered blueprints.

In Django you can separate some logic into the set of applications and hook up them
in INSTALLED_APPS list. In Flask you have one main application and a set of
blueprints for the same task. 

Flaskit will automatically register blueprints specified in the INSTALLED_BLUEPRINTS 
list for you.

`INSTALLED_BLUEPRINTS = ['blueprint']` is by default (example blueprint package).

`CONTEXT_PROCESSORS` is a list of registered context processors. You have to set 
full path to your processor module like 'application_or_blueprint.context_processors.processor'.
Django-style thing.


### manage.py
A set of scripts that you may find useful. Amount of commands will constantly
grow. By now, there are:

**Command**           | **Result**                                             |
----------------------|--------------------------------------------------------|
runserver             | Runs the Flask development server i.e. app.run()       |
shell                 | Runs interactive shell, ipython if installed           |
createblueprint       | Creates new blueprint package with the specified name  |
test                  | Nose test runner (with some restrictions yet)          |

Run `./manage.py -h` for the list of all available commands.

Run `./manage.py command_name -h` for the list of command arguments.
