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