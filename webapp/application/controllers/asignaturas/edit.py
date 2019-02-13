import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveA, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveA) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveA, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveA) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveA, **k):

    @staticmethod
    def POST_EDIT(ClaveA, **k):
        
    '''

    def GET(self, ClaveA, **k):
        message = None # Error message
        ClaveA = config.check_secure_val(str(ClaveA)) # HMAC ClaveA validate
        result = config.model.get_asignaturas(int(ClaveA)) # search for the ClaveA
        result.ClaveA = config.make_secure_val(str(result.ClaveA)) # apply HMAC for ClaveA
        return config.render.edit(result, message) # render asignaturas edit.html

    def POST(self, ClaveA, **k):
        form = config.web.input()  # get form data
        form['ClaveA'] = config.check_secure_val(str(form['ClaveA'])) # HMAC ClaveA validate
        # edit user with new data
        result = config.model.edit_asignaturas(
            form['ClaveA'],form['NombreA'],
        )
        if result == None: # Error on udpate data
            ClaveA = config.check_secure_val(str(ClaveA)) # validate HMAC ClaveA
            result = config.model.get_asignaturas(int(ClaveA)) # search for ClaveA data
            result.ClaveA = config.make_secure_val(str(result.ClaveA)) # apply HMAC to ClaveA
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/asignaturas') # render asignaturas index.html
