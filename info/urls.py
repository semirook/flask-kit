from . import info
from .views import HelpPageView

routes = [
        ((info),
            ('',HelpPageView.as_view('help')),
        )
    ]
