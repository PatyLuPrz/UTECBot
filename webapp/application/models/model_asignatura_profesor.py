import web
import config

db = config.db


def get_all_asignatura_profesor():
    try:
        return db.select('asignatura_profesor')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asignatura_profesor(ClaveAP):
    try:
        return db.select('asignatura_profesor', where='ClaveAP=$ClaveAP', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_asignatura_profesor(ClaveAP):
    try:
        return db.delete('asignatura_profesor', where='ClaveAP=$ClaveAP', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_asignatura_profesor(ClaveA,ClaveP):
    try:
        return db.insert('asignatura_profesor',ClaveA=ClaveA,
ClaveP=ClaveP)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_asignatura_profesor(ClaveAP,ClaveA,ClaveP):
    try:
        return db.update('asignatura_profesor',ClaveAP=ClaveAP,
ClaveA=ClaveA,
ClaveP=ClaveP,
                  where='ClaveAP=$ClaveAP',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
