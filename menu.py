import json

class Menu:
    pulp = None
    
    def __init__(self, pulp):
        self.pulp = pulp
        
    def pick_repo(self, multiple=False):
        repos = self.pulp.get_repositories()
        i = 1
        for repo in repos:
            print(str(i) + ") " + str(repo.display_name))
            i += 1
        
        selection = input('>')
        if multiple:
            ids = []
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
            importer0 = repo.get_importers()[0]
            print(repo.display_name + ':')
            if 'rpm' in repo.content_unit_counts.keys():
                print('\t' + str(repo.content_unit_counts['rpm']) + " rpms")
            print('\t' + "last synced: " + str(importer0.last_sync))
            print('\t' + "last added: " + str(repo.last_unit_added))
    
            if 'rpm' in repo.content_unit_counts.keys():
                packages += repo.content_unit_counts['rpm']
        
        print("\nTotal: " + str(packages) + " rpms in " + str(len(repos)) + " repositories.")
    
    def repos_details(self):
        repo = self.pulp.get_repository(self.pick_repo(self.pulp))
        print("Repository details:")
        print(repo.dump())
        print("\nRepository importers:")
        for importer in repo.get_importers():
            print(importer.dump())
        print("\nRepository distributors:")
        for distributor in repo.get_distributors():
            print(distributor.dump())
    
    def repos_sync(self):
        ids = self.pick_repo(self.pulp, multiple=True)
        for id in ids:
            self.pulp.sync_repository(id)
    
    def repos_schedules(self):
        repos = self.pulp.get_repositories()
        for repo in repos:
            importer0 = repo.get_importers()[0]
            print(repo.display_name + ":")
            if len(importer0.scheduled_syncs):
                for sync in importer0.scheduled_syncs:
                    print(" - " + sync)
            else:
                print(" - None")
    
    def repos_schedules_set(self):
        ids = self.pick_repo(self.pulp, multiple=True)
        schedule = input("Schedule?\n>")
        for id in ids:
            self.pulp.update_importer(id, "yum_importer", json.dumps({'importer_config': {'scheduled_syncs': [schedule]}}))        
    
    def mainmenu(self):
        while True:
            print("1) Repository overview")
            print("2) Repository details")
            print("3) Start sync")
            print("4) Show schedules")
            print("5) Set schedules")
    
            print("q) Quit")
    
            selection = input("> ")
            if selection == '1':
                self.repos_overview()
            elif selection == '2':
                self.repos_details()
            elif selection == '3':
                self.repos_sync()
            elif selection == '4':
                self.repos_schedules()
            elif selection == '5':
                self.repos_schedules_set()
            
            elif selection == 'q':
                break
    
            else:
                print("Invalid selection")