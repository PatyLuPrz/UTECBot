import web
import config

db = config.db


def get_all_profesores():
    try:
        return db.select('profesores')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_profesores(ClaveP):
    try:
        return db.select('profesores', where='ClaveP=$ClaveP', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_profesores(ClaveP):
    try:
        return db.delete('profesores', where='ClaveP=$ClaveP', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_profesores(NombreP):
    try:
        return db.insert('profesores',NombreP=NombreP)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_profesores(ClaveP,NombreP):
    try:
        return db.update('profesores',ClaveP=ClaveP,
NombreP=NombreP,
                  where='ClaveP=$ClaveP',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
