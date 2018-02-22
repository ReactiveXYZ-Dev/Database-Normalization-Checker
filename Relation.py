import AttributeSet, FD

class Relation(object):
    
    def __init__(self, attrs, fds):
        """
        attrs: string
        fds: functional dependencies in object form
        """
        self._attrs = AttributeSet(attrs)
        self._fds = set()
        for lhs, rhs in fds.items():
            self._fds.add(FD(lhs, rhs))
    
    def attrs(self):
        return self._attrs

    def fds(self):
        return self._fds