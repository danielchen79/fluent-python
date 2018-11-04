from collections import abc
import keyword

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
    <class 'explore2.FrozenJSON'>
    >>> talk.name
    'There *Will* Be Bugs'
    >>> talk.speakers
    [3471, 5199]
    >>> grad = FrozenJSON({'name': 'Jim Bo', 'class': 1982})
    >>> grad.class_
    1982
    >>> type(feed.Schedule.conferences[0])
    <class 'explore2.FrozenJSON'>
    >>> sorted(feed.Schedule.conferences[0].keys())
    ['serial']
    >>> feed.Schedule.conferences[0].serial
    115
    '''
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            # getattr return not only value attributes, but methods
            return getattr(self.__data, name)
            # return self.__data.name
        else:
            return FrozenJSON(self.__data[name])
