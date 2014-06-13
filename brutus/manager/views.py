""" views """

from brutus.app import Handler


class index(Handler):
    def get(self):
        return self.render_json({"manager_index": "IM IN THEIR MANAGER VIEW"})
