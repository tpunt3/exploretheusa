from google.appengine.ext import ndb

class Trip(ndb.Model):
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    start_date = ndb.StringProperty()
    end_date = ndb.StringProperty()
    description = ndb.TextProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
