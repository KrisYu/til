# Python get all permutations of numbers

[Python get all permutations of numbers](https://stackoverflow.com/questions/2052951/python-get-all-permutations-of-numbers)

```
from itertools import permutations
res = [a for a in permutations([7, 11, 4])]

for v in res:
	print(v[0], v[1], v[2])
```