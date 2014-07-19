from . import base
from .views import FrontView,LoginView,logout

routes = [
        ((base),
            ('',FrontView.as_view('front_page')),
            ('login',LoginView.as_view('login')),
            ('logout',logout, methods=['POST']),
        )
    ]

