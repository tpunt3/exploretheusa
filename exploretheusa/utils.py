from google.appengine.ext import ndb
from models import Trip

def get_parent_key_for_email(email):
    return ndb.Key("Entity", email.lower())

def get_query_for_all_trips_for_email(email):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key).order(Trip.state)
    
def get_query_for_all_distinct_states_for_email(email):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key, projection=["state"], distinct=True).count()
