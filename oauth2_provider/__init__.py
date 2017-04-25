import pkg_resources


#__version__ = pkg_resources.require("django-oauth-toolkit")[0].version
VERSION = (0, 12, 0, 'final', 0)

__title__ = 'django-oauth-toolkit'
__version_info__ = VERSION
__version__ = '.'.join(map(str, VERSION[:3])) + ('-{}{}'.format(
    VERSION[3], VERSION[4] or '') if VERSION[3] != 'final' else '')
__author__ = 'Massimiliano Pippi, Federico Frenguelli'
__license__ = 'BSD'
__copyright__ = 'Copyright 2010-2017 Massimiliano Pippi, Federico Frenguelli'


default_app_config = "oauth2_provider.apps.DOTConfig"