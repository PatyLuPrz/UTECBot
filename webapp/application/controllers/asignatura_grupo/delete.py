import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveAG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveAG) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveAG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveAG) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveAG, **k):

    @staticmethod
    def POST_DELETE(ClaveAG, **k):
    '''

    def GET(self, ClaveAG, **k):
        message = None # Error message
        ClaveAG = config.check_secure_val(str(ClaveAG)) # HMAC ClaveAG validate
        result = config.model.get_asignatura_grupo(int(ClaveAG)) # search  ClaveAG
        result.ClaveAG = config.make_secure_val(str(result.ClaveAG)) # apply HMAC for ClaveAG
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveAG, **k):
        form = config.web.input() # get form data
        form['ClaveAG'] = config.check_secure_val(str(form['ClaveAG'])) # HMAC ClaveAG validate
        result = config.model.delete_asignatura_grupo(form['ClaveAG']) # get asignatura_grupo data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveAG = config.check_secure_val(str(ClaveAG))  # HMAC user validate
            ClaveAG = config.check_secure_val(str(ClaveAG))  # HMAC user validate
            result = config.model.get_asignatura_grupo(int(ClaveAG)) # get ClaveAG data
            result.ClaveAG = config.make_secure_val(str(result.ClaveAG)) # apply HMAC to ClaveAG
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/asignatura_grupo') # render asignatura_grupo delete.html 
