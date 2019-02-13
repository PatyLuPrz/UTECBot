import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, ClaveP):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(ClaveP) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(ClaveP):
    '''

    def GET(self, ClaveP):
        ClaveP = config.check_secure_val(str(ClaveP)) # HMAC ClaveP validate
        result = config.model.get_profesores(ClaveP) # search for the ClaveP data
        return config.render.view(result) # render view.html with ClaveP data
