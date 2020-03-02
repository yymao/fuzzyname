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
        self.name = name

        if use_unidecode:
            if not _HAS_UNIDECODE:
                raise RuntimeError(
                    "Cannot import unidecode package. Please install unidecode or set `use_unidecode` to False."
                )
            name = unidecode(name)

        name = re.sub(r"[^a-z-,.\s]", "", name.strip().lower())

        if "," in name:
            name = "{0[1]} {0[0]}".format(name.split(",")).strip()

        self.names = tuple(
            (n for n in name.replace("-", " ").replace(".", ". ").split() if n != ".")
        )

        if not self.names:
            raise ValueError("`name` must not be empty")

        self.exact = bool(exact)
        self.normalized_name = " ".join(self.names)

    def __repr__(self):
        return repr(self.name)

    def __str__(self):
        return str(self.name)

    def __eq__(self, other):
        return not self.__ne__(other)

    def __ne__(self, other):
        if self.normalized_name == other.normalized_name:
            return False

        exact = self.exact or other.exact

        if exact and len(self.names) != len(other.names):
            return True

        if (
            not exact
            and (
                self.normalized_name in other.normalized_name
                and " " in self.normalized_name
            )
            or (
                other.normalized_name in self.normalized_name
                and " " in other.normalized_name
            )
        ):
            return False

        matched_back = 0
        for a, b in zip(reversed(self.names), reversed(other.names)):
            if a == b:
                matched_back += 1
            else:
                break

        s = slice(None, -matched_back if matched_back else None)
        matched_front = 0
        for a, b in zip(self.names[s], other.names[s]):
            if a == b:
                matched_front += 1
                continue

            a = a.rstrip(".")
            b = b.rstrip(".")
            initials = len(a) == 1 or len(b) == 1

            if exact and not initials:
                return True

            if not (a.startswith(b) or b.startswith(a)):
                if initials:
                    return True
                else:  # check nicknames
                    for m in re.findall(_re_template.format(a), nicknames, re.M):
                        if b in m.split(","):
                            break
                    else:
                        return True

            matched_front += 1

        matched = matched_front + matched_back
        if matched < max(2, min(len(self.names), len(other.names))):
            s = slice(matched_front, -matched_back if matched_back else None)
            for n in (self.names, other.names):
                n = n[s]
                if n and not all(len(a.rstrip(".")) == 1 for a in n):
                    return True

        return False


FuzzyName = Name
