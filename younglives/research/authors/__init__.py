from zope.i18nmessageid import MessageFactory

from Products.Archetypes.atapi import listTypes, process_types
from Products.CMFCore.utils import ContentInit

from younglives.research.authors import config

_ = MessageFactory('younglives.research.authors')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

    from content.author import Author
    from content.author_folder import AuthorFolder

    content_types, constructors, ftis = process_types(
        listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        ContentInit('%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype, ),
            permission=config.ADD_PERMISSIONS[atype.portal_type],
            extra_constructors=(constructor,),
            ).initialize(context)
