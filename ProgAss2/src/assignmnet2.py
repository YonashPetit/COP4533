import heapq
from collections import deque, defaultdict

class Node:
    def __init__(self, data):
        self.data = data  
        self.prev = None
        self.next = None

def FIFO(k, m, requests):
    hit, miss = 0, 0
    q = []
    hold = set()
    for r in requests:
        if r in hold:
            hit += 1
        else:
            miss += 1
            if len(q) == k:
                to_remove = q.pop(0) #pretend this is a queue using a q library
                hold.remove(to_remove)
            q.append(r)
            hold.add(r)

def LRU(k, m, requests):
    hit, miss, size = 0, 0, 0
    back, start = Node(None), Node(None)
    back.next = start
    start.prev = back
    hold = {"start": start, "back": back}
    
    for r in requests:
        if r in hold:
            hit += 1
            #get rid of old position
            behind, forward = hold[r].prev, hold[r].next
            behind.next, forward.prev = forward, behind
            del hold[r]
        else:
            miss += 1
            size += 1
            if size > k:
                size -= 1
                secondary = hold["back"].next
                hold["back"].next = secondary.next
                secondary.next.prev = hold["back"]
                del hold[secondary.data]

                
        #put new position right behind start
        hold[r] = Node(r)
        secondary = hold["start"].prev
        secondary.next = hold[r]
        hold[r].prev = secondary
        hold["start"].prev = hold[r]
        hold[r].next = hold["start"]
          
def OPTFF(k, m, requests):
    cache = set()
    heap = []
    hit, misses = 0, 0
    
    #to make item -> array of index where it occur pair
    fut_idx = defaultdict(deque)
    for idx, item in enumerate(requests):
        fut_idx[item].append(idx)

    for i, item in enumerate(requests):
        fut_idx[item].popleft()
        if fut_idx[item]:
            next_idx = fut_idx[item][0]  
        else:
            next_idx = float('inf')
    
        #update to next closest idx of same item if we hit
        if item in cache:
            hit += 1
            heapq.heappush(heap, (-next_idx, item))
        else:
            misses += 1
            if len(cache) >= k:
                #we pop  the items with the furthest next_idx until we pop one that's in the cache
                while True:
                    furthest_idx, victim = heapq.heappop(heap)
                    if victim in cache: # Check for stale heap entries
                        cache.remove(victim)
                        break
            
        # INSERT
        cache.add(item)
        heapq.heappush(heap, (-next_idx, item))
    
