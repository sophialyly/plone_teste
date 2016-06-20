# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from meu.produto.testing import MEU_PRODUTO_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that meu.produto is properly installed."""

    layer = MEU_PRODUTO_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if meu.produto is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'meu.produto'))

    def test_browserlayer(self):
        """Test that IMeuProdutoLayer is registered."""
        from meu.produto.interfaces import (
            IMeuProdutoLayer)
        from plone.browserlayer import utils
        self.assertIn(IMeuProdutoLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MEU_PRODUTO_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['meu.produto'])

    def test_product_uninstalled(self):
        """Test if meu.produto is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'meu.produto'))

    def test_browserlayer_removed(self):
        """Test that IMeuProdutoLayer is removed."""
        from meu.produto.interfaces import IMeuProdutoLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMeuProdutoLayer, utils.registered_layers())
