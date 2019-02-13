import web
import config

db = config.db


def get_all_asignatura_grupo():
    try:
        return db.select('asignatura_grupo')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asignatura_grupo(ClaveAG):
    try:
        return db.select('asignatura_grupo', where='ClaveAG=$ClaveAG', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_asignatura_grupo(ClaveAG):
    try:
        return db.delete('asignatura_grupo', where='ClaveAG=$ClaveAG', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_asignatura_grupo(ClaveAP,ClaveG):
    try:
        return db.insert('asignatura_grupo',ClaveAP=ClaveAP,
ClaveG=ClaveG)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_asignatura_grupo(ClaveAG,ClaveAP,ClaveG):
    try:
        return db.update('asignatura_grupo',ClaveAG=ClaveAG,
ClaveAP=ClaveAP,
ClaveG=ClaveG,
                  where='ClaveAG=$ClaveAG',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
