class _globe: 
    def __setattr__(self, name, value): 
        self.__dict__[name]=value 
import sys
sys.modules[__name__] = _globe()
