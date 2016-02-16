
class QueryPlan(object):
    _operations = None

    def __init__(self):
        self._operations = []

    def optimize(self):
        # returns a new, optimized query plan
        pass


class QueryOperation(object):
    pass


class SelectOperation(QueryOperation):
    pass


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

