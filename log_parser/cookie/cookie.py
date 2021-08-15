class Cookie(object):
    """
    Object Representation of the Cookie Data
    """
    def __init__(self, name, timestamp):
        """
        Constructor for the Cookie Object
        :param name:  Name of the cookie
        :param timestamp:  Time of usage in UTC format
        """
        self.name = name
        self.timestamp = timestamp

    def __repr__(self):
        return 'Cookie(%r, %r)' % (self.name, self.timestamp.date())

    def __str__(self):
        return 'Cookie(%r, %r)' % (self.name, self.timestamp.date())
