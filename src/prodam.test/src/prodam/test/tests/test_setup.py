# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from prodam.test.testing import PRODAM_TEST_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that prodam.test is properly installed."""

    layer = PRODAM_TEST_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if prodam.test is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'prodam.test'))

    def test_browserlayer(self):
        """Test that IProdamTestLayer is registered."""
        from prodam.test.interfaces import (
            IProdamTestLayer)
        from plone.browserlayer import utils
        self.assertIn(IProdamTestLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PRODAM_TEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['prodam.test'])

    def test_product_uninstalled(self):
        """Test if prodam.test is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'prodam.test'))

    def test_browserlayer_removed(self):
        """Test that IProdamTestLayer is removed."""
        from prodam.test.interfaces import IProdamTestLayer
        from plone.browserlayer import utils
        self.assertNotIn(IProdamTestLayer, utils.registered_layers())
