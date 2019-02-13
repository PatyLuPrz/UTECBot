import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, ClaveG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(ClaveG) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, ClaveG, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(ClaveG) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(ClaveG, **k):

    @staticmethod
    def POST_EDIT(ClaveG, **k):
        
    '''

    def GET(self, ClaveG, **k):
        message = None # Error message
        ClaveG = config.check_secure_val(str(ClaveG)) # HMAC ClaveG validate
        result = config.model.get_grupos(int(ClaveG)) # search for the ClaveG
        result.ClaveG = config.make_secure_val(str(result.ClaveG)) # apply HMAC for ClaveG
        return config.render.edit(result, message) # render grupos edit.html

    def POST(self, ClaveG, **k):
        form = config.web.input()  # get form data
        form['ClaveG'] = config.check_secure_val(str(form['ClaveG'])) # HMAC ClaveG validate
        # edit user with new data
        result = config.model.edit_grupos(
            form['ClaveG'],form['GradoG'],form['GrupoG'],form['CarreraG'],
        )
        if result == None: # Error on udpate data
            ClaveG = config.check_secure_val(str(ClaveG)) # validate HMAC ClaveG
            result = config.model.get_grupos(int(ClaveG)) # search for ClaveG data
            result.ClaveG = config.make_secure_val(str(result.ClaveG)) # apply HMAC to ClaveG
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/grupos') # render grupos index.html
