# from copy import deepcopy
from __future__ import print_function
import logging
from collections import namedtuple

from grossdb.results import Results

logger = logging.getLogger(__name__)

class QueryPlan(object):
    _operations = None
    _db = None

    def __init__(self, db):
        self._operations = []
        self._db = db

    def select(self, table, predicates=None):
        self._operations.append(TableScan(table, predicates))
        return self

    def optimize(self):
        # returns a new, optimized query plan
        pass


    def execute(self):
        results = Results()
        for ops in self._operations:
            logger.debug("exec")
            results = ops.execute(results)

        return results

    def __repr__(self):
        result = ""
        return result


class QueryOperation(object):
    pass


class TableScan(QueryOperation):
    _table = None
    _predicates = None

    def __init__(self, table, predicates=None):
        if predicates:
            assert isinstance(predicates, (PredicateFilter, AndOperation, OrOperation))

        self._table = table
        self._predicates = predicates

    def execute(self, results):
        # returns a new Results
        r = Results()
        for row in self._table._rows.itervalues():
            logger.debug("Scanning table")

            # evalate predicates, if any
            if self._predicates and not self._predicates.evaluate_row(row):
                continue

            r._rows.append(row)
        return r

    def __str__(self):
        return "TableScan <{}>".format(self._table._name)

    def __repr__(self):
        return "TableScan <{}>".format(self._table._name)


class AndOperation(QueryOperation):
    # takes 2 predicates
    pass


class OrOperation(QueryOperation):
    # takes 2 predicates
    pass

Field = namedtuple("Field", ["name"])

class PredicateFilter(QueryOperation):
    _lhs = None # usually a field, but could be a function on a field
    _op = None
    _rhs = None #right hand side derp
    def __init__(self, lhs, op, rhs):
        self._lhs = lhs
        self._op = op
        self._rhs = rhs

    def evaluate_row(self, row):
        # helper function
        # returns true if row satisfies predicate
        # if lhs is a field, we use the value of that field off the row

        if isinstance(self._lhs, Field):
            lhs = row[self._lhs.name]
        else: # TODO add function support
            lhs = self._lhs

        if isinstance(self._rhs, Field):
            rhs = row[self._rhs.name]
        else:
            rhs = self._rhs

        return self._op(lhs, rhs)


class IndexQuery(QueryOperation):
    pass


class Join(QueryOperation):
    pass


class Aggregation(QueryOperation):
    pass

