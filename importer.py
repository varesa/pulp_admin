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