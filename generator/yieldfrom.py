def g(x):
    yield from range(x, 0, -1)
    yield from range(x)


# print(list(g(5)))

def accumulate():
    tally = 0
    while True:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while True:
        tally = yield from accumulate()
        tallies.append(tally)


tallies = []
acc = gather_tallies(tallies)
next(acc)
for i in range(4):
    acc.send(i)

acc.send(None)

for i in range(5):
    acc.send(i)

acc.send(None)

print(tallies)
