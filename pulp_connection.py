import requests

class PulpConnection:
    def __init__(self, auth, ca=None):
        self.url = "https://pulp.ikioma"
        self.auth = auth
        if ca is None:
            self.ca = "/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem"
        else:
            self.ca = ca

    def get(self, path):
        return requests.get(self.url+path, auth=self.auth, verify=self.ca)

    def put(self, path, data=None):
        return requests.put(self.url+path, data=data,  auth=self.auth, verify=self.ca)

    def post(self, path, data=None):
        return requests.post(self.url+path, data=data, auth=self.auth, verify=self.ca)

    def delete(self, path):
        return requests.delete(self.url+path, auth=self.auth, verify=self.ca)
