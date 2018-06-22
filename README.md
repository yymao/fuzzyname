# fuzzyname
A simple python class for fuzzy name matching, especially in academic settings.

## Installation
```sh
pip install fuzzyname
```

## Examples
```python
from fuzzyname import Name

Name('Vanessa T. Porter') == Name('V. T. Porter')
Name('Vanessa T. Porter') == Name('V. Porter')
Name('Vanessa Teresa Porter') == Name('V. T. Porter')
Name('Vanessa Porter') == Name('V. Porter')
Name('Porter, V.') == Name('V. T. Porter')
Name('Phil Porter') == Name('Philip Porter')
Name('Benjamin Porter') == Name('Ben Porter')
Name('Yessica van de Langenberg') == Name('van de Langenberg, Y.')
Name('Li Qin Ho') == Name('Li-Qin Ho')
Name('Li Qin Ho') == Name('L.-Q. Ho')
Name('Li Qin Ho', exact=True) == Name('L. Q. Ho')
Name('Vanessa Teresa Porter') != Name('V. R. Porter')
Name('Vanessa Porter') != Name('Violet Porter')
Name('Li Qin Ho', exact=True) != Name('L. Ho')
Name('Li Qin Ho', exact=True) != Name('Li Qi Ho')
```