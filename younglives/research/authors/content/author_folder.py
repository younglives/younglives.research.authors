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
        plone_tool = getToolByName(self, 'plone_utils', None)
        workflow_tool = getToolByName(self, 'portal_workflow', None)
        author_list = authors.split(',')
        for author in author_list:
            alternative_order = False
            author = author.strip()
            names = author.split(' ')
            first_name = names[0]
            if first_name in VIETNAM_NAMES:
                alternative_order = True
                family_name = names[0]
                personal_names = ' '.join(names[1:])
                full_name = family_name + ' ' + personal_names
                full_name = plone_tool.normalizeString(full_name)
                results = self.getFolderContents({'id':'full_name'})
            elif names[-1] == 'Boo':
                family_name = 'Lopez Boo'
                personal_names = ' '.join(names[:-2])
                full_name = personal_names + ' ' + family_name
                full_name = plone_tool.normalizeString(full_name)
                results = self.getFolderContents({'id':'full_name'})
            else:
                personal_names = ' '.join(names[:-1])
                family_name = names[-1]
                full_name = personal_names + ' ' + family_name
                full_name = plone_tool.normalizeString(full_name)
                results = self.getFolderContents({'id':'full_name'})
            if results:
                # author already exists
                objects.append(results[0].getObject())
                continue
            unique_id = self.generateUniqueId('Author')
            new_id = self.invokeFactory('Author', unique_id)
            object = self[new_id]
            if alternative_order:
                object.setNameOrder(True)
            object.setFamilyName(family_name)
            object.setPersonalNames(personal_names)
            object._renameAfterCreation()
            object.unmarkCreationFlag()
            workflow_tool.doActionFor(object,'publish',comment='Published on initial import')
            object.reindexObject()
            objects.append(object)
        return objects

registerType(AuthorFolder, PROJECTNAME)
