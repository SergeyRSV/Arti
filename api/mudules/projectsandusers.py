import json

from redminelib import Redmine


def projects(KEY, url):
    URL = 'http://85.234.37.158:45456'
    URL = url
    redmine = Redmine(URL, key=KEY)
    proj_list = []
    for project in redmine.project.all():
        vard = {'name': project.name, 'id': project.id}
        proj_list.append(vard)
    return proj_list


def members(KEY, proj_number, url):
    URL = 'http://85.234.37.158:45456'
    URL = url
    redmine = Redmine(URL, key=KEY)
    my_users = []
    project = redmine.project.get(proj_number)
    for membership in project.memberships:
        vard = {'name': str(membership.user), 'id': membership.user.id, 'roles': list(membership.roles)}
        print(vard)
        my_users.append(vard)

        # my_users[membership.user.id] = str(membership.user)
    return my_users


# KEY = 'ffe0bbfb0b37dc9e6865fda716f9621e6a453583'
#
#
# print(members(KEY, 1))
