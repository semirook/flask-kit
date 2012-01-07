# Flask Kit
Microkit for the Flask microframework


## What the Flask Kit is and what it is not

*Flask Kit* is about [Flask](http://flask.pocoo.org/) project organizing. It's not yet another framework, it's not
some kind of Python battery and it's not a layer on top of the original Flask. *Flask Kit is the general file structure
of a Flask project and the set of useful helpers for it.* That's it.

I decided that the most comfortable and the most flexible project file structure for my new Flask-based projects is:

```
/project
    /app
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /style.css
            /img
                /image.png
            /js
                /jquery.js
        /templates
            index.html
    ...
```

New versions of the Flask give us a concept of Blueprints, a simple way to build extendable applications.
If you're not familiar with them - please, visit [Modular Applications with Blueprints](http://flask.pocoo.org/docs/blueprints/).
Blueprint encapsulates some logic, models, urls, templates etc. to keep your main app clean and simple to maintain.
So, with a set of blueprints, the project file structure will be mostly like this:

```
/project
    /app
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /style.css
            /img
                /image.png
            /js
                /jquery.js
        /templates
            index.html
    /some_blueprint
        /__init__.py
        /views.py
        /models.py
        /static
            /css
                /some_style.css
        /templates
            some_template.html
    /another_blueprint
        ...
    ...
```

It's important to remember that Flask is a microframework for small projects and doesn't provide any way to build
non-micro applications/sites. Maybe, you have already read the [Larger Applications](http://flask.pocoo.org/docs/patterns/packages/),
[Becoming Big](http://flask.pocoo.org/docs/becomingbig/) and [Design Decisions in Flask](http://flask.pocoo.org/docs/design/)
document sections. If not yet - spend a bit of time and read them to have a more clear understanding of the Flask
internal design.

### The basic idea of the Flask Kit
If you have some experience with Django, you should find the project structure above very familiar. Such kind of
file structure helps us to work around MVC/MTV pattern, which is a good programming practice. Flask is not MVC
framework, it was designed for much less complicated tasks. But we can work in usual manner and use the power and
elegance of Flask, powered by Werkzeug and Jinja tools. After some experiments I found the most straightforward
pattern for how to organize my Flask-based projects and wrote the minimum set of background magic for that.
I hope, that you'll find this kit useful and convenient for your own Flask-based projects.
