#!/usr/bin/env python3
import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'umer.settings')
django.setup()

# Run collectstatic
execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])

print("Build completed successfully!")
