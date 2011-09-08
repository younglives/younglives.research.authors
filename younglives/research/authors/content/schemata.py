from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import BooleanField
from Products.Archetypes.atapi import BooleanWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget

from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

AuthorFolderSchema = ATFolderSchema.copy() + Schema((

))

AuthorSchema = ATContentTypeSchema.copy() + Schema((

    StringField('personalNames',
        required = False,
        searchable = False,
        widget = StringWidget(
            label='Personal Names',
            format='checkbox',
        )
    ),

    StringField('familyName',
        required = False,
        searchable = False,
        widget = StringWidget(
            label='Family Name',
            format='checkbox',
        )
    ),

    BooleanField('nameOrder',
        required = False,
        searchable = False,
        widget = BooleanWidget(
            label='Name order',
            description='Tick this if the name order should be family name followed by personal names',
            format='checkbox',
        )
    ),

    StringField('emailAddress',
        required = False,
        searchable = False,
        widget = StringWidget(
            label='Email Address',
        )
    ),

))

AuthorSchema['title'].required = 0
AuthorSchema['title'].widget.visible = 0
AuthorSchema['description'].widget.visible = 0

finalizeATCTSchema(AuthorSchema)
