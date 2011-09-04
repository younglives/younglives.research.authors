import os
from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType
from Products.CMFCore.utils import getToolByName

from younglives.research.authors import permissions
from younglives.research.authors.config import PROJECTNAME
from younglives.research.authors.interfaces.author_folder import IAuthorFolder

from schemata import AuthorFolderSchema

# only needed for import
from younglives.research.authors.config import VIETNAM_NAMES

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

#only needed for import
    def _createAuthors(self, authors):
        """Create the authors if they don't already exist"""
        objects = []
        portal_catalog = getToolByName(self, 'portal_catalog')
        plone_tool = getToolByName(self, 'plone_utils', None)
        author_list = authors.split(',')
        for author in author_list:
            author = author.strip()
            title = plone_tool.normalizeString(author)
            results = portal_catalog(id=title)
            if results:
                # author already exists
                objects.append(results[0].getObject())
                continue
            unique_id = self.generateUniqueId('Author')
            new_id = self.invokeFactory('Author', unique_id)
            object = self[new_id]
            try:
                names = author.split(' ')
            except TypeError:
                import pdb;pdb.set_trace()
            family_name = names[-1]
            if family_name in VIETNAM_NAMES:
                family_name = names[0]
                personal_names = names[1:]
                object.setNameOrder(True)
            elif family_name == 'Boo':
                family_name = 'Lopez Boo'
                personal_names = ' '.join(names[:-2])
            else:
                personal_names = ' '.join(names[:-1])
            object.setFamilyName(family_name)
            object.setPersonalNames(personal_names)
            object._renameAfterCreation()
            object.unmarkCreationFlag()
            object.reindexObject()
            objects.append(object)
        return objects

registerType(AuthorFolder, PROJECTNAME)
