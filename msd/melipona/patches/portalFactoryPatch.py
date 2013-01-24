from Products.CMFPlone.FactoryTool import FactoryTool

FACTORY_INFO = '__factory__info__'

def _fixRequest(self):
    """Our before_publishing_traverse call mangles URL0.  This fixes up
    the REQUEST."""
    # Everything seems to work without this method being called at all...
    factory_info = self.REQUEST.get(FACTORY_INFO, None)
    if not factory_info:
        return
    stack = factory_info['stack']
    FACTORY_URL = self.REQUEST.URL
    URL = '/'.join([FACTORY_URL] + stack)
    self.REQUEST.set('URL', URL)
    
    url_list = URL.split('/')
    n = 0
    while len(url_list) > 0 and url_list[-1] != '':
        self.REQUEST.set('URL%d' % n, '/'.join(url_list))
        url_list = url_list[:-1]
        n = n + 1
    
    # # BASE1 is the url of the Zope App object
    n = len(self.REQUEST._steps) + 2
    base = FACTORY_URL
    for part in stack:
        base = '%s/%s' % (base, part)
        self.REQUEST.set('BASE%d' % n, base)
        n += 1
    # TODO fix URLPATHn, BASEPATHn here too
    # 

FactoryTool.__old_fixRequest = FactoryTool._fixRequest
FactoryTool._fixRequest = _fixRequest