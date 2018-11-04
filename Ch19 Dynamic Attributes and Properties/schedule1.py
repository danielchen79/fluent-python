import warnings
import osconfeed

DB_NAME = 'schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def load_db(db):
    '''
    >>> import shelve
    >>> db = shelve.open(DB_NAME)
    >>> if CONFERENCE not in db:
    ...     load_db(db)
    >>> event = db["event.33451"]
    >>> type(event)
    <class 'schedule1.Record'>
    >>> event.name, event.event_type
    ('Migrating to the Web Using Dart and Polymer - A Guide for Legacy OOP Developers', '40-minute conference session')
    '''
    raw_data = osconfeed.load()
    warnings.warn("loading " + DB_NAME)
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        # print("record_type:", record_type)
        for record in rec_list:
            key = "{}.{}".format(record_type, record["serial"])
            record["serial"] = key
            # print("serial:", record["serial"])
            db[key] = Record(**record)
