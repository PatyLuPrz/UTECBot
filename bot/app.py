# -*- coding: UTF-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web
import time


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'bothorarios',
    user = 'bot',
    pw = 'bot.2019',
    port = 3306
)

token = ''


hora = time.strftime("%I:%M:%S")
#hora = "07:00:00"
noDiaStr = time.strftime("%w")
noDia = (int(noDiaStr))-1
days =[ 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']

def mensajeDeError(user,e):
    print "Error: {}".format(e.message)
    print "Error: {}".format(e.args)
    update.message.reply_text("Algo salio mal! No te preocupes, nos estamos encargando de eso. \nIntenta de nuevo más tarde")
    update.message.reply_text("Puedes reportar este error en el siguiente correo: may.patrics@gmail.com\nNo olvides incluir tu nombre y la descripción del error")
    


def start(bot, update):
    username = update.message.from_user.username
    mensaje = "Hola {} bienvenidx al sistema de consulta de horario!\nUsa el comando /info para mas informacion y /help para conocer la lista de comandos".format(username)
    nota = "NOTA: Este bot se encuentra en fase de desarrollo, es posible que algunas funciones NO esten disponibles aun :) \nDisfruta tu estancia"
    update.message.reply_text(mensaje)
    update.message.reply_text(nota)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text # que texto mando
    print update.message.date # cuando lo mando
    print update.message.from_user # quien lo mando
    print update.message.from_user.username

def help(bot,update):
    mensaje = "Lista de comandos: \n/help - para mostrar ayuda \n/today [Grupo] - para ver tu horario del dia actual \n/day [Grupo] [NombreDelDia] - Para ver tu horario de un dia especifico \n/now [Grupo] - Para saber la clave actual y las siguiente"
    # /hour [Grupo] [Hora] - Para saber la clase de una hora especifia del dia actual
    # /later [Grupos] [Hora] [NombreDelDia] - Para saber la clase a una hora y dia especificos
    update.message.reply_text(mensaje)
 
def info(bot,update):
    mensaje = "Con este bot podrás consultar información de tu horario. \n Hace falta solo que sepas tu grupo y listo. \n\n\n Consulta /help para conocer los comandos."
    update.message.reply_text(mensaje)

# Metodos de los comandos para consultas

def day(bot,update):
    searchDay(update)

def today(bot,update):
    searchToday(update)

def now(bot,update):
    searchNow(update)

# Consultas de cada comando

def searchNow(update):
    try:
        username = update.message.from_user.username
        text = update.message.text.split()
        grupo = text[1]
        dia = days[noDia]
        if dia == 'Sabado' or dia == 'Domingo':
            update.message.reply_text("Fin de semana! Tienes el dia libre.\nDiviertete")
        else:
            print "Send info to {}".format(username)
            print "Key serach: {}".format(dia)
            result = db.query("SELECT profesores.NombreP, asignaturas.NombreA, horario.HoraEntradaH, horario.HoraSalidaH, horario.Salon, horario.DiaH, grupos.GrupoG FROM horario INNER JOIN asignatura_grupo ON horario.ClaveAG = asignatura_grupo.ClaveAG INNER JOIN asignatura_profesor ON asignatura_grupo.ClaveAP = asignatura_profesor.ClaveAP INNER JOIN asignaturas ON asignatura_profesor.ClaveA = asignaturas.ClaveA INNER JOIN profesores ON asignatura_profesor.ClaveP = profesores.ClaveP INNER JOIN grupos ON asignatura_grupo.ClaveG = grupos.ClaveG WHERE horario.DiaH = $dia AND grupos.ClaveG = $grupo AND (horario.HoraEntradaH BETWEEN '"+hora+"' AND '07:40:00') ORDER BY horario.HoraEntradaH ASC",vars=locals())
            if not result:
                update.message.reply_text("Tus clases por hoy han terminado\n Prueba con /day para conocer tus clases de mañana \n o /today para ver las clases que tomaste hoy")
            list= []
            for x in result:
                Salon=str(x['Salon'])
                NombreA=str(x['NombreA'])
                DiaH=str(x['DiaH'])
                HoraEntradaH=str(x['HoraEntradaH'])
                GrupoG=str(x['GrupoG'])
                HoraSalidaH=str(x['HoraSalidaH'])
                list.append([
                    "Día: ", DiaH,
                    "\nGrupo: ",GrupoG,
                    "\nNombre de la asignatura: ", NombreA,
                    "\nSalón: ",Salon,
                    "\nHora de entrada: ",HoraEntradaH,
                    "\nHora de salida: ",HoraSalidaH
                ])
            txt = ""
            for y in list:
                for g in y:
                    txt += g
                update.message.reply_text(txt)
                txt = ""
    except Exception as e:
        mensajeDeError(username,e)

def searchDay(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        dia = text[2]
        grupo = text[1]
        if dia == 'Sabado' or dia == 'Domingo':
            update.message.reply_text("Fin de semana! Tienes el dia libre.\nDiviertete")
        else:
            print "Send info to {}".format(username)
            print "Key serach: {}".format(dia)
            result = db.query("SELECT \
    profesores.NombreP, \
    asignaturas.NombreA,  \
    horario.HoraEntradaH,  \
    horario.HoraSalidaH,  \
    horario.Salon,  \
    horario.DiaH,  \
    grupos.GrupoG  \
    FROM  \
    horario  \
    INNER JOIN asignatura_grupo ON horario.ClaveAG = asignatura_grupo.ClaveAG  \
    INNER JOIN asignatura_profesor ON asignatura_grupo.ClaveAP = asignatura_profesor.ClaveAP \
    INNER JOIN asignaturas ON asignatura_profesor.ClaveA = asignaturas.ClaveA  \
    INNER JOIN profesores ON asignatura_profesor.ClaveP = profesores.ClaveP  \
    INNER JOIN grupos ON asignatura_grupo.ClaveG = grupos.ClaveG  \
    WHERE  \
    horario.DiaH = $dia AND  \
    grupos.ClaveG = $grupo \
    ORDER BY horario.HoraEntradaH ASC",vars=locals())

            list= []
            for x in result:
                Salon=str(x['Salon'])
                NombreA=str(x['NombreA'])
                DiaH=str(x['DiaH'])
                HoraEntradaH=str(x['HoraEntradaH'])
                GrupoG=str(x['GrupoG'])
                HoraSalidaH=str(x['HoraSalidaH'])
                list.append([
                    "Día: ", DiaH,
                    "\nGrupo: ",GrupoG,
                    "\nNombre de la asignatura: ", NombreA,
                    "\nSalón: ",Salon,
                    "\nHora de entrada: ",HoraEntradaH,
                    "\nHora de salida: ",HoraSalidaH
                ])
                
                #list.append(["Salon: ",Salon,"\nNombre de la signatura: ",NombreA,DiaH,HoraEntradaH,GrupoG,HoraSalidaH])
            txt = ""
            for y in list:
                for g in y:
                    txt += g
                update.message.reply_text(txt)
                txt = ""
    except Exception as e:
        mensajeDeError(username,e)


def searchToday(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        dia = days[noDia]
        grupo = text[1]
        if dia == 'Sabado' or dia == 'Domingo':
            update.message.reply_text("Fin de semana! Tienes el dia libre.\nDiviertete")
        else:
            print "Send info to {}".format(username)
            print "Key serach: {}".format(dia)
            result = db.query("SELECT \
    profesores.NombreP, \
    asignaturas.NombreA,  \
    horario.HoraEntradaH,  \
    horario.HoraSalidaH,  \
    horario.Salon,  \
    horario.DiaH,  \
    grupos.GrupoG  \
    FROM  \
    horario  \
    INNER JOIN asignatura_grupo ON horario.ClaveAG = asignatura_grupo.ClaveAG  \
    INNER JOIN asignatura_profesor ON asignatura_grupo.ClaveAP = asignatura_profesor.ClaveAP \
    INNER JOIN asignaturas ON asignatura_profesor.ClaveA = asignaturas.ClaveA  \
    INNER JOIN profesores ON asignatura_profesor.ClaveP = profesores.ClaveP  \
    INNER JOIN grupos ON asignatura_grupo.ClaveG = grupos.ClaveG  \
    WHERE  \
    horario.DiaH = $dia AND  \
    grupos.ClaveG = $grupo \
    ORDER BY horario.HoraEntradaH ASC",vars=locals())

            list= []
            for x in result:
                Salon=str(x['Salon'])
                NombreA=str(x['NombreA'])
                DiaH=str(x['DiaH'])
                HoraEntradaH=str(x['HoraEntradaH'])
                GrupoG=str(x['GrupoG'])
                HoraSalidaH=str(x['HoraSalidaH'])
                list.append([
                    "Día: ", DiaH,
                    "\nGrupo: ",GrupoG,
                    "\nNombre de la asignatura: ", NombreA,
                    "\nSalón: ",Salon,
                    "\nHora de entrada: ",HoraEntradaH,
                    "\nHora de salida: ",HoraSalidaH
                ])
                
                #list.append(["Salon: ",Salon,"\nNombre de la signatura: ",NombreA,DiaH,HoraEntradaH,GrupoG,HoraSalidaH])
            txt = ""
            for y in list:
                for g in y:
                    txt += g
                update.message.reply_text(txt)
                txt = ""
    except Exception as e:
        mensajeDeError(username,e)

def main():
    try:
        print "HorariosUTECBot init token"

        updater = Updater(token)

        dp = updater.dispatcher

        print "HorariosUTECBot init dispatcher"

        dp.add_handler(CommandHandler("start",start))
        dp.add_handler(CommandHandler("help",help))
        dp.add_handler(CommandHandler("info",info))
        dp.add_handler(CommandHandler("today",today))
        dp.add_handler(CommandHandler("day",day))
        dp.add_handler(CommandHandler("now",now))
        # dp.add_handler(CommandHandler("",))

        
        dp.add_handler(MessageHandler(Filters.text, echo))

        updater.start_polling()

        print "HorariosUTECBot ready!"
        updater.idle()
    except Exception as e:
        print "Error 001: ", e.message

if __name__ == '__main__':
    main()
