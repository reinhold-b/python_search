pythonsearch package
====================


Pythonsearch is a package containing popular searching algorithms, which can be **quickly** implemented for various projects to save coding time for more important things! 

Recently I got really interested in searching algorithms and decided to code a Python solution, which allows users to quickly implement the algorithms listed below:
* Linear Search
* Bilinear Search
* Binary Search
* Jump Search
* Interpolation Search

Searching algorithms are used in almost every application and can be fun to play around with so feel free to try out this pythonsearch!

Install
--------------

To install the package just run `pip install pythonsearch` in your shell!
After that you can `import pythonsearch` in your Python program and start coding.
Currently there are five searching algorithms available, which are listed above.

Use
---

```
from pythonsearch.search import linear_search

array_one = [8, 2, 9, 10, 34]

#index of element 10
index_10 = linear_search(array, 10)

print(index_10)

```
Output: `3`

**Pythonsearch also works with strings:**

```
array_two = ["Max", "Paul", "Mary, "Julia"]

#index of element "Julia"
index_Julia = linear_search(array, "Julia")

print(index_Julia)
```
Output: `3`

Functionality
-------------
| Algorithm     | Needs sorted array           | Speed  |
| ------------- |:-------------:| -----:|
| linear_search     | no| relatively slow |
| bilinear_search    | no      |   relatively slow |
| binary_search | yes     |  fast |
| jump_search     | yes | medium |
| interpolation_search    | yes    |   fast |

`linear_search` is also reversable: `linear_search(array, x, reversed=True)`.
