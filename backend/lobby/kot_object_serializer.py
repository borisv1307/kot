import json


class KOTObjectSerializer(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'serialize_kot_obj'):
            return o.serialize_kot_obj()
        else:
            raise TypeError('Object of type {} is not serializable through KOT serializer'.format(type(o)))
