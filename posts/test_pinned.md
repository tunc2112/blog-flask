title: test pinned post
date: 2020-01-20
pinned: True
category: "test"
tags: ["test", "tag2"]

# Heading 1

## Heading 2

* Item 1

* Item 2
    * Item 2a
    * Item 2b

---

1. Item 1

1. Item 2

1. Item 3
    1. Item 3a
    1. Item 3b

### Heading 3

- *This text will be italic*
- _This will also be italic_
- **This text will be bold**
- __This will also be bold__
- _You **can** combine them_
- Three or more...

---

Hyphens

***

Asterisks

___

Underscores

#### Quotes

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
> 
> Quote level 1
>> Quote level 2
>>> Quote level 3

##### Table

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

###### Latex

- $$x + y = z$$

- $$\int_{0}^{\infty} f(t)dt=F_X(x)$$

###### This a very long heading

Some codes are `here`.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello\n";
    unsigned long long a = {1, 2L, 3UL, 4LL, 5ULL};
    return 0;
}
```

```python
from math import factorial as fact

class Test(object):
    def __init__(self):
        super().__init__()
        self.a = [None, False, True, 0b1, 0o2, 0x3, 4.0, r'[a-z]+']

    def f(self, n):
        return self.a[n % len(self.a)]

if __name__ == '__main__':
    for n in range(100):
        print(n, fact(n))

    s = """
for i in range(100):
    print(i, i + fact(i))
"""
```