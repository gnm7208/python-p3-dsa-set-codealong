class MySet:
    """A custom Set implementation using a dictionary as backing store."""

    def __init__(self, enumerable=None):
        """Initialize MySet with optional enumerable of values."""
        self.dictionary = {}
        if enumerable is None:
            enumerable = []
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def __str__(self):
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{", ".join(set_list)}}'

    def clear(self):
        self.dictionary.clear()
        return self
