import time
import unittest2 as unittest
from zExceptions import BadRequest

from zope.component import getSiteManager

from Products.CMFCore.utils import getToolByName

from base import INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testTypesInstalled(self):
        portal_types = getToolByName(self.portal, 'portal_types')
        assert 'Author' in portal_types.objectIds(), portal_types.objectIds()
        assert 'AuthorFolder' in portal_types.objectIds(), portal_types.objectIds()

    def testPortalFactorySetup(self):
        assert 'Author' in self.portal.portal_factory.getFactoryTypes()
        assert 'AuthorFolder' in self.portal.portal_factory.getFactoryTypes()

    def testNavtreePropertiesConfigured(self):
        portal_types = self.portal.portal_properties.navtree_properties.metaTypesNotToList
        assert 'Author' in portal_types

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        try:
            portal_setup.runAllImportStepsFromProfile('profile-younglives.research.authors:default')
        except BadRequest:
            # if tests run too fast, duplicate profile import id makes test fail
            time.sleep(0.5)
            portal_setup.runAllImportStepsFromProfile('profile-younglives.research.authors:default')
