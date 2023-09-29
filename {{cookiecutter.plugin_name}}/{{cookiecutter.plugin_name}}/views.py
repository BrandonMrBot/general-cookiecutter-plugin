import {{ cookiecutter.plugin_for }}.plugins.utilities as u


class MyPublicView(u.PublicView):
    def process_view(self):

        return {}


class MyPrivateView(u.PrivateView):
    def __init__(self, request):
        u.PrivateView.__init__(self, request)
        self.checkCrossPost = False

    def processView(self):

        return {
            "activeUser": self.user,
            "message": "Hello word",
        }
