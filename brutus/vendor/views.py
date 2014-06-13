""" brutus/vendor/views - vendor specific controllers """

from brutus.app import Handler


class index(Handler):
    def get(self):
        return self.render_json({"vendor_view": "IM IN THERE VENDOR VIEW"})
