def averager(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)


def averager_coroutine():
    sum = 0
    print("routine started")
    x = yield "do this first before input"
    while x:
        for i in averager_coroutine():
            sum += i
            x = yield sum / len(i)
            
g = averager_coroutine()
next(g)

g.send(1)

""" CHATGPT LØSNING 
def averager():
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        total += value
        count += 1
        average = total / count
        
"""
