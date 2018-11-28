class MyIterator(object):
    def __init__(self,step):
        self.step = step
    def next(self):
        """return the next ele"""
        if self.step==0:
            raise StopIteration
        self.step-=1
        return self.step
    def __iter__(self):
        return self