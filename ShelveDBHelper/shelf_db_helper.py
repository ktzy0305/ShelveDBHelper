import shelve
import uuid
from ShelveDBHelper.shelf_db_errors import *

class DBHelper:

    def __init__(self, db_name):
        self.db_name = db_name

    def open_db(self):
        self.db = shelve.open(self.db_name)

    def close_db(self):
        self.db.close()

    def create_key(self, key):
        if key not in self.db:
            self.db[key] = []
        else:
            raise KeyDoesNotExistError("The key '{0}' already exists".format(key))
    
    def delete_key(self, key):
        if key in self.db:
            del self.db[key]
        else:
            raise KeyDoesNotExistError("The key '{0}' does not exist".format(key))
    
    def get_keys(self):
        return self.db.keys()

    def add(self, key, item):
        object_list = self.db[key]
        object_list.append(item)
        object_list[len(object_list) - 1]["uuid"] = uuid.uuid1()
        self.db[key] = object_list

    # def delete(self, key, index):
    #     object_list = self.db[key]
    
    def get(self, key):
        if key in self.db:
            values = self.db[key]
            return values
        else:
            raise KeyDoesNotExistError("The key '{0}' does not exist".format(key))