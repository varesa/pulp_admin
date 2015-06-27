import json
from schedule import Schedule

class Importer:
    id = None
    repo_id = None
    importer_type_id = None

    config = {}
    scratchpad = None

    scheduled_syncs = None
    last_sync = None

    _id = {}
    _ns = None

    connection = None

    def __init__(self, data, connection):
        self.id = data['id']
        self.repo_id = data['repo_id']
        self.importer_type_id = data['importer_type_id']

        self.config = data['config']
        self.scratchpad = data['scratchpad']

        self.scheduled_syncs = data['scheduled_syncs']
        self.last_sync = data['last_sync']

        self._id = data['_id']
        self._ns = data['_ns']

        self.connection = connection

    def get_schedules(self):
        result = self.connection.get("/pulp/api/v2/repositories/" + self.repo_id + "/importers/" + self.id + "/schedules/sync/")
        schedules = []
        for sched in json.loads(result.text):
            schedules.append(Schedule(sched, self.connection))
        return schedules

    def dump(self):
        out =  "- id: " + str(self.id) + "\n"
        out += "- repo_id: " + str(self.repo_id) + "\n"
        out += "- importer type id: " + str(self.importer_type_id) + "\n"
        out += "\n"
        out += "- config: " + str(self.config) + "\n"
        out += "- scratchpad: " + str(self.scratchpad) + "\n"
        out += "\n"
        out += "- scheduled syncs: " + str(self.scheduled_syncs) + "\n"
        out += "- last sync: " + str(self.last_sync) + "\n"
        out += "\n"
        out += "- _id: " + str(self._id) + "\n"
        out += "- _ns: " + str(self._ns) + "\n"

        return out