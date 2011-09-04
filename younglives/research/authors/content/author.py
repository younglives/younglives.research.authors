import transaction
from AccessControl import ClassSecurityInfo
from zExceptions import BadRequest
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from younglives.research.authors import _
from younglives.research.authors import permissions
from younglives.research.authors.config import PROJECTNAME
from younglives.research.authors.interfaces.author import IAuthor

from schemata import AuthorSchema

class Author(ATCTContent):
    """A author of a piece of research"""

    security = ClassSecurityInfo()

    implements(IAuthor)

    meta_type = 'Author'
    _at_rename_after_creation = False

    schema = AuthorSchema

    security.declarePrivate('_renameAfterCreation')
    def _renameAfterCreation(self, check_auto_id=False):
        plone_tool = getToolByName(self, 'plone_utils', None)
        parent = self.aq_inner.aq_parent
        newId = self.getName()
        newId = plone_tool.normalizeString(newId)
        #newId = newId.replace(' ', '_')
        #newId = newId.lower()
        transaction.savepoint(optimistic = True)
        self.setId(newId)

    security.declarePrivate('at_post_edit_script')
    def at_post_edit_script(self):
        """change the id based on referenceNumber"""
        self._renameAfterCreation()

    security.declarePublic('Title')
    def Title(self):
        """Return the name as the title"""
        return self.getName()

    security.declarePublic('canSetConstrainTypes')
    def getName(self):
        """Return the name in correct order"""
        personal_names = self.getPersonalNames()
        family_name = self.getFamilyName()
        if self.getNameOrder():
            return family_name + ' ' + personal_names
        return personal_names + ' ' + family_name

registerType(Author, PROJECTNAME)
