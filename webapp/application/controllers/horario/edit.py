import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveH, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveH) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveH, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveH) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveH, **k):

    @staticmethod
    def POST_EDIT(ClaveH, **k):
        
    '''

    def GET(self, ClaveH, **k):
        message = None # Error message
        ClaveH = config.check_secure_val(str(ClaveH)) # HMAC ClaveH validate
        result = config.model.get_horario(int(ClaveH)) # search for the ClaveH
        result.ClaveH = config.make_secure_val(str(result.ClaveH)) # apply HMAC for ClaveH
        return config.render.edit(result, message) # render horario edit.html

    def POST(self, ClaveH, **k):
        form = config.web.input()  # get form data
        form['ClaveH'] = config.check_secure_val(str(form['ClaveH'])) # HMAC ClaveH validate
        # edit user with new data
        result = config.model.edit_horario(
            form['ClaveH'],form['ClaveAG'],form['DiaH'],form['HoraEntradaH'],form['HoraSalidaH'],form['Salon'],
        )
        if result == None: # Error on udpate data
            ClaveH = config.check_secure_val(str(ClaveH)) # validate HMAC ClaveH
            result = config.model.get_horario(int(ClaveH)) # search for ClaveH data
            result.ClaveH = config.make_secure_val(str(result.ClaveH)) # apply HMAC to ClaveH
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/horario') # render horario index.html
