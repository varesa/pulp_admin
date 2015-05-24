class Distributor:
    id = None
    repo_id = None
    distributor_type_id = None

    config = {}
    scratchpad = None

    auto_publish = None
    scheduled_publishes = None
    last_publish = None

    _id = {}
    _ns = None

    connection = None

    def __init__(self, data, connection):
        self.id = data['id']
        self.repo_id = data['repo_id']
        self.distributor_type_id = data['distributor_type_id']

        self.config = data['config']
        self.scratchpad = data['scratchpad']

        self.auto_publish = data['auto_publish']
        self.scheduled_publishes = data['scheduled_publishes']
        self.last_publish = data['last_publish']

        self._id = data['_id']
        self._ns = data['_ns']

        self.connection = connection

    def dump(self):
        out =  "- id: " + str(self.id) + "\n"
        out += "- repo_id: " + str(self.repo_id) + "\n"
        out += "- importer type id: " + str(self.distributor_type_id) + "\n"
        out += "\n"
        out += "- config: " + str(self.config) + "\n"
        out += "- scratchpad: " + str(self.scratchpad) + "\n"
        out += "\n"
        out += "- auto publish: " + str(self.auto_publish) + "\n"
        out += "- scheduled syncs: " + str(self.scheduled_publishes) + "\n"
        out += "- last sync: " + str(self.last_publish) + "\n"
        out += "\n"
        out += "- _id: " + str(self._id) + "\n"
        out += "- _ns: " + str(self._ns) + "\n"

        return out
