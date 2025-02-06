from source.mydb import MyDB

def test_johns_id():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789

'''
Issues : 
1. Repeating lines 
2. Database connections, network connections are costly

In unittest, we use setup and teardown
'''

conn = None
cur = None

def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()

def teardown_module(module):
    cur.close()
    conn.close()

def test_johns1_id():
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms1_id():
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789


# Using fixtures:
import pytest

@pytest.fixture(scope="module")
def cur():
    print("Setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    # return curs #works for regular fixtures, But we are using database which must be closed after execution
    yield curs
    curs.close()
    conn.close()
    print("Tearing up")

def test_johns2_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms2_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789

