import json

class Menu:
    pulp = None
    
    def __init__(self, pulp):
        self.pulp = pulp

    def prompt(self, prompt=None):
        if prompt:
            return input(prompt + "\n> ")
        else:
            return input("> ")

    def pick_repo(self, multiple=False):
        repos = self.pulp.get_repositories()
        i = 1
        for repo in repos:
            print(str(i) + ") " + str(repo.display_name))
            i += 1
        
        selection = input('>')
        if multiple:
            ids = []
            if selection == '*':
                for repo in repos:
                    ids.append(repo.id)
            else:
                for num in selection.split(' '):
                    ids.append(repos[int(num)-1].id)
                return ids
        else:
            return repos[int(selection)-1].id

    def repos_overview(self):
        packages = 0
    
        repos = self.pulp.get_repositories()
        for repo in repos:
            repo = repo
            """:type: Repository"""
            print(repo.display_name + ':')
            if 'rpm' in repo.content_unit_counts.keys():
                print('\t' + str(repo.content_unit_counts['rpm']) + " rpms")
            importers = repo.get_importers()
            if len(importers):
                print('\t' + "last synced: " + str(importers[0].last_sync))
            print('\t' + "last added: " + str(repo.last_unit_added))
    
            if 'rpm' in repo.content_unit_counts.keys():
                packages += repo.content_unit_counts['rpm']
        
        print("\nTotal: " + str(packages) + " rpms in " + str(len(repos)) + " repositories.")
    
    def repos_details(self):
        repo = self.pulp.get_repository(self.pick_repo())
        print("Repository details:")
        print(repo.dump())
        print("\nRepository importers:")
        for importer in repo.get_importers():
            print(importer.dump())
        print("\nRepository distributors:")
        for distributor in repo.get_distributors():
            print(distributor.dump())

    def repos_create(self):
        id = self.prompt("ID:")
        display_name = self.prompt("Display name []:")
        description = self.prompt("Description []:")
        feed = self.prompt("Feed []:")
        self.pulp.create_repository(id, display_name, description, feed)

    
    def repos_sync(self):
        ids = self.pick_repo(self.pulp, multiple=True)
        for id in ids:
            self.pulp.sync_repository(id)
    
    def repos_schedules(self):
        repos = self.pulp.get_repositories()
        for repo in repos:
            importers = repo.get_importers()
            if len(importers):
                print(repo.display_name + ":")
                for importer in importers:
                    for schedule in importer.get_schedules():
                        print(schedule.dump())
    
    def repos_schedules_set(self):
        ids = self.pick_repo(multiple=True)
        schedule = self.prompt("Schedule?")
        for id in ids:
            for importer in self.pulp.get_repository(id).get_importers():
                for schedule in importer.get_schedules():
                    schedule.delete()
    
    def mainmenu(self):
        while True:
            print("1) Repository overview")
            print("2) Repository details")
            print("3) New repository")
            print("4) Start sync")
            print("5) Show schedules")
            print("6) Set schedules")
    
            print("q) Quit")
    
            selection = input("> ")
            if selection == '1':
                self.repos_overview()
            elif selection == '2':
                self.repos_details()
            elif selection == '3':
                self.repos_create()
            elif selection == '4':
                self.repos_sync()
            elif selection == '5':
                self.repos_schedules()
            elif selection == '6':
                self.repos_schedules_set()
            
            elif selection == 'q':
                break
    
            else:
                print("Invalid selection")

