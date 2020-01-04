import pytest
from ShelveDBHelper.shelf_db_helper import DBHelper
from ShelveDBHelper.shelf_db_errors import *

db_name = "newdb"

def test_create_db_helper():
    db = DBHelper(db_name)
    assert db.db_name == db_name

def test_create_new_key():
    db = DBHelper(db_name)
    db.open_db()
    db.create_key("users")
    number_of_items = len(db.get("users"))
    db.close_db()
    assert number_of_items == 0

def test_create_key_already_exists():
    with pytest.raises(KeyDoesNotExistError) as e:
        db = DBHelper("newdb")
        db.open_db()
        db.create_key("users")
        db.close_db()
    assert "The key 'users' already exists" in str(e.value)

def test_add_to_key():
    test_user_1 = {
        "email" : "user1@gmail.com",
        "password" : "password1",
        "username" : "user1",
    }

    test_user_2 = {
        "email" : "user2@gmail.com",
        "password" : "password2",
        "username" : "user2",
    }

    test_user_3 = {
        "email" : "user3@gmail.com",
        "password" : "password3",
        "username" : "user3",
    }

    db = DBHelper(db_name)
    db.open_db()
    original_count = len(db.get("users"))
    db.add("users", test_user_1)
    db.add("users", test_user_2)
    db.add("users", test_user_3)
    new_count = len(db.get("users"))
    db.close_db()
    assert new_count == original_count + 3

def test_key_find_value():
    db = DBHelper(db_name)
    db.open_db()
    result = db.find("users", email="user2@gmail.com")
    flag = result[0]["email"] == "user2@gmail.com"
    db.close_db()
    assert flag == True

def test_key_update_value():
    db = DBHelper(db_name)
    db.open_db()
    user2 = db.find("users", email="user2@gmail.com")
    db.update("users", values_to_update=user2, password="password2update")
    user2 = db.find("users", email="user2@gmail.com")[0]
    flag = user2["password"] == "password2update"
    db.close_db()
    assert flag == True

def test_key_delete_value():
    db = DBHelper(db_name)
    db.open_db()
    original_count = len(db.get("users")) 
    db.delete(key="users", email="user3@gmail.com", password="password3")
    new_count = len(db.get("users")) 
    flag = (original_count - 1) == new_count
    db.close_db()
    assert flag == True

def test_delete_key():
    db = DBHelper(db_name)
    db.open_db()
    db.delete_key("users")
    flag = "users" not in db.get_keys()
    db.close_db()
    assert flag == True