class Redprint:
    def __init__(self,name):
        self.name=name
        self.mound=[]
    def route(self,rule,**options):
        def decorator(f):
            self.mound.append((rule,f,options))
            return f
        return decorator
    def register(self,bp,url_prefix=None):
        if url_prefix is None:
            url_prefix = '/'+self.name
        for rule, f, options in self.mound:
            # endpoint机制。这里连接符不能用 . 系统不让过
            endpoint = self.name +'+'+options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
