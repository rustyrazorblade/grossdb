
class Results(object):
    _total = None
    _rows = None

    # TODO track schema of results
    def __init__(self):
        self._total = 0
        self._rows = []

    def __len__(self):
        return self._total

