from .models import Utente, Valutazione


class PugliaEventiRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'api':
            return 'PugliaEventi'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'api':
            return 'PugliaEventi'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return obj1._meta.app_label == obj2._meta.app_label

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        #if app_label == 'api':
        #    return db == 'PugliaEventi'
        #return None
        return True
