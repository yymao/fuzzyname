# This Python file uses the following encoding: utf-8

from __future__ import unicode_literals
from fuzzyname import FuzzyName as Name


def test_fuzzyname():
    assert Name("Vanessa T. Porter") == Name("V. T. Porter")
    assert Name("Vanessa T. Porter") == Name("V. Porter")
    assert Name("Vanessa Teresa Porter") == Name("V. T. Porter")
    assert Name("Vanessa Teresa Porter") != Name("V. C. Porter")
    assert Name("Vanessa Teresa Porter") == Name("Teresa Porter")
    assert Name("Vanessa Teresa Porter") == Name("V. Teresa Porter")
    assert Name("Vanessa Teresa Porter") != Name("C. Teresa Porter")
    assert Name("Vanessa Teresa Porter") == Name("Vanessa Teresa")
    assert Name("Vanessa Teresa Porter") == Name("Teresa, Vanessa")
    assert Name("Porter, Vanessa") == Name("Porter, Vanessa T.")
    assert Name("Porter, V. Teresa") == Name("Porter, Teresa")
    assert Name("Vanessa Porter") == Name("V. Porter")
    assert Name("Porter, V.") == Name("V. T. Porter")
    assert Name("Phil Porter") == Name("Philip Porter")
    assert Name("Benjamin Porter") == Name("Ben Porter")
    assert Name("Yessica van de Langenberg") == Name("van de Langenberg, Y.")
    assert Name("Li Qin Ho") == Name("Li-Qin Ho")
    assert Name("Li Qin Ho") == Name("L.-Q. Ho")
    assert Name("Li Qin Ho", exact=True) == Name("L. Q. Ho")
    assert Name("Vanessa Teresa Porter") != Name("V. R. Porter")
    assert Name("Vanessa Porter") != Name("Violet Porter")
    assert Name("Li Qin Ho", exact=True) != Name("L. Ho")
    assert Name("Li Qin Ho", exact=True) != Name("Li Qi Ho")
    assert Name("Bill Gates") == Name("William Gates")
    assert Name("Bill Gates", exact=True) != Name("William Gates")
    assert Name("André François") == Name("Andre Francois")
    assert Name("Borgland, Anders W.") == Name("Borgland, Anders")
