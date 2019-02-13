import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveP) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveP) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveP, **k):

    @staticmethod
    def POST_EDIT(ClaveP, **k):
        
    '''

    def GET(self, ClaveP, **k):
        message = None # Error message
        ClaveP = config.check_secure_val(str(ClaveP)) # HMAC ClaveP validate
        result = config.model.get_profesores(int(ClaveP)) # search for the ClaveP
        result.ClaveP = config.make_secure_val(str(result.ClaveP)) # apply HMAC for ClaveP
        return config.render.edit(result, message) # render profesores edit.html

    def POST(self, ClaveP, **k):
        form = config.web.input()  # get form data
        form['ClaveP'] = config.check_secure_val(str(form['ClaveP'])) # HMAC ClaveP validate
        # edit user with new data
        result = config.model.edit_profesores(
            form['ClaveP'],form['NombreP'],
        )
        if result == None: # Error on udpate data
            ClaveP = config.check_secure_val(str(ClaveP)) # validate HMAC ClaveP
            result = config.model.get_profesores(int(ClaveP)) # search for ClaveP data
            result.ClaveP = config.make_secure_val(str(result.ClaveP)) # apply HMAC to ClaveP
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/profesores') # render profesores index.html
