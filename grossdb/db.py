from .table import Table
from .query import QueryPlan

class DB(object):
    _tables = None

    def __init__(self):
        self._tables = {}

    def create_table(self, name):
        # TODO check if table exists first
        table = Table(name)
        self._tables[name] = table
        return table

    def query(self):
        return QueryPlan(self)
