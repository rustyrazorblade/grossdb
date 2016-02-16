from grossdb.db import DB
from grossdb.row import Row

def test_basic_db_operations():
    db = DB()
    tab = db.create_table("test")

    tab.insert(Row(name="jon", age="34"))

    assert tab._total == 1
