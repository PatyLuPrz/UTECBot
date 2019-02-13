# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/asignatura_grupo', 'application.controllers.asignatura_grupo.index.Index',
    '/asignatura_grupo/view/(.+)', 'application.controllers.asignatura_grupo.view.View',
    '/asignatura_grupo/edit/(.+)', 'application.controllers.asignatura_grupo.edit.Edit',
    '/asignatura_grupo/delete/(.+)', 'application.controllers.asignatura_grupo.delete.Delete',
    '/asignatura_grupo/insert', 'application.controllers.asignatura_grupo.insert.Insert',
    '/asignatura_profesor', 'application.controllers.asignatura_profesor.index.Index',
    '/asignatura_profesor/view/(.+)', 'application.controllers.asignatura_profesor.view.View',
    '/asignatura_profesor/edit/(.+)', 'application.controllers.asignatura_profesor.edit.Edit',
    '/asignatura_profesor/delete/(.+)', 'application.controllers.asignatura_profesor.delete.Delete',
    '/asignatura_profesor/insert', 'application.controllers.asignatura_profesor.insert.Insert',
    '/asignaturas', 'application.controllers.asignaturas.index.Index',
    '/asignaturas/view/(.+)', 'application.controllers.asignaturas.view.View',
    '/asignaturas/edit/(.+)', 'application.controllers.asignaturas.edit.Edit',
    '/asignaturas/delete/(.+)', 'application.controllers.asignaturas.delete.Delete',
    '/asignaturas/insert', 'application.controllers.asignaturas.insert.Insert',
    '/grupos', 'application.controllers.grupos.index.Index',
    '/grupos/view/(.+)', 'application.controllers.grupos.view.View',
    '/grupos/edit/(.+)', 'application.controllers.grupos.edit.Edit',
    '/grupos/delete/(.+)', 'application.controllers.grupos.delete.Delete',
    '/grupos/insert', 'application.controllers.grupos.insert.Insert',
    '/horario', 'application.controllers.horario.index.Index',
    '/horario/view/(.+)', 'application.controllers.horario.view.View',
    '/horario/edit/(.+)', 'application.controllers.horario.edit.Edit',
    '/horario/delete/(.+)', 'application.controllers.horario.delete.Delete',
    '/horario/insert', 'application.controllers.horario.insert.Insert',
    '/profesores', 'application.controllers.profesores.index.Index',
    '/profesores/view/(.+)', 'application.controllers.profesores.view.View',
    '/profesores/edit/(.+)', 'application.controllers.profesores.edit.Edit',
    '/profesores/delete/(.+)', 'application.controllers.profesores.delete.Delete',
    '/profesores/insert', 'application.controllers.profesores.insert.Insert',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
