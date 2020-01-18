from django.db import models
import sqlite3
from django.template import Context, Template
from django.http import HttpResponse
# Create your models here.
def filterQuery(query):
    res = query
    if type(query) == str:
        res = res.replace(";", "&#059;").replace("'", "&#39;").replace('"', '&quot;')
    else:
        pass
    return res

def update_rating(j_id, j_value):
    id = filterQuery(j_id)
    value = filterQuery(j_value)
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    j_cursor = jumoreski_db.cursor()
    sql = f'SELECT rating FROM jumoreski WHERE id = {id};'
    j_cursor.execute(sql)
    rating = int(str(j_cursor.fetchall()[0][0]))
    new_rating = rating + value
    sql = f'UPDATE jumoreski SET rating = {new_rating} WHERE id = {id};'
    j_cursor.execute(sql)
    jumoreski_db.commit()
    return rating + value;

def getPostsById(idlist):
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    jumoreski = []
    j_cursor = jumoreski_db.cursor()
    for i in idlist:
        sql = f'SELECT text, id, rating FROM jumoreski WHERE id = {i}'
        j_cursor.execute(sql)
        jumoreski.append(j_cursor.fetchall())
    if len(jumoreski) == 0:
        return '<h2>По данному запросу ничего не найдено.</h2>'
    else:
        j_temp = open("templates/jumoreska.html", "r")
        t = Template(j_temp.read())
        j_temp.close()
        base_content = '<h2>Найденные юморески:</h2>'
        for i in range(len(jumoreski)):
            a = jumoreski[i]
            c = Context({"jid": a[0][1], "jtext": a[0][0], "jrating": a[0][2]})
            base_content += t.render(c)
        return base_content

def getPostsBySubstring(substring, start_id=-1):
    res = []
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    j_cursor = jumoreski_db.cursor()
    # sql = f'SELECT text, id FROM jumoreski WHERE text LIKE %s;'
    sql = f'SELECT text, id FROM jumoreski WHERE id > {start_id} ORDER BY id LIMIT 5;'
    j_cursor.execute(sql)
    j_all = j_cursor.fetchall()
    if len(j_all) == 0:
        return res
    else:
        for i in range(len(j_all)):
            if substring.lower() in j_all[i][0].lower():
                res.append(j_all[i][1])
        return res

def new_jumoreska(text):
    t = filterQuery(text)
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    j_cursor = jumoreski_db.cursor()
    sql = f'SELECT max(id) FROM jumoreski'
    j_cursor.execute(sql)
    max_id = int(j_cursor.fetchall()[0][0]) + 1
    sql = f'INSERT INTO jumoreski (text, rating, id) VALUES {t}, 0, {max_id};'
    j_cursor.execute(sql)

def delete_post(id):
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    j_cursor = jumoreski_db.cursor()
    sql = f'DELETE FROM jumoreski WHERE id = {id};'
    j_cursor.execute(sql)
    jumoreski_db.commit()


def generate_content():
    jumoreski_db = sqlite3.connect('jumoreski.db.sqlite3')
    j_cursor = jumoreski_db.cursor()
    sql = '''SELECT text, id, rating FROM jumoreski'''
    j_cursor.execute(sql)
    jumoreski = j_cursor.fetchall()
    if len(jumoreski) == 0:
        return '<h2>Сегодня у нас нет юморесок!</h2>'
    else:
        j_temp = open("templates/jumoreska.html", "r")
        t = Template(j_temp.read())
        j_temp.close()
        base_content = ''
        for i in range(len(jumoreski)):
            a = jumoreski[i]
            c = Context({"jid": a[1], "jtext": filterQuery(a[0]), "jrating":a[2]})
            base_content += t.render(c)
        return base_content