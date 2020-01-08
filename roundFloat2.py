



class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float"
        self.Value = round(val, 2)

    def __str__(self):
        return '%.2f' % self.Value

    __repr__ = __str__