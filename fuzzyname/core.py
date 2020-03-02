"""
fuzzyname: for better name comparison
"""

import re

try:
    from unidecode import unidecode
except ImportError:
    _HAS_UNIDECODE = False
else:
    _HAS_UNIDECODE = True

from .nickname import nicknames

__all__ = ["Name", "FuzzyName"]

_re_template = r"(^[a-z,]*(?:,|^){}(?:,|$)[a-z,]*$)"


class Name(object):
    """
    Parameters
    ----------
    name: string
    exact: bool, optional
    """

    def __init__(self, name, exact=False, use_unidecode=True):
        if use_unidecode:
            if not _HAS_UNIDECODE:
                raise RuntimeError(
                    "Cannot import unidecode package. Please install unidecode or set `use_unidecode` to False."
                )
            self.name = unidecode(name)
        else:
            self.name = name

        self.name = self.name.strip()
        if "," in self.name:
            self.name = "{0[1]} {0[0]}".format(self.name.split(","))

        self.name = self.name.strip()
        self.names = tuple(
            (
                n.lower()
                for n in self.name.replace("-", " ").replace(".", ". ").split()
                if n != "."
            )
        )
        assert self.names, "*name* must not be empty"
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

        s = slice(None, None if i is None else -i)  # pylint: disable=E1130

        j = None
        for j, (a, b) in enumerate(zip(self.names[s], other.names[s])):
            if a == b:
                continue

            if exact and not (a.endswith(".") or b.endswith(".")):
                return True

            a = a.rstrip(".")
            b = b.rstrip(".")
            if not (a.startswith(b) or b.startswith(a)):
                # check nicknames
                if len(a) > 1 and len(b) > 1:
                    for m in re.findall(_re_template.format(a), nicknames, re.M):
                        if b in m.split(","):
                            break
                    else:
                        return True
                else:
                    return True

        s = slice(
            j if j is None else j + 1, i if i is None else -i  # pylint: disable=E1130
        )

        for n in (self.names, other.names):
            n = n[s]
            if n and not all(a.endswith(".") for a in n):
                return True

        return False


FuzzyName = Name
