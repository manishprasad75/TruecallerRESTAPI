import os, sys
sys.path.insert(0, os.path.abspath("../"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'Truecaller.settings'

import django
django.setup()

import csv
import requests
from requests.auth import HTTPBasicAuth
from mysite.models import UsersContact, UserSpam, User
from user.models import UserProfile
import random

base_url = 'http://127.0.0.1:8000/'


def register_user():
    register_user = "dummy_data/register_user.csv"
    endpoint = "api/register/"
    url = base_url+endpoint
    # obj = ()
    with open(register_user) as user:
        csv_reader = csv.DictReader(user)
        for row in csv_reader:
            r = requests.post(url, json=row)
            print(r.status_code)
            data = r.json()
            print(data)

def print_csv_data():
    user_contacts = "dummy_data/user_contacts.csv"
    endpoint = "api/user/"
    url = base_url + endpoint

    with open(user_contacts) as user_contacts:
        csv_reader = csv.DictReader(user_contacts)
        for row in csv_reader:
            # print(row)
            # import pdb
            # pdb.set_trace()
            queryset = User.objects.all()
            row['synced_from_uid'] = random.choice(queryset).id
            r = requests.post(url, json=row, auth=HTTPBasicAuth(username="admin", password="admin"))
            # print(r.status_code)
            # data = r.json()
            # print(data)
            # break

print_csv_data()
register_user()