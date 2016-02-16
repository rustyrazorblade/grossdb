
class Row(object):
    _data = {}

    def __init__(self, **values):
        self._data = values

    def __getitem__(self, item):
        return self._data[item]
