import os

if (os.getenv('ENV') or "DEV").upper().startswith("PROD"):
    from .prod import *
else:
    from .dev import *