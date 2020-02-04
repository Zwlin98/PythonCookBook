# Create by Zwlin
s = '{name} has {n} messages'

print(s.format(name='Zwlin', n=100))

name = 'Zwlin'
n = 100

print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


info = Info(name, n)

print(s.format_map(vars(info)))


class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n

print(s.format_map(safesub(vars())))
