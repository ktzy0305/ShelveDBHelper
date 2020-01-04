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

    def delete(self, key, uuid):
        object_list = self.db[key]

    def find(self, key, **kwargs):
        if key in self.db:
            values = self.db[key]
            values_count = len(list(map(lambda x: x, values)))
            if values_count > 0:
                kwargs_keys = list(map(lambda x : x, kwargs))
                value_keys = list(map(lambda x : x, values[0]))
                if set(kwargs_keys).issubset(set(value_keys)):
                    match_result = []
                    for value in values:
                        match_count = 0
                        for kwargs_key in kwargs_keys:
                            if value[kwargs_key] == kwargs[kwargs_key]:
                                match_count += 1
                        if match_count == len(kwargs_keys):
                            match_result.append(value)
                    return match_result
                else:
                    print("The following arguments '{0}' do not exist in the key '{1}'.".format(set(kwargs_keys) - set(value_keys), key))
            else:
                print("There is no data in the key '{0}'.".format(key))
        else:
            raise KeyDoesNotExistError("The key '{0}' does not exist".format(key))
    
    def get(self, key):
        if key in self.db:
            values = self.db[key]
            return values
        else:
            raise KeyDoesNotExistError("The key '{0}' does not exist".format(key))

    def update(self, key):
        # Need a parameter for search condition
        # Need another parameter to set new values
        return

