""" api """

from brutus.app import Handler


class index(Handler):
    def get(self):
        return self.render_json({"products": "list of products"})


class detail(Handler):
    def get(self, _id):
        return self.render_json({"product_detail": _id})
