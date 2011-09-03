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

registerType(Author, PROJECTNAME)
