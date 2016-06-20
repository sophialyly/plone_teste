# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import meu.produto


class MeuProdutoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=meu.produto)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'meu.produto:default')


MEU_PRODUTO_FIXTURE = MeuProdutoLayer()


MEU_PRODUTO_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MEU_PRODUTO_FIXTURE,),
    name='MeuProdutoLayer:IntegrationTesting'
)


MEU_PRODUTO_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MEU_PRODUTO_FIXTURE,),
    name='MeuProdutoLayer:FunctionalTesting'
)


MEU_PRODUTO_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MEU_PRODUTO_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='MeuProdutoLayer:AcceptanceTesting'
)
