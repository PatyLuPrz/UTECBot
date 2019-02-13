import web
import config

db = config.db


def get_all_horario():
    try:
        return db.select('horario')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_horario(ClaveH):
    try:
        return db.select('horario', where='ClaveH=$ClaveH', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_horario(ClaveH):
    try:
        return db.delete('horario', where='ClaveH=$ClaveH', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_horario(ClaveAG,DiaH,HoraEntradaH,HoraSalidaH,Salon):
    try:
        return db.insert('horario',ClaveAG=ClaveAG,
DiaH=DiaH,
HoraEntradaH=HoraEntradaH,
HoraSalidaH=HoraSalidaH,
Salon=Salon)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_horario(ClaveH,ClaveAG,DiaH,HoraEntradaH,HoraSalidaH,Salon):
    try:
        return db.update('horario',ClaveH=ClaveH,
ClaveAG=ClaveAG,
DiaH=DiaH,
HoraEntradaH=HoraEntradaH,
HoraSalidaH=HoraSalidaH,
Salon=Salon,
                  where='ClaveH=$ClaveH',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
