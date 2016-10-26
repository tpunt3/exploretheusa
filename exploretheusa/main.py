#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os

from google.appengine.api import users
from google.appengine.ext.analytics.standaloneapp import MainPage
import jinja2
import webapp2

from handlers import blob_handler
from handlers.base_handlers import BasePage
from handlers.trip_handlers import InsertTripAction
from models import Trip
import utils


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    autoescape=True)

class LoginPage(BasePage):
    def get(self):
        user = users.get_current_user()
        if user:
            self.redirect("/home")
            return
        template = jinja_env.get_template("templates/login.html")
        values = {"login_url" :users.create_login_url("/home")}
        self.response.out.write(template.render(values))

class MainPage(BasePage):
    def get_page_title(self):
        return "Explore The USA"        
        
    def get_template(self):
        return "templates/mainpage.html"
    
    def update_values(self, email, values):
        values["num_trips"] = utils.get_query_for_all_distinct_states_for_email(email)

class ViewTripPage(BasePage):
    def get_template(self):
        return "templates/viewTrips.html"
    
    def update_values(self, email, values):
        if self.request.get("filter"):
            trip_filter = utils.get_filter_type_from_string(self.request.get("filter"))
        else:
            trip_filter = utils.get_filter_type_from_string('state')

        values["trip_filter"] = trip_filter['key']
        values["trip_query"] = utils.get_filtered_query_for_all_trips_for_email(email, trip_filter['value']);    
        
config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': 'mysupersecretkey',
}

app = webapp2.WSGIApplication([
    ('/', LoginPage),
    ('/home', MainPage),
    ('/insert-trip', InsertTripAction),
#     ('/delete-trip', DeleteTripAction),
    ('/view-trips', ViewTripPage),

    # for images
    ('/img/([^/]+)?', blob_handler.BlobServer)
], config=config, debug=True)
