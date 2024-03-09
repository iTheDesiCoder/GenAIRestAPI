import os

environment = os.getenv('ENVIRONMENT', 'local')

if environment == 'local':
    from config_local import *
else:
    raise ValueError("Invalid environment name")