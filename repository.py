import json

from pulp_connection import PulpConnection
from importer import Importer
from distributor import Distributor

class Repository:

    id = None
    """:type: string"""
    display_name = None
    """:type: string"""
    description = None
    """:type: string"""
    notes = {}

    content_unit_counts = {}
    last_unit_added = None
    """:type: string"""
    last_unit_removed = None
    """:type: string"""

    _ns = None
    """:type: string"""
    _href = None
    """:type: string"""
    _id = {}

    connection = None
    """:type: PulpConnection"""

    def __init__(self, data, connection):
        self.id = data['id']
        self.display_name = data['display_name']
        self.description = data['description']
        self.notes = data['notes']

        self.content_unit_counts = data['content_unit_counts']
        self.last_unit_added = data['last_unit_added']
        self.last_unit_removed = data['last_unit_removed']

        self._ns = data['_ns']
        self._id = data['_id']
        self._href = data['_href']

        self.connection = connection

    def get_importers(self):
        result = self.connection.get(self._href + "/importers/")
        importers = []
        for importer in json.loads(result.text):
            importers.append(Importer(importer, self.connection))
        return importers

    def get_importer(self, id):
        result = self.connection.get(self._href + "/importers/" + id + "/")
        importer = json.loads(result)
        return Importer(importer, self.connection)

    def get_distributors(self):
        result = self.connection.get(self._href + "/distributors/")
        distributors = []
        for distributor in json.loads(result.text):
            distributors.append(Distributor(distributor, self.connection))
        return distributors

    def get_distributor(self, id):
        result = self.connection.get(self._href + "/distributors/" + id + "/")
        distributor = json.loads(result)
        return Distributor(distributor, self.connection)

    def sync(self):
        result = self.connection.post(self._href + "/actions/sync/")
        if result.status_code == 202:
            print("Repo id " + str(id) + " successfully scheduled for syncing")
        else:
            print("Unable to schedule repo id " + str(id) + " for syncing")
    
    def dump(self):
        out =  "- id: " + str(self.id) + "\n"
        out += "- display name: " + str(self.display_name) + "\n"
        out += "- description: " + str(self.description) + "\n"
        out += "- notes: " + str(self.notes) + "\n"
        out += "\n"
        out += "- content units: " + str(self.content_unit_counts) + "\n"
        out += "- last added: " + str(self.last_unit_added) + "\n"
        out += "- last removed: " + str(self.last_unit_removed) + "\n"
        out += "\n"
        out += "- _id: " + str(self._id) + "\n"
        out += "- _ns: " + str(self._ns) + "\n"
        out += "- _href: " + str(self._href) + "\n"

        return out
