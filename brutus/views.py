""" views - brutus views """

from brutus.app import Handler


class index(Handler):
    def get(self):
        self.render("home.html")


class about(Handler):
    def get(self):
        self.render("about.html")


class explore(Handler):
    def get(self):
        self.render("explore.html")


class pricing(Handler):
    pass


class login(Handler):
    pass


class logout(Handler):
    pass
