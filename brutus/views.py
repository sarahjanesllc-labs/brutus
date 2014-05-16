""" views - brutus views """

from brutus.app import Handler

class index(Handler):
    def get(self):
        self.render_json({'status':'it works!'})

class about(Handler):
    def get(self):
        self.render_json({'status':'about us!'})
