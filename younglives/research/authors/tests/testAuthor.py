import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

from base import INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Test content type"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('AuthorFolder', 'af1')
        af1 = getattr(self.portal, 'af1')
        af1.invokeFactory('Author', 'a1')
        assert 'a1' in af1.objectIds()
