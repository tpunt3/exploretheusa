
from google.appengine.api import users, blobstore
import webapp2
from webapp2_extras import sessions

import main
from models import STATE_VALUES


# Potentially helpful (or not) superclass for *logged in* pages and actions (assumes app.yaml gaurds for login)
### Pages ###
class BasePage(webapp2.RequestHandler):
  """Page handlers should inherit from this one."""
  def get(self):
    user = users.get_current_user()
    values = {}
    if not user:
      self.redirect("/")
      return
    if user:
        email = user.email().lower()
        
    values["user_email"] = email,
    values["logout_url"] = users.create_logout_url("/")
    values["form_action"] = blobstore.create_upload_url('/insert-trip')
    values["states"] = STATE_VALUES

    self.update_values(email, values)  
        
    template = main.jinja_env.get_template(self.get_template())
    self.response.out.write(template.render(values))

  def dispatch(self):
    # Get a session store for this request.
    self.session_store = sessions.get_store(request=self.request)
    try:
        # Dispatch the request.
        webapp2.RequestHandler.dispatch(self)
    finally:
        # Save all sessions.
        self.session_store.save_sessions(self.response)
    
  @webapp2.cached_property
  def session(self):
    # Returns a session using the default cookie key.
    return self.session_store.get_session()

  def get_template(self):
    # Subclasses must override this method to set the Jinja template.
    raise Exception("Subclass must implement handle_post!")

### Actions ###

class BaseAction(webapp2.RequestHandler):
  """ALL action handlers should inherit from this one."""
  def post(self):
    user = users.get_current_user()
    if not user:
      raise Exception("Missing user!")
      return
    if user:
        email = user.email().lower()
        
    self.handle_post(email)

  def get(self):
    self.post()  # Action handlers should not use get requests.

  def handle_post(self, email):
    # Subclasses must override this method to handle the request.
    raise Exception("Subclass must implement handle_post!")

  def dispatch(self):
    # Get a session store for this request.
    self.session_store = sessions.get_store(request=self.request)
    try:
        # Dispatch the request.
        webapp2.RequestHandler.dispatch(self)
    finally:
        # Save all sessions.
        self.session_store.save_sessions(self.response)
    
  @webapp2.cached_property
  def session(self):
    # Returns a session using the default cookie key.
    return self.session_store.get_session()
  

