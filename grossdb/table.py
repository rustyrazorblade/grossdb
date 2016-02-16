import logging
logger = logging.getLogger(__name__)

class Table(object):
    _rows = None
    _indexes = None
    _name = None

    def __init__(self, name):
        self._rows = {}
        self._name = name
        self._indexes = {}


