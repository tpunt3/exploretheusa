from google.appengine.ext import ndb
from models import Trip

def get_parent_key_for_email(email):
    return ndb.Key("Entity", email.lower())

def get_query_for_all_states_for_email(email):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key).order(Trip.state)
    