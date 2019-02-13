import web
import config

db = config.db


def get_all_grupos():
    try:
        return db.select('grupos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_grupos(ClaveG):
    try:
        return db.select('grupos', where='ClaveG=$ClaveG', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_grupos(ClaveG):
    try:
        return db.delete('grupos', where='ClaveG=$ClaveG', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_grupos(GradoG,GrupoG,CarreraG):
    try:
        return db.insert('grupos',GradoG=GradoG,
GrupoG=GrupoG,
CarreraG=CarreraG)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_grupos(ClaveG,GradoG,GrupoG,CarreraG):
    try:
        return db.update('grupos',ClaveG=ClaveG,
GradoG=GradoG,
GrupoG=GrupoG,
CarreraG=CarreraG,
                  where='ClaveG=$ClaveG',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
