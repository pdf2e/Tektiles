from django.db import connections

class DBRouter(object):


    def db_for_read(self, model, **hints):
        m = model.__module__.split('.')
        try:
            d = m[-1]
            if d in connections:
                return d
        except IndexError:
            pass
        return None

    def db_for_write(self, model, **hints):
        m = model.__module__.split('.')
        try:
            d = m[-1]
            if d in connections:
                return d
        except IndexError:
            pass
        return None

    def allow_syncdb(self, db, model):
        "Make sure syncdb doesn't run on anything but companion"
        if model._meta.app_label == 'companion':
            return False
        elif db == 'companion':
            return True
        return None

