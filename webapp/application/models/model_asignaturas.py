import web
import config

db = config.db


def get_all_asignaturas():
    try:
        return db.select('asignaturas')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_asignaturas(ClaveA):
    try:
        return db.select('asignaturas', where='ClaveA=$ClaveA', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_asignaturas(ClaveA):
    try:
        return db.delete('asignaturas', where='ClaveA=$ClaveA', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_asignaturas(NombreA):
    try:
        return db.insert('asignaturas',NombreA=NombreA)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_asignaturas(ClaveA,NombreA):
    try:
        return db.update('asignaturas',ClaveA=ClaveA,
NombreA=NombreA,
                  where='ClaveA=$ClaveA',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
