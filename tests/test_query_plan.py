from pytest import fixture

from grossdb.db import DB
from grossdb.query import QueryPlan
from grossdb.results import Results
from grossdb.row import Row
from grossdb.query import PredicateFilter
import operator
import logging

@fixture
def db():
    # TODO put this in a fixtures file, i'm going to need it everywhere
    db = DB()
    test = db.create_table("test")
    test.insert(Row(name="jon", age=34))

    return db

def test_select(db):
    tab = db.get_table("test")
    plan = db.query().select(tab)
    assert isinstance(plan, QueryPlan)

    results = plan.execute()

    assert isinstance(results, Results)

    assert len(results) == 1

def test_select_with_predicate(db):
    test = db.get_table("test")
    test.insert(Row(name="dave", age=44))
    results = db.query().select(test,
                                PredicateFilter("name",
                                                operator.eq,
                                                "jon")).execute()
    assert isinstance(results, Results)

    assert len(results) == 1
