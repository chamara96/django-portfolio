from collections import OrderedDict

CONSTANCE_CONFIG = OrderedDict([
    ('SITE_TITLE', ('---', 'Site Title')),
    ('DESCRIPTION', ('---', 'META Description')),
    ('KEYWORDS', ('---', 'META Keywords')),
    ('AUTHOR', ('---', 'META Author')),
    ('FOOTER_TEXT', ('---', 'Footer Text')),
])

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
    ('General Options', ('SITE_TITLE', 'FOOTER_TEXT')),
    ('Site META', ('DESCRIPTION', 'KEYWORDS', 'AUTHOR')),
])
