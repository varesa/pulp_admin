import json
from repository import Repository

class Pulp():
    def __init__(self, connection):
        self.connection = connection

    def get_repositories(self):
        result = self.connection.get("/pulp/api/v2/repositories/")
        repositories = []
        for repo in json.loads(result.text):
            repositories.append(Repository(repo, self.connection))
        return repositories
    
    def get_repository(self, repo_id):
        """
        :param repo_id:  Repository id
        :type repo_id: string
        :rtype: Repository
        """
        result = self.connection.get("/pulp/api/v2/repositories/" + str(repo_id) + "/")
        repo = json.loads(result.text)
        return Repository(repo, self.connection)

    def create_repository(self, id, display_name, description, feed):
        if not len(id):
            raise ValueError("Invalid ID")
        data = {}
        data['id'] = id
        if len(display_name):
            data['display_name'] = display_name
        if len(description):
            data['description'] = description
        if len(feed):
            data['importer_type_id'] = "yum_importer"
            data['importer_config'] = {'feed': feed, 'validate': True, 'retain_old_count': 1}

            url = '/' + '/'.join(feed.split('/')[3:])
        else:
            url = '/' + id + '/'

        data['distributors'] = [{'distributor_id': 'yum_distributor',
                                 'distributor_type_id': 'yum_distributor',
                                 'distributor_config': {'http': False, 'https': True,
                                                        'relative_url': url, 'checksum_type': 'sha256'},
                                 'auto_publish': True
                                }]

        result = self.connection.post("/pulp/api/v2/repositories/", json.dumps(data))
        print(result.status_code)
        print(result.text)
