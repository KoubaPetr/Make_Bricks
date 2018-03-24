# can I make a line of n inches, if I have infinite amount of bricks of size size_small and size_big?

def achievability(size_small, size_big, n):
    if n%(size_small + size_big) == 0:
        return True
    elif ((n%(size_small + size_big))%size_small == 0 or (n%(size_small + size_big))%size_big == 0):
        return True
    else:
        return False

print(achievability(3,6,21))

# if I have bricks of size 1 in the amount "small" and bricks of size 5 in the amount "big" can I compose the line?

def limited_storage_achievability(small, big, n):
    if small < 0 or big < 0:
        return False
    elif n/5 <= big and n%5 <= small:
        return True
    elif limited_storage_achievability(small-5, big-1, n):
        return True
    else:
        return False

print(limited_storage_achievability(1, 6, 32))