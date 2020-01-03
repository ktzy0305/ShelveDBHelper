import shelve
import uuid
from ShelveDBHelper.shelf_db_errors import *

class DBHelper:

    def __init__(self, db_name):
        self.db_name = db_name
        db = shelve.open(db_name)
        db.close()

    def open_db(self):
        self.db = shelve.open()

    def create_key(self, key):
        db = shelve.open(self.db_name)
        if key not in db:
            db[key] = []
            db.close()
        else:
            db.close()
            raise KeyDoesNotExistError("The key '{0}' already exists".format(key))


    def add(self, key, item):
        db = shelve.open(self.db_name)
        if key not in db:
            db[key] = []
        object_list = db[key]
        object_list.append(item)
        object_list[len(object_list) - 1]["{0}_id".format(key)] = uuid.uuid1()
        db[key] = object_list
        db.close()
    
    def get(self, key):
        db = shelve.open(self.db_name)
        if key in db:
            values = db[key]
            db.close()
            return values
        else:
            db.close()
            raise KeyDoesNotExistError("The key '{0}' does not exist".format(key))