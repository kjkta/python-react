class Conf(object):
    _render_url = 'http://127.0.0.1:9009/render'
    _render = True
    _no_throw = False

    # Indicates that we should rely on Django's settings as the
    # canonical reference and use the above defaults as fallbacks.
    # Proxying to django.conf.settings allows us to swap out Django's
    # tests during tests
    _PROXY_DJANGO_SETTINGS = False

    @property
    def RENDER_URL(self):
        if not self._PROXY_DJANGO_SETTINGS:
            return self._render_url

        from django.conf import settings

        if hasattr(settings, 'REACT'):
            return settings.REACT.get('RENDER_URL', self._render_url)

        return self._render_url

    @property
    def RENDER(self):
        if not self._PROXY_DJANGO_SETTINGS:
            return self._render

        from django.conf import settings

        if hasattr(settings, 'REACT'):
            return settings.REACT.get('RENDER', self._render)

        return self._render

    @property
    def NO_THROW(self):
        if not self._PROXY_DJANGO_SETTINGS:
            return self._no_throw

        from django.conf import settings

        if hasattr(settings, 'REACT'):
            return settings.REACT.get('NO_THROW', self._no_throw)

        return self._no_throw

    def configure(self, RENDER_URL=None, RENDER=None, NO_THROW=None):
        if RENDER_URL is not None:
            self._render_url = RENDER_URL
        if RENDER is not None:
            self._render = RENDER
        if NO_THROW is not None:
            self._no_throw = NO_THROW

settings = Conf()
