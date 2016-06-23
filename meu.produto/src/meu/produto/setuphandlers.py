# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer
from collective.transmogrifier.transmogrifier import Transmogrifier


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'meu.produto:uninstall',
        ]

# def setupVarious(context):
#     if context.readDataFile('noticias.csv') is None:
#         return
#     transmogrifier = Transmogrifier(context.getSite())
#     transmogrifier('Zap Event Import')

def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.
