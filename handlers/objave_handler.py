import cgi
import uuid

from google.appengine.api import users, memcache

from handlers.base_handler import BaseHandler
from models.models import Objava


class DodajObjavoHandler(BaseHandler):
    def get(self):
        params = {
            "csrf_zeton": str(uuid.uuid4())
        }
        memcache.add(params["csrf_zeton"], True, 60 * 10)
        return self.render_template("dodaj_objavo.html", params)

    def post(self):
        vrednost_csrf = self.request.get("csrf-zeton")

        if not memcache.get(vrednost_csrf):
            return self.write("CSRF napad v dogajanju.")

        naslov = cgi.escape(self.request.get("title"))
        vsebina = cgi.escape(self.request.get("text"))
        uporabnik = users.get_current_user()
        email = uporabnik.email()
        nova_objava = Objava(naslov=naslov,
                             vsebina=vsebina,
                             uporabnik_email=email)
        nova_objava.put()
        return self.write("Objava dodana.")


class PreglejObjaveHandler(BaseHandler):
    def get(self):
        objave = Objava.query().order(-Objava.cas_objave).fetch()
        params = {
            "objave": objave
        }
        return self.render_template("preglej_objave.html", params)


class PreglejObjavoHandler(BaseHandler):
    def get(self, objava_id):
        objava = Objava.get_by_id(int(objava_id))
        if not objava:
            return self.write('Te objave ni.')
        params = {
            "objava": objava
        }
        return self.render_template("preglej_objavo.html", params)
