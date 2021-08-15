class Cookie(object):
    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return 'Cookie(%r, %r)' % (self.name, self.timestamp.date())

    def __str__(self):
        return 'Cookie(%r, %r)' % (self.name, self.timestamp.date())
