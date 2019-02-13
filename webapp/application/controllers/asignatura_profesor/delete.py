import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveAP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveAP) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveAP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveAP) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveAP, **k):

    @staticmethod
    def POST_DELETE(ClaveAP, **k):
    '''

    def GET(self, ClaveAP, **k):
        message = None # Error message
        ClaveAP = config.check_secure_val(str(ClaveAP)) # HMAC ClaveAP validate
        result = config.model.get_asignatura_profesor(int(ClaveAP)) # search  ClaveAP
        result.ClaveAP = config.make_secure_val(str(result.ClaveAP)) # apply HMAC for ClaveAP
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveAP, **k):
        form = config.web.input() # get form data
        form['ClaveAP'] = config.check_secure_val(str(form['ClaveAP'])) # HMAC ClaveAP validate
        result = config.model.delete_asignatura_profesor(form['ClaveAP']) # get asignatura_profesor data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveAP = config.check_secure_val(str(ClaveAP))  # HMAC user validate
            ClaveAP = config.check_secure_val(str(ClaveAP))  # HMAC user validate
            result = config.model.get_asignatura_profesor(int(ClaveAP)) # get ClaveAP data
            result.ClaveAP = config.make_secure_val(str(result.ClaveAP)) # apply HMAC to ClaveAP
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/asignatura_profesor') # render asignatura_profesor delete.html 
