from flask import render_template, session
from models.modelPublications import modelPublications

class PublicationsController():
    def index(self, id):
        if id == 'list':
            content = render_template("publications/list.html", **modelPublications.getList(id))
            return content

        if id == 'create':
            if session.get("admin") is None: return render_template("auth/form.html");
            content = render_template("publications/create.html", **modelPublications.getCreateData())
            return content

        if id == 'edit':
            if session.get("admin") is None: return render_template("auth/form.html");
            content = render_template("publications/edit.html", **modelPublications.getEditData())
            return content

        if id == 'save':
            if session.get("admin") is None: return render_template("auth/form.html");
            return modelPublications.save()

        if id == 'remove':
            if session.get("admin") is None: return render_template("auth/form.html");
            return modelPublications.remove()

        content = render_template("publications/publication.html", **modelPublications.getPublication(id))
        return content


publicationspage = PublicationsController()
