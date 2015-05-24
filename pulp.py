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
        result = self.connection.get("/pulp/api/v2/repositories/" + str(repo_id) + "/")
        repo = json.loads(result.text)
        return Repository(repo, self.connection)
