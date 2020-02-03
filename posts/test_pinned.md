title: test pinned post
date: 2020-01-20
pinned: True
tags: ["test", "tag2"]

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

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