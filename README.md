# Flask Kit
Flexible microkit for Flask microframework


## What the Flask Kit is and what it is not

**Flask Kit** is about [Flask](http://flask.pocoo.org/) project organization.
It's not yet another framework, it's not some kind of Python battery and it's not
a layer on the top of original Flask.

*Flask Kit is the general file structure for your new Flask projects
and the set of useful helpers to avoid some routine.* That's it.

I decided that the most comfortable and the most flexible project file structure
for my new Flask-based projects is:

```
/project
    /app
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /...
            /img
                /...
            /js
                /...
        /templates
            index.html
            ...
    ...
```

New versions of Flask give us the concept of [Blueprints](http://flask.pocoo.org/docs/blueprints/),
a simple way to build extendable applications. Blueprint encapsulates some logic,
models, urls, templates etc. to keep your main app clean and simple to maintain.
So, with a set of blueprints, the project file structure will be mostly like this:

```
/project
    /app
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /...
            /img
                /...
            /js
                /...
        /templates
            index.html
            ...
    /some_blueprint
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /...
            /img
                /...
            /js
                /...
        /templates
            some_template.html
            ...
    /another_blueprint
        __init__.py
        ...
    ...
```

But. It's important to remember that Flask is the microframework for relatively
small projects and doesn't provide any way to build non-micro applications/sites.
Maybe, you have already familiar with [Larger Applications](http://flask.pocoo.org/docs/patterns/packages/),
[Becoming Big](http://flask.pocoo.org/docs/becomingbig/) and
[Design Decisions in Flask](http://flask.pocoo.org/docs/design/) articles.
If not yet - spend a bit of time and read them to have a more clear understanding
of the Flask internal design.

### The main idea of the Flask Kit
The above file structure helps us to work around MVC/MTV pattern, which is a good
programming practice. Flask is not MVC framework. But it's possible to bring some
MVC experience with a minimum set of background magic to support the suitable
project structure.

I hope, that you'll find this kit useful for your new Flask-based projects.


## Installation

Flask Kit is the project backbone and the couple of helpers, such as nice
application factory. Installation process is very easy and trivial. I hope,
all of you use `virtualenv` and I don't have to explain how to setup and use it.

1. ```git clone git://github.com/semirook/flask-kit.git```
2. ```cd flask-kit```
3. ```pip install -r reqs.pip```

That's all!


## Configuration and modifying

Flask Kit consists of the `application` and `blueprint` example modules, core
`kit` module with some helpers, `manage.py` and `settings.py` files in the
root of the folder. The basic file structure is:

```
/flask-kit
    /application
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /...
            /img
            /js
        /templates
            main.html

    /blueprint
        /__init__.py
        /views.py
        /models.py
        /templates
            welcome_page.html

    /kit
        /__init__.py
        /helpers.py

    /settings.py
    /manage.py
```

If you have some experience with Django, you'll find this structure familiar and
intuitive. Write your logic in `views.py`, define your models in `models.py` and
so on. At the same time we have some stuff specific to Flask, such as explicit app
object, the concept of blueprints and some others. How can we work around it?


### settings.py
Notice a couple of Flask-Kit specific attributes:

`APP_PACKAGE` attribute defines the name of the package which contains
your main application instance (and it's located in the `application.views` module,
by default). It's necessary attribute to run you project and to make some
background tricks work. If you've decided to rename `application` module to
`common` or something like that, you have to specify this name in the
APP_PACKAGE attribute.

`APP_PACKAGE = 'application'` is default (example application package)


`INSTALLED_BLUEPRINTS` attribute is something from Django world :)
In Django you can separate some logic to the set of applications and hook up them
in INSTALLED_APPS list. In Flask, you have one main application and a set of
blueprints for the same task. Specify the names of your blueprints here and Kit
will automatically bind them to the app instance for you (you can use another
behaviour, as you will see short while later).

`INSTALLED_BLUEPRINTS = ['blueprint']` is default (example blueprint package)


### manage.py
Another useful stuff from Django world. The amount of commands will constantly
grow. By now, there are:

**Command**           | **Result**                                             |
----------------------|--------------------------------------------------------|
runserver             | Runs the Flask development server i.e. app.run()       |
shell                 | Runs interactive shell, ipython if installed           |
createblueprint       | Creates new blueprint package with the specified name  |

Run `./manage.py -h` for help and actual list of all available commands.

Run `./manage.py command_name -h` for the list of command arguments.


*To be continued...*
