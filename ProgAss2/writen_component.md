##Question 1:
| Input File | k | m | FIFO | LRU | OPTFF |
|---|---|---|---|---|---|
| Test 5 | 3 | 50 | 31 | 31 | 34 |
| Test 6 | 6 | 50 | 50 | 50 | 45 |
| Test 7 | 4 | 50 | 50 | 50 | 16 |

-1 OPTFF generally misses less than FIFO and LRU (it sometimes misses an equal amount as these two), notably because it is an offline algorithm, and 
therefore has access ot information that the other two algoritms do not at the beginning of runtime.
-2 With the datasets run in this trial, they both missed an equal amount of times; however, I would imagine that there are some datasets that FIFO 
would be more optimal for, and other datasets that LRU would be better with. I do think LRU would have a slight edge for the majority of datasets.

##Question 2:
-1 We will use the string "ABCDBEACDA" as an example for OPTFF having strictly less misses than LRU. OPTFF will have 6 misses while LRU will have 9 
misses. This is because LRU is bounded soley by the characters that have already been seen in the past while OPTFF can drop a very recently used letter
from its cache immediatly if that character is never used again (we can use the fifth 'B' as an example). When looking at the 6th character 'E', it is 
evident that there are no more Bs later in the sequence so we drop B from the cache in order to add E with OPTFF. However, when using LRU, we would 
actually drop C once we get to the 6th position because it's the least recently used, despite 'C' saving us from another cache miss in the third to last
position.

##Question 3:
