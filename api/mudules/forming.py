from redminelib import Redmine
import datetime
from datetime import timedelta
from beautifultable import BeautifulTable


# URL = 'http://192.168.111.74:3718'
# KEY = 'ffe0bbfb0b37dc9e6865fda716f9621e6a453583'


def proj_all(URL, KEY):
    redmine = Redmine(URL, key=KEY)
    string = ''
    for project in redmine.project.all():
        string += proj_iss_info(URL=URL, proj_number=project.id, KEY=KEY)  # добавление строки
        string += '\n***\n'
        string += sprint_info(URL=URL, proj_number=project.id, KEY=KEY)
        string += '\n***\n'

    return string


# ---------------------------------------------
def proj_iss_info(URL, KEY, proj_number):
    redmine = Redmine(URL, key=KEY)
    project = redmine.project.get(proj_number)
    proj_name = project.name
    string = '**Название проекта: **' + proj_name + '\n===\n'

    wd = datetime.datetime.today().weekday()
    time = datetime.datetime.today()
    if wd == 0:
        checktime = time - timedelta(days=3)
    else:
        checktime = time - timedelta(days=1)

    projects = redmine.issue.filter(
        sort='category:desc',
        project_id=proj_number,
        created_on='>=%s' % checktime.strftime('%Y-%m-%d')
    )

    # -----------------------------------------------------

    date_iss_list = []

    for iss in projects:
        date_iss_list.append(iss.id)

    projects = redmine.project.get(proj_number)

    all_iss_list = []
    for iss in projects.issues:
        all_iss_list.append(iss.id)

    all_iss_list = sorted(all_iss_list)

    string += '**_Изменение статусов задач за _**' + str(checktime.strftime('%Y-%m-%d')) + '\n' + '\n'

    table_change = BeautifulTable()
    table_change.set_style(BeautifulTable.STYLE_MARKDOWN)
    table_change.column_headers = ["Задача", "Номер", "Статус", "Новый статус"]

    for i in all_iss_list:
        issue = redmine.issue.get(i, include='journals')

        for record in issue.journals:
            for x in range(len(record.details)):
                if record.created_on.strftime('%Y-%m-%d') >= str(checktime):
                    try:
                        if record.details[x]['name'] == 'status_id':
                            old_value = redmine.issue_status.get(int(record.details[x]['old_value']))
                            new_value = redmine.issue_status.get(int(record.details[x]['new_value']))
                            table_change.append_row([str(issue), str(issue.id), str(old_value), str(new_value)])
                    except:
                        pass

    string += str(table_change) + '\n' + '\n'

    # ---------статусы---------------

    string += '**_Задачи с новым статусом за _**' + str(checktime.strftime('%Y-%m-%d')) + '\n' + '\n'
    iss_status = []
    table_new = BeautifulTable()
    table_new.set_style(BeautifulTable.STYLE_MARKDOWN)
    table_new.column_headers = ["Задача", "Номер"]
    for iss in date_iss_list:
        issue = redmine.issue.get(iss, include=['children', 'journals', 'watchers'])
        if str(issue.status) == 'New':
            table_new.append_row([str(issue), str(iss)])
            iss_status.append(iss)
        elif iss_status == []:
            string += 'Новых задач нет' + '\n'
    string += str(table_new)

    # --------------Процент готовности--------------------------

    string += '\n' + '**_Процент готовности/затраты времени:_**' + '\n' + '\n'

    table_done = BeautifulTable()
    table_done.set_style(BeautifulTable.STYLE_MARKDOWN)
    table_done.column_headers = ["Задача", "Номер", "Готовность", "Время"]
    for iss in all_iss_list:
        issue = redmine.issue.get(iss, include=['children', 'journals', 'watchers'])  # Проверить---
        table_done.append_row([str(issue), str(iss), str(issue.done_ratio), str(issue.spent_hours)])
    string += str(table_done)
    # --------------------------------------------------

    return string


def sprint_info(URL, KEY, proj_number):
    redmine = Redmine(URL, key=KEY)
    project = redmine.project.get(proj_number)
    string = ''

    # get versions
    versions = project.versions
    for i in range(len(versions)):
        if versions[i].status == 'open':
            try:
                created = versions[i].created_on
                today = datetime.datetime.today()
                a = today - created
                due_date = versions[i].due_date
                today1 = datetime.date.today()
                b = due_date - today1
                string += '**' + str(versions[i]) + ';**' + '\n' + '**_Дней прошло: ' + str(
                    a.days) + '; ' + ' Дней осталось: ' + str(
                    b.days) + '_**' + '\n' + '\n'
            except:
                string += '**_' + str(versions[i]) + '; Дней прошло: ' + str(
                    a.days) + '; ' + ' Дата завершения не указана' + '_**' + '\n' + '\n'
        else:
            break
    # -------------------------------------------------------------------------------------

    ID_PROJ = proj_number
    table_traker = BeautifulTable()
    table_traker.set_style(BeautifulTable.STYLE_MARKDOWN)
    table_traker.column_headers = ["", "Открыто", "Закрыто", "В работе"]

    issues_bug = redmine.issue.filter(project_id=ID_PROJ, status_id='*', tracker_id='1')
    table_traker.append_row(iss_count(issues_bug, 'Баги'))

    issues_task = redmine.issue.filter(project_id=ID_PROJ, status_id='*', tracker_id='4')
    table_traker.append_row(iss_count(issues_task, 'Задачи'))

    string += str(table_traker) + '\n' + '\n'
    # --------------------------------------------------------------------------------------

    all_iss_list = []
    string += '**_Превышение трудозатрат по задачам _**' + '\n' + '\n'

    projects = redmine.project.get(proj_number)

    table_estimated_hours = BeautifulTable()
    table_estimated_hours.set_style(BeautifulTable.STYLE_MARKDOWN)
    table_estimated_hours.column_headers = ["Задача", "Номер", "Время"]

    for iss in projects.issues:
        all_iss_list.append(iss.id)

    all_iss_list = sorted(all_iss_list)
    prev = 0

    for iss in all_iss_list:
        issue = redmine.issue.get(iss, include=['children', 'journals', 'watchers'])
        try:
            x = issue.spent_hours - issue.total_estimated_hours
            if x > 0:
                table_estimated_hours.append_row([str(issue), str(iss), str(x)])
                prev += 1
        except:
            pass

    string += str(table_estimated_hours)
    if prev == 0:
        string += 'Превышения нет' + '\n' + '\n'

    return string


def iss_count(issues_bug, tracker):
    closed = 0  # 5
    in_progress = 0  # 2
    other = 0  # 3

    for iss in issues_bug:

        status = iss.status.id
        if status == 5:
            closed += 1
        elif status == 2:
            in_progress += 1
        else:
            other += 1

    list = [tracker, str(other), str(closed), str(in_progress)]

    return list

    # -----------------------------------------------------

# with open('file.txt', 'w') as w:
#     w.write(proj_all())

# print(proj_all())
