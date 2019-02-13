import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveA, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveA) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveA, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveA) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveA, **k):

    @staticmethod
    def POST_DELETE(ClaveA, **k):
    '''

    def GET(self, ClaveA, **k):
        message = None # Error message
        ClaveA = config.check_secure_val(str(ClaveA)) # HMAC ClaveA validate
        result = config.model.get_asignaturas(int(ClaveA)) # search  ClaveA
        result.ClaveA = config.make_secure_val(str(result.ClaveA)) # apply HMAC for ClaveA
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveA, **k):
        form = config.web.input() # get form data
        form['ClaveA'] = config.check_secure_val(str(form['ClaveA'])) # HMAC ClaveA validate
        result = config.model.delete_asignaturas(form['ClaveA']) # get asignaturas data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveA = config.check_secure_val(str(ClaveA))  # HMAC user validate
            ClaveA = config.check_secure_val(str(ClaveA))  # HMAC user validate
            result = config.model.get_asignaturas(int(ClaveA)) # get ClaveA data
            result.ClaveA = config.make_secure_val(str(result.ClaveA)) # apply HMAC to ClaveA
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/asignaturas') # render asignaturas delete.html 
