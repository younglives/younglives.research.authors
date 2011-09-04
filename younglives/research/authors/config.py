from Products.Archetypes.atapi import DisplayList

PROJECTNAME = 'younglives.research.authors'

ADD_PERMISSIONS = {
    'Author': 'YounglivesResearchAuthors: Add Author',
    'AuthorFolder': 'YounglivesResearchAuthors: Add AuthorFolder',
}

# vocabs for initial imports

VIETNAM_NAMES = DisplayList((
    ('Le', 'Thuc Duc'),
    ('Vu', 'Hoang Dat'),
    ('Nguyen', 'Hoai Chau'),
    ('Truong', 'Huyen Chi'),
    ('Nguyen', 'Ngoc Danh'),
    ('Nguyen', 'Ngoc P.'),
    ('Tran', 'Ngoc Ai Vy'),
    ('Vu', 'Thi Thanh Huong'),
    ('Tran', 'Ngo Minh Tam'),
    ('Lopez Boo', 'Florencia'),
))
