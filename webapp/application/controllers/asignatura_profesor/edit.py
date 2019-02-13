import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveAP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveAP) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveAP, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveAP) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveAP, **k):

    @staticmethod
    def POST_EDIT(ClaveAP, **k):
        
    '''

    def GET(self, ClaveAP, **k):
        message = None # Error message
        ClaveAP = config.check_secure_val(str(ClaveAP)) # HMAC ClaveAP validate
        result = config.model.get_asignatura_profesor(int(ClaveAP)) # search for the ClaveAP
        result.ClaveAP = config.make_secure_val(str(result.ClaveAP)) # apply HMAC for ClaveAP
        return config.render.edit(result, message) # render asignatura_profesor edit.html

    def POST(self, ClaveAP, **k):
        form = config.web.input()  # get form data
        form['ClaveAP'] = config.check_secure_val(str(form['ClaveAP'])) # HMAC ClaveAP validate
        # edit user with new data
        result = config.model.edit_asignatura_profesor(
            form['ClaveAP'],form['ClaveA'],form['ClaveP'],
        )
        if result == None: # Error on udpate data
            ClaveAP = config.check_secure_val(str(ClaveAP)) # validate HMAC ClaveAP
            result = config.model.get_asignatura_profesor(int(ClaveAP)) # search for ClaveAP data
            result.ClaveAP = config.make_secure_val(str(result.ClaveAP)) # apply HMAC to ClaveAP
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/asignatura_profesor') # render asignatura_profesor index.html
