"""Objekty, proměnné a data v programu jsou dočasně uloženy v operační paměti (RAM). Po skončení programu zmizí. Cílem Serializace je uložit existující objekt ve standardizovaném formátu do trvalé paměti - do souboru nebo databáze například.

"""

"""Nejjednodušším způsobem serializace je použití modulu pickle. Ten převede libovolný objekt na sérii bajtů. Tuto sekvenci bajtů lze někam poslat nebo uložit a později rekonstruovat a vytvořit nový objekt se stejnými vlastnostmi."""

"""Modul pickle serializace"""
import pickle

data = {
    'a': [1, 2.0, 3, 4 + 6j],
    'b': ("Alice has a cat", "Python programming is great"),
    'c': [False, True, False]
}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

"""Modul pickle deserializace"""

import pickle

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)
