
class Results(object):
    _total = None
    # TODO track schema of results
    def __init__(self):
        self._total = 0

    def __len__(self):
        return self._total
