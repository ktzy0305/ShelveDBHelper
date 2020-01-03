import pytest
import os, sys
from ShelveDBHelper.shelf_db_helper import DBHelper
from ShelveDBHelper.shelf_db_errors import *

db_name = "newdb"

def test_create_db_helper():
    newdb = DBHelper(db_name)
    assert newdb.db_name == db_name

def test_create_new_key():
    db = DBHelper(db_name)
    db.create_key("users")
    assert len(db.get("users")) == 0

def test_create_key_already_exists():
    with pytest.raises(KeyDoesNotExistError) as e:
        db = DBHelper("newdb")
        db.create_key("users")
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

    db = DBHelper(db_name)
    original_count = len(db.get("users"))
    db.add("users", test_user_1)
    db.add("users", test_user_2)

    assert len(db.get("users")) == original_count + 2