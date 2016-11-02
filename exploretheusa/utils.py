from google.appengine.ext import ndb
from models import Trip

def get_parent_key_for_email(email):
    return ndb.Key("Entity", email.lower())

def get_filtered_query_for_all_trips_for_email(email, filter_type):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key).order(filter_type)    

def get_query_for_all_distinct_states_for_email(email):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key, projection=["state"], distinct=True).fetch()

def get_query_for_all_distinct_states_count_for_email(email):
    parent_key = get_parent_key_for_email(email)
    return Trip.query(ancestor=parent_key, projection=["state"], distinct=True).count()

def get_filter_type_from_string(filter_type):
    if filter_type.lower() == 'created date':
        return {'key': filter_type.lower(), 'value': -Trip.last_touch_date_time}
    elif filter_type.lower() == 'city':
        return {'key': filter_type.lower(), 'value': Trip.city}
    else:
        return {'key': 'state', 'value': Trip.state}
