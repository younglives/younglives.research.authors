import os
from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import DisplayList
from Products.Archetypes.atapi import registerType
from Products.CMFCore.utils import getToolByName

from younglives.research.authors import permissions
from younglives.research.authors.config import PROJECTNAME
from younglives.research.authors.interfaces.author_folder import IAuthorFolder

from schemata import AuthorFolderSchema

class AuthorFolder(ATFolder):
    """Folder to contain the authors in the research database"""

    security = ClassSecurityInfo()

    implements(IAuthorFolder)

    meta_type = 'AuthorFolder'
    _at_rename_after_creation = True

    schema = AuthorFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(AuthorFolder, PROJECTNAME)
