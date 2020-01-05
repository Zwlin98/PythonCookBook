from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


# Example use
yahoo = UrlTemplate('https://finance.yahoo.com/d/quotes.csv?s={name}&f={field}')

for line in yahoo.open(names='IBM,AAPL,FB', field='sl1c1v'):
    print(line.decode('utf-8'))


# can be replaced by

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


# Example use
yahoo = urltemplate('https://finance.yahoo.com/d/quotes.csv?s={name}&f={field}')

for line in yahoo(names='IBM,AAPL,FB', field='sl1c1v'):
    print(line.decode('utf-8'))
