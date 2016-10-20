from google.appengine.ext import ndb

class Trip(ndb.Model):
    # State the trip was taken
    state = ndb.StringProperty()

    # City visited
    city = ndb.StringProperty()

    # Date trip was started
    start_date = ndb.StringProperty()

    # Date trip ended
    end_date = ndb.StringProperty()

    # Text description of the trip
    description = ndb.TextProperty()

    # Last date time the trip was modified
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)

    # Reference to the image blob(s)
    media_blob_key = ndb.BlobKeyProperty() # repeated=True
