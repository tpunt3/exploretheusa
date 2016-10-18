from handlers.base_handlers import BaseAction
from models import Trip
import utils


class InsertTripAction(BaseAction):
    def handle_post(self, email):
        trip = Trip(parent=utils.get_parent_key_for_email(email))
        
        trip.state = self.request.get("state")
        trip.city = self.request.get("city")
        trip.start_date = self.request.get("arrival-date")
        trip.end_date = self.request.get("departure-date")
        trip.description = self.request.get("description")
        # last touch modified time update? or nah?
        
        trip.put()
        self.redirect(self.request.referer)
