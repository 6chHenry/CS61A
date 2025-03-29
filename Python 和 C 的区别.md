​                                              *Python 和 C 的区别*

1.Py没有分号 C有分号

2.Py不用定义**变量与函数**类型 C需要提前定义类型（int，char等）

3.Py：

```python
def main():
    cough(3)
def cough(n):
    n=3
    for i in range(n):
        print("cough")  #自动包含换行
main()
```

 

C:

```c
#include <stdio.h>
void cough(int n);
int main()
{
    cough(3);
    return 0;
}
void cough(int n)
{
    for(int i=0;i<n;i++)
    {
        printf("cough\n");  //不包含空行 需要自己添加\n
    }
}
```

