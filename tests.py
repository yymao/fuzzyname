from fuzzyname import Name

def test_fuzzyname():
    assert Name('Vanessa T. Porter') == Name('V. T. Porter')
    assert Name('Vanessa T. Porter') == Name('V. Porter')
    assert Name('Vanessa Teresa Porter') == Name('V. T. Porter')
    assert Name('Vanessa Porter') == Name('V. Porter')
    assert Name('Porter, V.') == Name('V. T. Porter')
    assert Name('Phil Porter') == Name('Philip Porter')
    assert Name('Benjamin Porter') == Name('Ben Porter')
    assert Name('Yessica van de Langenberg') == Name('van de Langenberg, Y.')
    assert Name('Li Qin Ho') == Name('Li-Qin Ho')
    assert Name('Li Qin Ho') == Name('L.-Q. Ho')
    assert Name('Li Qin Ho', exact=True) == Name('L. Q. Ho')
    assert Name('Vanessa Teresa Porter') != Name('V. R. Porter')
    assert Name('Vanessa Porter') != Name('Violet Porter')
    assert Name('Li Qin Ho', exact=True) != Name('L. Ho')
    assert Name('Li Qin Ho', exact=True) != Name('Li Qi Ho')
