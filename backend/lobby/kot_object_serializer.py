import json


class KOTObjectSerializer(json.JSONEncoder):
    """
    Allows custom KOT objects to be stuffed into database (hopefully)
    to make a complex object serializable, add a serialize_kot_obj method to define the JSON results
    """

    def default(self, o):
        if hasattr(o, 'serialize_kot_obj'):
            return o.serialize_kot_obj()
        else:
            raise TypeError('Object of type {} is not serializable through KOT serializer'.format(type(o)))
