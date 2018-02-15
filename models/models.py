from google.appengine.ext import ndb


class Objava(ndb.Model):
    vsebina = ndb.TextProperty()
    naslov = ndb.StringProperty()
    uporabnik_email = ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty(auto_now_add=True)
    cas_posodobitve = ndb.DateTimeProperty(auto_now=True)
    cas_izbrisa = ndb.DateTimeProperty()


class Komentar(ndb.Model):
    objava_id = ndb.StringProperty()
    vsebina = ndb.TextProperty()
    uporabnik_email = ndb.StringProperty()
    cas_objave = ndb.DateTimeProperty(auto_now_add=True)
    cas_posodobitve = ndb.DateTimeProperty(auto_now=True)
    cas_izbrisa = ndb.DateTimeProperty()
