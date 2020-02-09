import sqlite3
import json
from flask import request

class PublicationsModel():
    def getList(self, id):
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row

        cur = con.cursor()

        cur.execute("SELECT * FROM `publications` ORDER BY `id` ASC")

        publications = cur.fetchall()

        data = {
            "id"  : id,
            "publications": publications
        }
        return data

    def getCreateData(self):
        data = {
        }
        return data

    def getEditData(self):
        args = request.args;

        data = PublicationsModel.getPublication(self, args.get("id"))

        return data

    def getPublication(self, id):
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM `publications` WHERE `id` = ?", [id])

        rows = cur.fetchall();

        data = {
            "id"  : id,
            "publication": rows[0]
        }
        return data

    def save(self):
        id = request.form['id']
        title = request.form['title']
        description = request.form['description']
        content = request.form['content']
        cover = request.form['cover']
        author = request.form['author']

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        if float(id) == 0 :
            cur.execute("INSERT INTO `publications` (`title`, `content`, `cover`, `description`, `author`) VALUES (?,?,?,?,?)",
                (title, content, cover, description, author) )
            id = cur.lastrowid
        else:
            cur.execute("UPDATE `publications` SET `title` = ?, `content` = ?, `cover` = ?, `description` = ?, `author` = ? WHERE `id` = ?",
                (title, content, cover, description, author, id) )
        con.commit()

        return json.dumps({
            "status": "success",
            "id": id
        })

    def remove(self):
        id = request.form['id']

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        cur.execute("DELETE FROM `publications` WHERE `id` = ?", (id) )
        con.commit()

        return json.dumps({
            "status": "success"
        })


modelPublications = PublicationsModel()
