title: test pinned post
date: 2020-01-20
pinned: True
category: "test"
tags: ["test", "tag2"]

# Heading 1

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

## Heading 2

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

### Emoji :joy:

:joy: :smile: :grin:

#### Quotes

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.
> 
> Lorem Ipsum，也称乱数假文或者哑元文本， 是印刷及排版领域所常用的虚拟文字。由于曾经一台匿名的打印机刻意打乱了一盒印刷字体从而造出一本字体样品书，Lorem Ipsum从西元15世纪起就被作为此领域的标准文本使用。它不仅延续了五个世纪，还通过了电子排版的挑战，其雏形却依然保存至今。在1960年代，”Leatraset”公司发布了印刷着Lorem Ipsum段落的纸张，从而广泛普及了它的使用。最近，计算机桌面出版软件”Aldus PageMaker”也通过同样的方式使Lorem Ipsum落入大众的视野。
> 
> 我们为何用它？
> 无可否认，当读者在浏览一个页面的排版时，难免会被可阅读的内容所分散注意力。Lorem Ipsum的目的就是为了保持字母多多少少标准及平均的分配，而不是“此处有文本，此处有文本”，从而让内容更像可读的英语。如今，很多桌面排版软件以及网页编辑用Lorem Ipsum作为默认的示范文本，搜一搜“Lorem Ipsum”就能找到这些网站的雏形。这些年来Lorem Ipsum演变出了各式各样的版本，有些出于偶然，有些则是故意的（刻意的幽默之类的）。

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 
> 
> **Quote level 1**
>
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
>> **Quote level 2**
>>
>> Vel fringilla est ullamcorper eget nulla facilisi etiam. Libero enim sed faucibus turpis in eu. Cursus euismod quis viverra nibh cras pulvinar mattis.
>>> **Quote level 3**
>>> 
>>> Id diam maecenas ultricies mi eget mauris pharetra et ultrices. Mattis pellentesque id nibh tortor id aliquet lectus proin.

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

- $$x^n + y^n = z^n$$

- $$\int_{0}^{\infty} f(t)dt=F_X(x)$$

- Inline \\(E[X] = \int_{0}^{\infty}xf(x)dx\\)

###### This a very long heading

<details><summary>Magic</summary>
<p>
yes, even hidden code blocks!

```python
print("hello world!")
```

</p>
</details>

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