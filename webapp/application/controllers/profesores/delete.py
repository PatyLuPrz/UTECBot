import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveP) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveP) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveP, **k):

    @staticmethod
    def POST_DELETE(ClaveP, **k):
    '''

    def GET(self, ClaveP, **k):
        message = None # Error message
        ClaveP = config.check_secure_val(str(ClaveP)) # HMAC ClaveP validate
        result = config.model.get_profesores(int(ClaveP)) # search  ClaveP
        result.ClaveP = config.make_secure_val(str(result.ClaveP)) # apply HMAC for ClaveP
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveP, **k):
        form = config.web.input() # get form data
        form['ClaveP'] = config.check_secure_val(str(form['ClaveP'])) # HMAC ClaveP validate
        result = config.model.delete_profesores(form['ClaveP']) # get profesores data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveP = config.check_secure_val(str(ClaveP))  # HMAC user validate
            ClaveP = config.check_secure_val(str(ClaveP))  # HMAC user validate
            result = config.model.get_profesores(int(ClaveP)) # get ClaveP data
            result.ClaveP = config.make_secure_val(str(result.ClaveP)) # apply HMAC to ClaveP
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/profesores') # render profesores delete.html 
