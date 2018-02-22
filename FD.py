import AttributeSet

class FD(object):
    
    def __init__(self, lhs, rhs):
        """
        lhs: string
        rhs: strinf
        """
        this._lhs = AttributeSet(lhs)
        this._rhs = AttributeSet(rhs)
    
    def lhs(self):
        return self._lhs
    
    def rhs(self):
        return self._rhs