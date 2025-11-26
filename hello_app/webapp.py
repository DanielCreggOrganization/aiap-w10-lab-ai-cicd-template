"""Entry point for the application.

This module exposes `app` for tools like the `flask` command and imports
`views` for their side-effects (route registration).
"""

from . import app  # For application discovery by the 'flask' command.  # noqa: F401
from . import views  # For import side-effects of setting up routes.  # noqa: F401

# Time-saver: uncomment to quickly open the example URL in a local terminal
# print('http://127.0.0.1:5000/hello/VSCode')
