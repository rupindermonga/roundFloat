

class RoundFloatManual(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be a float"
        self.Value = round(val, 2)

    def __str__(self):
        return str(self.Value)