# Create by Zwlin
parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print(' '.join(parts))

data = ['ACME', 50, 91.1]

print(','.join(str(d) for d in data))

print('a','b','c',sep=":")

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

print(' '.join(sample()))

def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size+=len(part)
        if size>maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(),2):
    print(part)