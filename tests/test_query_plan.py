
from pytest import fixture

from grossdb.db import DB
from grossdb.query import QueryPlan


@fixture
def db():
    # TODO put this in a fixtures file, i'm going to need it everywhere
    db = DB()
    test = db.create_table("test")

    return db

def test_select(db):
    tab = db.get_table("test")
    plan = db.query().select(tab)
    assert isinstance(plan, QueryPlan)



