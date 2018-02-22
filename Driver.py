# source data
ATTRIBUTES = "ABCDE"
FDS = {
    "A": "AB",
    "B": "C",
    "D": "AE"
}

import copy
import Relation

# the main algorithms
# all AttributeSet used in this class are bounded by the ATTRIBUTES array
class Algorithms(object):
    
    def __init__(self):
        self._relation = Relation(ATTRIBUTES, FDS)
    
    def _attribute_closure(attrs):
        """
        attrs: AttributSet
        returns: AttributeSet that contains all derived attributes
        """
        result = copy.deepcopy(attrs)
        tmp = set()
        # halt when no more attributes are added
        while result.attrs() != tmp:
            tmp = result.attrs()
            for fd in self._relation.fds():
                if fd.lhs().issubset(result.attrs()):
                    # if A->B and A in attrs, add B to attrs
                    result.union(fd.lhs())
        return result

    def is_super_key(self, keyA, keyB):
        """
        keyA: AttributeSet
        keyB: AttributeSet
        check whether keyA is a super key of keyB
        """
        return self._attribute_closure(keyB) == keyA

