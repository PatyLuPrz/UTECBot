import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(ClaveG) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(ClaveG) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(ClaveG, **k):

    @staticmethod
    def POST_DELETE(ClaveG, **k):
    '''

    def GET(self, ClaveG, **k):
        message = None # Error message
        ClaveG = config.check_secure_val(str(ClaveG)) # HMAC ClaveG validate
        result = config.model.get_grupos(int(ClaveG)) # search  ClaveG
        result.ClaveG = config.make_secure_val(str(result.ClaveG)) # apply HMAC for ClaveG
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, ClaveG, **k):
        form = config.web.input() # get form data
        form['ClaveG'] = config.check_secure_val(str(form['ClaveG'])) # HMAC ClaveG validate
        result = config.model.delete_grupos(form['ClaveG']) # get grupos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            ClaveG = config.check_secure_val(str(ClaveG))  # HMAC user validate
            ClaveG = config.check_secure_val(str(ClaveG))  # HMAC user validate
            result = config.model.get_grupos(int(ClaveG)) # get ClaveG data
            result.ClaveG = config.make_secure_val(str(result.ClaveG)) # apply HMAC to ClaveG
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/grupos') # render grupos delete.html 
