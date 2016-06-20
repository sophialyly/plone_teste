# Zope imports
from zope.interface import Interface
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class Teste(BrowserView):
    """ Render the title and description of item only (example)
    """
    index = ViewPageTemplateFile("static/teste.pt")
    def render(self):
        return self.index()

    def __call__(self):
        return self.render()
