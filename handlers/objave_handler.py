from google.appengine.api import users

from handlers.base_handler import BaseHandler
from models.models import Objava


class DodajObjavoHandler(BaseHandler):
    def get(self):
        return self.render_template("dodaj_objavo.html")

    def post(self):
        naslov = self.request.get("title")
        vsebina = self.request.get("text")
        uporabnik = users.get_current_user()
        email = uporabnik.email()
        nova_objava = Objava(naslov=naslov,
                             vsebina=vsebina,
                             uporabnik_email=email)
        nova_objava.put()
        return self.write("Objava dodana.")
