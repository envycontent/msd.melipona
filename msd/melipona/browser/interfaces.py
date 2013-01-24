from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface
from zope.viewlet.interfaces import IViewletManager



class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
    
class IBelowFooter(IViewletManager):
    """A viewlet manager below the portal footer
    """


class IMeliponaLayoutPolicy(Interface):
    """Interface to provide utility layout methods
    """
    
    def get_content_column_class(column_left, column_right):
        """Get the classes for the middle column
           calculating the width from the presence of left or right cols
        """
        
    def get_column_left_class():
        """Return classes for the left column    
        """
        
    def get_column_right_class():
        """Return classes for the right column
        """