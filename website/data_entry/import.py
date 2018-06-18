import csv,os,sys

project_dir = "/Users/m02ghan/PycharmProjects/website"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS-MODULE'] = 'settings'

import django
django.setup()

