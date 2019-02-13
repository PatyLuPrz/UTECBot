import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveAG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveAG) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveAG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveAG) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveAG, **k):

    @staticmethod
    def POST_EDIT(ClaveAG, **k):
        
    '''

    def GET(self, ClaveAG, **k):
        message = None # Error message
        ClaveAG = config.check_secure_val(str(ClaveAG)) # HMAC ClaveAG validate
        result = config.model.get_asignatura_grupo(int(ClaveAG)) # search for the ClaveAG
        result.ClaveAG = config.make_secure_val(str(result.ClaveAG)) # apply HMAC for ClaveAG
        return config.render.edit(result, message) # render asignatura_grupo edit.html

    def POST(self, ClaveAG, **k):
        form = config.web.input()  # get form data
        form['ClaveAG'] = config.check_secure_val(str(form['ClaveAG'])) # HMAC ClaveAG validate
        # edit user with new data
        result = config.model.edit_asignatura_grupo(
            form['ClaveAG'],form['ClaveAP'],form['ClaveG'],
        )
        if result == None: # Error on udpate data
            ClaveAG = config.check_secure_val(str(ClaveAG)) # validate HMAC ClaveAG
            result = config.model.get_asignatura_grupo(int(ClaveAG)) # search for ClaveAG data
            result.ClaveAG = config.make_secure_val(str(result.ClaveAG)) # apply HMAC to ClaveAG
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/asignatura_grupo') # render asignatura_grupo index.html
