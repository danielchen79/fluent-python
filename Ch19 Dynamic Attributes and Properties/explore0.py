from collections import abc

class FrozenJSON:
    '''
    >>> from osconfeed import load
    >>> raw_feed = load()
    >>> feed = FrozenJSON(raw_feed)
    >>> len(feed.Schedule.speakers)
    357
    >>> sorted(feed.Schedule.keys())
    ['conferences', 'events', 'speakers', 'venues']
    >>> for key, value in feed.Schedule.items():
    ...     print("{:3} {}".format(len(value), key))
      1 conferences
    494 events
    357 speakers
     53 venues
    >>> feed.Schedule.speakers[-1].name
    'Carina C. Zona'
    >>> talk = feed.Schedule.events[40]
    >>> type(talk)
    <class 'explore0.FrozenJSON'>
    >>> talk.name
    'There *Will* Be Bugs'
    >>> talk.speakers
    [3471, 5199]
    '''
    def __init__(self, mapping):
        # Has to be __data, but not __dict__
        # __dict__ stores the object's writable attributes
        # seld.__dict__.Schedule gets the dictionary, and doesn't invoke
        # __getattr__
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            # getattr return not only value attributes, but methods
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
