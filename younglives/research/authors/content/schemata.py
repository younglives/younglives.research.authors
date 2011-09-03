from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import BooleanField
from Products.Archetypes.atapi import BooleanWidget
from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import MultiSelectionWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget

from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

AuthorFolderSchema = ATFolderSchema.copy() + Schema((

))

AuthorSchema = ATContentTypeSchema.copy() + Schema((

))

finalizeATCTSchema(AuthorSchema)
