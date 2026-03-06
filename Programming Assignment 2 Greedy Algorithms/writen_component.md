## Question 1:
| Input File | k | m | FIFO | LRU | OPTFF |
|---|---|---|---|---|---|
| Test 5 | 3 | 50 | 31 | 31 | 34 |
| Test 6 | 6 | 50 | 50 | 50 | 45 |
| Test 7 | 4 | 50 | 50 | 50 | 16 |

- OPTFF generally misses less than FIFO and LRU (it sometimes misses an equal amount as these two), notably because it is an offline algorithm, and 
therefore has access ot information that the other two algoritms do not at the beginning of runtime.

- With the datasets run in this trial, they both missed an equal amount of times; however, I would imagine that there are some datasets that FIFO 
would be more optimal for, and other datasets that LRU would be better with. I do think LRU would have a slight edge for the majority of datasets.

## Question 2:
- We will use the string "ABCDBEACDA" as an example for OPTFF having strictly less misses than LRU. OPTFF will have 6 misses while LRU will have 9 
misses. This is because LRU is bounded soley by the characters that have already been seen in the past while OPTFF can drop a very recently used letter
from its cache immediatly if that character is never used again (we can use the fifth 'B' as an example). When looking at the 6th character 'E', it is 
evident that there are no more Bs later in the sequence so we drop B from the cache in order to add E with OPTFF. However, when using LRU, we would 
actually drop C once we get to the 6th position because it's the least recently used, despite 'C' saving us from another cache miss in the third to last
position.

## Question 3:
Lets say we have an optimal algo 'A' and let 't' be the first time step where A makes a different eviction choice than OPTFF.
At request A, a miss occurs because the cache is full. Lets say the OPTFF choice is to evict x (the item whose next access is furthest in the future).
Algo A evicts y, and y!=x.

Now, create a new algorithm A′ that behaves exactly like A until t, but evicts x instead of y.
After step t, the cache states are:
C(A)=S∪{x}
C(A′)=S∪{y}
(Where S is the set of other k−1 items they both hold.)

From that, let next(y) be the first time y is requested after t. Because of the nature of OPTFF, we know next(y)≤next(x).
Before next(y), it should be noted that any request for an item in S results in the same outcome for both.
when the next y comes [next(y)]
A has a miss (it evicted y).
A′ has a hit (it kept y).
[OR 
A has a miss (it evicted y).
A` has a miss (it evicted y).
in a different senario where A' evicts y (in this case, niether algorithm has the leg up)]

At time next(y), A′ has one fewer miss than A. A′ can now evict y and bring in whatever A chooses to bring in.
If A evicts x to bring in y, the caches now match perfectly.
If A evicts something else, A′ still has a "credit" of one fewer miss and a cache that is strictly better or equal in utility to A's.

Since A′ incurred ≤ misses than A, and we can repeat this process for every deviation until A becomes OPTFF, so OPTFF must be optimal.