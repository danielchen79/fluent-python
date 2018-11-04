from collections import abc

class FrozenJSON:
    '''
    >>> from osconfeed import load
    >>> raw_feed = load()
    >>> feed = FrozenJSON(raw_feed)
    >>> sorted(feed.Schedule.keys())
    >>> event = feed.Schedule
    >>> type(event)
    '''
    def __init__(self, mapping):
        self.__data = dict(mapping)
        # for key, value in dict(mapping).items():
            # print(key)
            # self.__dict__[key] = value
            # print(self.__dict__[key])

    def __getattr__(self, name):
        if hasattr(self.__data, name):
        # if hasattr(self.__dict__, name):
            # getattr return not only value attributes, but methods
            print("hasattr ", getattr(self.__data, name))
            return getattr(self.__data, name)
            # return getattr(self.__dict__, name)
        else:
            print("FrozenJSON.build({})".format(self.__data[name]))
            return FrozenJSON.build(self.__data[name])
            # return FrozenJSON.build(self.__dict__[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

from osconfeed import load
raw_feed = load()
feed = FrozenJSON(raw_feed)
