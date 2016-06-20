# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from prodam.test1.testing import PRODAM_TEST1_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that prodam.test1 is properly installed."""

    layer = PRODAM_TEST1_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if prodam.test1 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'prodam.test1'))

    def test_browserlayer(self):
        """Test that IProdamTest1Layer is registered."""
        from prodam.test1.interfaces import (
            IProdamTest1Layer)
        from plone.browserlayer import utils
        self.assertIn(IProdamTest1Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PRODAM_TEST1_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['prodam.test1'])

    def test_product_uninstalled(self):
        """Test if prodam.test1 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'prodam.test1'))

    def test_browserlayer_removed(self):
        """Test that IProdamTest1Layer is removed."""
        from prodam.test1.interfaces import IProdamTest1Layer
        from plone.browserlayer import utils
        self.assertNotIn(IProdamTest1Layer, utils.registered_layers())
