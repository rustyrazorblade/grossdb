# from copy import deepcopy
import logging
from grossdb.results import Results

logger = logging.getLogger(__name__)

class QueryPlan(object):
    _operations = None
    _db = None

    def __init__(self, db):
        self._operations = []
        self._db = db

    def select(self, table):
        self._operations.append(TableScan(table))
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



class QueryOperation(object):
    pass


class TableScan(QueryOperation):
    _table = None

    def __init__(self, table):
        self._table = table

    def execute(self, results):
        # returns a new Results
        r = Results()
        for row in self._table._rows:
            r._rows.append(row)
        return r


class AndOperation(QueryOperation):
    # takes 2 predicates
    pass


class OrOperation(QueryOperation):
    # takes 2 predicates
    pass


class PredicateFilter(QueryOperation):
    pass


class IndexQuery(QueryOperation):
    pass


class Join(QueryOperation):
    pass


class Aggregation(QueryOperation):
    pass

