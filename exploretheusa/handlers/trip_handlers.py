import logging

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers

from models import Trip
import utils


class InsertTripAction(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        user = users.get_current_user()
        if not user:
            raise Exception("Missing user!")
            return
        if user:
            email = user.email().lower()

        self.handle_post(email)

    def handle_post(self, email):
        if self.request.get("trip_entity_key"):
            trip_key = ndb.Key(urlsafe=self.request.get("trip_entity_key"))
            trip = trip_key.get()
        else:
            trip = Trip(parent=utils.get_parent_key_for_email(email))
        
        trip.state = self.request.get("state")
        trip.city = self.request.get("city")
        trip.start_date = self.request.get("arrival-date")
        trip.end_date = self.request.get("departure-date")
        trip.description = self.request.get("description")
        # last touch modified time update? or nah?
        
        # image
        if self.get_uploads() and len(self.get_uploads()) == 1:
            logging.info("Received an image blob with this trip.")
            media_blob = self.get_uploads()[0]
            trip.media_blob_key = media_blob.key()
        else:
            logging.info("This is a trip without an image attachment.")

        trip.put()
        self.redirect(self.request.referer)
