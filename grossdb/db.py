from .table import Table

class DB(object):
    _tables = None

    def __init__(self):
        self._tables = {}

    def create_table(self, name):
        # TODO check if table exists first
        table = Table()
        self._tables[name] = table
