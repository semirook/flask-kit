# -*- coding: utf-8 -*-
from jinja2.environment import Template


BLUEPRINT_VIEWS_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint
from flask.templating import render_template
from flask.views import View


{{ blueprint_name }} = Blueprint('{{ blueprint_name }}', __name__, template_folder='templates', static_folder='static')

''')


BLUEPRINT_INIT_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-

# Put your {{ blueprint_name }} blueprint views here

''')


BLUEPRINT_MODELS_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-


# Put your {{ blueprint_name }} blueprint models here

''')
