
from messybrainz.webserver.testing import ServerTestCase
from flask import url_for


class IndexViewsTestCase(ServerTestCase):

    def test_home(self):
        resp = self.client.get(url_for('index.home'))
        self.assert200(resp)

    def test_flask_debugtoolbar(self):
        """ Test if flask debugtoolbar is loaded correctly

        Note: Debug is set to  True in test_config.py, so the app
        created by ServerTestCase's create_app should load the toolbar
        """
        resp = self.client.get(url_for('index.home'))
        self.assert200(resp)
        self.assertIn('flDebug', str(resp.data))
