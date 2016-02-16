import logging
logger = logging.getLogger(__name__)

class Table(object):
    _rows = None
    _indexes = None
    _name = None
    _total = 0

    def __init__(self, name):
        self._rows = {}
        self._name = name
        self._indexes = {}


    def add_field(self, name, type):
        pass


    def insert(self, row):
        # TODO schema validation
        record_id = self._total + 1
        self._rows[record_id] = row
        self._total += 1




