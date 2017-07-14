class Gitbub(object):

    u = ''

    def set_username(self, username):
        self.u = username

    def get_username(self):
        return self.u

    def obter_repositorios_do(self, usuario):
        url = 'https://api.github.com/users/%s/repos' %
            usuario

        return []
        
