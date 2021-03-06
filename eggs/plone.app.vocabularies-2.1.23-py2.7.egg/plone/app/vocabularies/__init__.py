# -*- coding: utf-8 -*-
from plone.app.vocabularies.interfaces import ISlicableVocabulary
from zope.interface import directlyProvides
from zope.interface import implementer


@implementer(ISlicableVocabulary)
class SlicableVocabulary(object):
    """
    A tokenized vocabulary in which the results can be sliced.
    This class does not implement a complete vocabulary. Instead you use
    this class as a mixin to your vocabulary class.
    This mixin class expects to be used with something resembling
    a SimpleVocabulary. It accesses internal members like _terms
    """

    def __init__(self, terms=[], *interfaces):
        self._terms = terms
        if interfaces:
            directlyProvides(self, *interfaces)

    def __getitem__(self, start, stop=None):
        if isinstance(start, slice):
            slice_inst = start
            start = slice_inst.start
            stop = slice_inst.stop
        elif not stop:
            return self._terms[start]

        # sliced up
        return self._terms[start:stop]

    def __len__(self):
        return len(self._terms)
