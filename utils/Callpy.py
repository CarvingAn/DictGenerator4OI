import sys,_io
class CallPy():
    def __init__(self,path):
        with open(path,'r') as f:
            self.code=f.read()
    def __call__(self,data):
        a=sys.stdin,sys.stdout
        sys.stdin = _io.StringIO(str(data)+"\n")
        sys.stdout = _io.StringIO()
        try:
            exec(self.code)
            result = sys.stdout.getvalue()
        finally:
            sys.stdin,sys.stdout=a
        return result