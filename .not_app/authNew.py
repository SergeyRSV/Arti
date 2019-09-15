from redminelib import Redmine

def auth():
    redmine = Redmine('http://192.168.111.74:3718', username='admin', password='P@ssword123').auth()
    return redmine.api_key

print(auth())


# project = redmine.project.get('test')
# issues  = list(project.issues)

