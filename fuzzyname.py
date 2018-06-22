"""
fuzzyname: for better name comparison
"""

__all__ = ['Name']
__version__ = '0.1.0'

class Name(object):
    """
    Parameters
    ----------
    name: string
    exact: bool, optional
    """
    def __init__(self, name, exact=False):
        self.name = name
        if ',' in name:
            name = '{0[1]} {0[0]}'.format(name.split(','))
        self.names = tuple((n.lower() for n in name.replace('-', ' ').replace('.', '. ').split() if n != '.'))
        assert self.names, '*name* must not be empty'
        self.exact = bool(exact)

    def __repr__(self):
        return repr(self.name)

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return not self.__ne__(other)

    def __ne__(self, other):
        exact = self.exact or other.exact

        if exact and len(self.names) != len(other.names):
            return True

        i = None
        for i, (a, b) in enumerate(zip(reversed(self.names), reversed(other.names))):
            if a != b:
                if not i:
                    return True
                break

        s = slice(None, None if i is None else -i) # pylint: disable=E1130

        j = None
        for j, (a, b) in enumerate(zip(self.names[s], other.names[s])):
            if a == b:
                continue

            if exact and not (a.endswith('.') or b.endswith('.')):
                return True

            a = a.rstrip('.')
            b = b.rstrip('.')
            if not (a.startswith(b) or b.startswith(a)):
                return True

        s = slice(j if j is None else j+1, i if i is None else -i) # pylint: disable=E1130

        for n in (self.names, other.names):
            n = n[s]
            if n and not all(a.endswith('.') for a in n):
                return True

        return False
