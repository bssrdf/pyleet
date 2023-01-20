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





