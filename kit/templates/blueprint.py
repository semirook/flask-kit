# -*- coding: utf-8 -*-
from jinja2.environment import Template


BLUEPRINT_VIEWS_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-
from {{ blueprint_name }} import {{ blueprint_name }}

# Your {{ blueprint_name }} views might be here

''')


BLUEPRINT_INIT_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint


{{ blueprint_name }} = Blueprint('{{ blueprint_name }}', __name__,
                                 template_folder='templates',
                                 static_folder='static',
                                 url_prefix='/{{ blueprint_name }}')


# Blueprint's views
from views import *

''')


BLUEPRINT_MODELS_TEMPLATE = Template(u'''\
# -*- coding: utf-8 -*-

# Put your {{ blueprint_name }} blueprint models here

''')
