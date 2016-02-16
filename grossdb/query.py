
class QueryPlan(object):
    _operations = None
    _db = None

    def __init__(self, db):
        self._operations = []
        self._db = db

    def optimize(self):
        # returns a new, optimized query plan
        pass


class QueryOperation(object):
    pass


class SelectOperation(QueryOperation):
    _table = None
    
    def __init__(self, table):
        self._table = table


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

