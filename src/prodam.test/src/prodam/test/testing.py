# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import prodam.test


class ProdamTestLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=prodam.test)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'prodam.test:default')


PRODAM_TEST_FIXTURE = ProdamTestLayer()


PRODAM_TEST_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PRODAM_TEST_FIXTURE,),
    name='ProdamTestLayer:IntegrationTesting'
)


PRODAM_TEST_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PRODAM_TEST_FIXTURE,),
    name='ProdamTestLayer:FunctionalTesting'
)


PRODAM_TEST_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PRODAM_TEST_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ProdamTestLayer:AcceptanceTesting'
)
