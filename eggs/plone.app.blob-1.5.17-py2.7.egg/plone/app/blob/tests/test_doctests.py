import unittest
import doctest

from plone.app.blob.tests.layer import BlobLayer, BlobReplacementLayer, BlobLinguaLayer
from plone.app.blob.tests.utils import hasLinguaPlone

from plone.testing import layered


def test_suite():
    optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
    suite = unittest.TestSuite()
    suite.addTest(layered(
        doctest.DocFileSuite(
           'README.txt', package='plone.app.blob',
           optionflags=optionflags),
           layer=BlobLayer))

    for filename in ['replacement-types.txt', 'transforms.txt']:
        suite.addTest(layered(
            doctest.DocFileSuite(
               filename, package='plone.app.blob.tests',
               optionflags=optionflags),
               layer=BlobReplacementLayer))

    if hasLinguaPlone():
        suite.addTest(layered(
            doctest.DocFileSuite(
               'linguaplone.txt', package='plone.app.blob.tests',
               optionflags=optionflags),
               layer=BlobLinguaLayer)
        )
    return suite
