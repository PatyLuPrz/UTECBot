import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, ClaveA):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(ClaveA) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(ClaveA):
    '''

    def GET(self, ClaveA):
        ClaveA = config.check_secure_val(str(ClaveA)) # HMAC ClaveA validate
        result = config.model.get_asignaturas(ClaveA) # search for the ClaveA data
        return config.render.view(result) # render view.html with ClaveA data
