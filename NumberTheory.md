## Greatest Commom Divisor (GCD) of two numbers a, b

- One can use python built-in function: ```math.gcd(a,b)```
- or use the following code

```python
def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a 
```

## Least Common Multiple (LCM) of two numbers a, b

lcm(a, b) = a * b / gcd(a, b)

## Properties of GCD of all numbers starting from A[i] until A[N]
    for fixed index i, the value of GCD(i, j) will be decreasing 
    as GCD(i, j) >= GCD(i, j + 1). Also, because GCD(i, j + 1) must 
    be equal or divisor of GCD(i, j), the number of distinct value X 
    of GCD(i, j), GCD(i, j + 1), ..., GCD(i, N) will satisfies 2^X <= A[i].
    or X <= log2(A[i])


## Test whether a number is prime

```python

import math

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for divisor in range(2, math.floor(math.sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True

```

## Find all primes less than or equal to n

- the code implements Sieve of Eratosthenes algorithm

```python

import math

def sieve(n):
    A = [i for i in range(n+1)]
    A[1] = 0
    for p in range(2, math.floor(math.sqrt(n))+1):
        if A[p]:
            j = p*p
            while j <= n:
                A[j] = 0
                j += p
    L = []
    for p in range(2, n+1):
        if A[p]:
            L.append(A[p])
    return L


```

## Find all distinct primes (a set) which are factors of m

```python
import math

def primes_set(m):
    if m == 1: return set()
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return primes_set(m//i) | set([i])
    return set([m])
```


## Find all primes (there could be duplicates, so it is a list) which are factors of m

```python
import math

def primes_list(m):
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return primes_list(m//i) + [i]
    return [m]
```

## Find the result of (a/b) % m where m is a primer number 
   use Euler's theorem where (1/b) % m = b ^ (m-2) % m

```python

   res = a * pow(b, m-2, m) % m
```

or use *Extended Euclidean algorithm*

```python
def inverse(a, m):
    t, r = 0, m
    newt, newr = 1, a 
    while newr != 0:
        q = r // newr
        t  = newt
        newt = t - q*newt
        r  = newr
        newr = r - q*newr
    if r > 1: return -1 # a is not invertible
    if t < 0:
        t += m
    return t
```

## 同余
  - 两个数 x 和 y，如果 (x−y) mod m = 0，则称 x 与 y 对模 m 同余，记作
             x ≡ y (mod m)
    例如 42≡12(mod10)，−17≡3(mod10)。
  - 处理取模的小技巧
     - 如果 x 和 y 均为非负数，则 x ≡ y (mod m) 相当于 
           x mod m = y mod m

       如果 x<0，y≥0，则 x ≡ y (mod m) 相当于 
           x mod m + m = y mod m

       例如 −17 mod 10 + 10 = −7 + 10 = 3。

       为了避免判断 x 是否为负数，等号左边可以写成 
           (x mod m + m ) mod m

       这样无论 x 是否为负数，运算结果都会落在区间 [0,m) 中。

       注：Python 用户可以忽略，取模运算会保证结果非负。

## Find a big decimal number 's modular of k: n % k
  - If ```n``` is very big and has to be constructed incrementally digit by digit, 
    the final result of ```n%k``` can also be obtained incrementally, that is
    ```python
    res = 0
    for d in digits:
        res = (res*10 + d) % k
    return res
    ```



     











