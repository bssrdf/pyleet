Set union `A | B`

Set intersection `A & B`

Set subtraction `A & ~B`

Set negation `ALL_BITS ^ A` or `~A`

Set bit `A |= 1 << bit`

Clear bit `A &= ~(1 << bit)`

Test bit `(A & 1 << bit) != 0`

Extract last bit `A&-A` or `A&~(A-1)` or `x^(x&(x-1))`

Remove last bit `A&(A-1)`

Get all 1-bits `~0`

Get n bits of all 1's `(1<<n)-1`

Most significant distinguishing (msd) index of two numbers: a and b
  `int(floor(math.log(a^b,2)))`
  e.g. a, b = 156, 134, their binary representation is:
  '0010011100' and '0010000110'
  msd = 4 i.e. starting from least significant digit (0-th) on the right, the 
  index where a and b differs at the most significant position is 4
