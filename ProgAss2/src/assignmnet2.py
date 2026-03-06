

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
                to_remove = q.pop(0)
                hold.remove(to_remove)
            q.append(r)
            hold.add(r)


def LRU(k, m, requests):
    pass
    
def OPTFF(k, m, requests):
    pass
    
