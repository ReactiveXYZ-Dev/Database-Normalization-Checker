class AttributeSet(object):
    
    def __init__(self, attrs):
        """
        attrs: string
        """
        this._attrs = set(attrs)

    def attrs(self):
        return self._attrs

    def union(self, attrs):
        self._attrs = self._attrs.union(attrs)

    def __eq__(self, other):
        return self._attrs == other.attrs()