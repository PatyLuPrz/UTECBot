import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveH, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveH) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveH, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveH) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveH, **k):

    @staticmethod
    def POST_DELETE(ClaveH, **k):
    '''

    def GET(self, ClaveH, **k):
        message = None # Error message
        ClaveH = config.check_secure_val(str(ClaveH)) # HMAC ClaveH validate
        result = config.model.get_horario(int(ClaveH)) # search  ClaveH
        result.ClaveH = config.make_secure_val(str(result.ClaveH)) # apply HMAC for ClaveH
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveH, **k):
        form = config.web.input() # get form data
        form['ClaveH'] = config.check_secure_val(str(form['ClaveH'])) # HMAC ClaveH validate
        result = config.model.delete_horario(form['ClaveH']) # get horario data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveH = config.check_secure_val(str(ClaveH))  # HMAC user validate
            ClaveH = config.check_secure_val(str(ClaveH))  # HMAC user validate
            result = config.model.get_horario(int(ClaveH)) # get ClaveH data
            result.ClaveH = config.make_secure_val(str(result.ClaveH)) # apply HMAC to ClaveH
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/horario') # render horario delete.html 
