#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу

garden_set = set(garden)
meadow_set = set(meadow)
#print(meadow_set)

# выведите на консоль все виды цветов
all_of_flowers = garden_set | meadow_set
print(all_of_flowers)
# выведите на консоль те, которые растут и там и там
piece_of_both = garden_set & meadow_set
print(piece_of_both)
# выведите на консоль те, которые растут в саду, но не растут на лугу
garden_without_meadow = garden_set - meadow_set
print(garden_without_meadow)
# выведите на консоль те, которые растут на лугу, но не растут в саду
meadow_without_garden = meadow_set - garden_set
print(meadow_without_garden)