class Schedule:
    _id = None
    ":type: string"

    _href = None
    ":type: string"

    kwargs = None
    ":type: dict"

    enabled = None
    ":type: bool"

    last_updated = None
    ":type: string"

    schedule = None
    ":type: string"

    first_run = None
    ":type: string"

    next_run = None
    ":type: string"

    last_run_at = None
    ":type: string"

    remaining_runs = None
    ":type: ?"

    total_run_count = None
    ":type: int"

    consecutive_failures = None
    ":type: int"

    failure_threshold = None
    ":type: int"

    task = None
    ":type: string"

    resource = None
    ":type: string"

    args = None
    ":type: list"

    def __init__(self, data, connection):
        self._id = data['_id']
        self.kwargs = data['kwargs']
        self.next_run = data['next_run']
        self.enabled = data['enabled']
        self.remaining_runs = data['remaining_runs']
        self.last_run_at = data['last_run_at']
        self._href = data['_href']
        self.last_updated = data['last_updated']
        self.first_run = data['first_run']
        self.task = data['task']
        self.consecutive_failures = data['consecutive_failures']
        self.schedule = data['schedule']
        self.total_run_count = data['total_run_count']
        self.failure_threshold = data['failure_threshold']
        self.resource = data['resource']
        self.args = data['args']

    def dump(self):
        out = "- Schedule: " + self.schedule
        out += ", last run: " + self.last_run_at
        out += ", next run: " + self.next_run
        return out