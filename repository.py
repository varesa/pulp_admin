import json

from pulp_connection import PulpConnection
from importer import Importer

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
