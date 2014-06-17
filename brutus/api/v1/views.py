""" views """

from brutus.app import Handler


class vendors(Handler):
    def get(self):
        return self.render_json({"vendors": "would be list of vendors"})

class products(Handler):
    def get(self):
        return self.render_json({"products": "list of products"})
