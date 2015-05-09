#!/bin/env python3

import getpass

import requests
import json

class Auth():
	def __init__(self):
		self.username = ""
		self.password = ""
	def init(self):
		self.username = input("Username?\n> ")
		self.password = getpass.getpass("Password?\n> ")
	
	def get_tuple(self):
		return self.username, self.password

class PulpConnection():
	def __init__(self, auth=None):
		self.url = "https://pulp.ikioma"
		self.auth = auth

	def get(self, path):
		return requests.get(self.url+path,auth=self.auth,verify="/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem")

	def post(self, path, data=None):
		return requests.post(self.url+path, data=data, auth=self.auth, verify="/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem")

class Pulp():
	def __init__(self, connection):
		self.connection = connection

	def get_repositories(self):
		result = self.connection.get("/pulp/api/v2/repositories/")
		return json.loads(result.text)
	
	def get_repository(self, id):
		result = self.connection.get("/pulp/api/v2/repositories/" + str(id) + "/")
		return json.loads(result.text)

	def get_importers(self, repo_id):
		result = self.connection.get("/pulp/api/v2/repositories/" + str(repo_id) + "/importers/")
		return json.loads(result.text)

	def get_distributors(self, repo_id):
		result = self.connection.get("/pulp/api/v2/repositories/" + str(repo_id) + "/distributors/")
		return json.loads(result.text)

	def sync_repository(self, id):
		result = self.connection.post("/pulp/api/v2/repositories/" + str(id) + "/actions/sync/")
		if result.status_code == 202:
			print("Repo id " + str(id) + " succesfully scheduled for syncing")
		else:
			print("Unable to schedule repo id " + str(id) + " for syncing")

def pick_repo(pulp, multiple=False):
	repos = pulp.get_repositories()
	i = 1
	for repo in repos:
		print(str(i) + ") " + str(repo['display_name']))
		i = i + 1
	
	selection = input('>')
	if multiple:
		ids = []
		for num in selection.split(' '):
			ids.append(repos[int(num)-1]['id'])
		return ids
	else:
		return repos[int(selection)-1]['id']

def repos_overview(pulp):
	repos = pulp.get_repositories()
	for repo in repos:
		print(repo['display_name'] + ':')
		print('\t' + str(repo['content_unit_counts']['rpm']) + " rpms")
		print('\t' + "last added: " + repo['last_unit_added'])

def repos_details(pulp):
	id = pick_repo(pulp)
	print("Repository details:")
	print(json.dumps(pulp.get_repository(id), indent=4))
	print("\nRepository importers:")
	print(json.dumps(pulp.get_importers(id), indent=4))
	print("\nRepository distributors:")
	print(json.dumps(pulp.get_distributors(id), indent=4))

def repos_sync(pulp):
	ids = pick_repo(pulp, multiple=True)
	for id in ids:
		pulp.sync_repository(id)


def mainmenu(pulp):
	while True:
		print("1) Repository overview")
		print("2) Repository details")
		print("3) Start sync")

		print("q) Quit")

		selection = input("> ")
		if selection == '1':
			repos_overview(pulp)
		elif selection == '2':
			repos_details(pulp)
		elif selection == '3':
			repos_sync(pulp)
		
		elif selection == 'q':
			break

		else:
			print("Invalid selection")

auth = Auth()
auth.init()

pulp = Pulp(PulpConnection(auth=auth.get_tuple()))

mainmenu(pulp)
#pick_repo(pulp)

