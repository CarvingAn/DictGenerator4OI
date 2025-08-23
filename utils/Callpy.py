import sys,_io
from PySide6.QtWidgets import QMessageBox


class CallPy():
    def __init__(self,path):
        try:
            with open(path,'r') as f:
                self.code=f.read()
        except Exception as e:
            QMessageBox.critical(None,"Error",f"An error occurred while reading files: {e}")
    def __call__(self,data):
        a=sys.stdin,sys.stdout
        sys.stdin = _io.StringIO(str(data)+"\n")
        sys.stdout = _io.StringIO()
        try:
            exec(self.code)
            result = sys.stdout.getvalue()
        except ModuleNotFoundError:
            QMessageBox.critical(None,"Error","Please do not use third-party libs.\n{e}")
        except Exception as e:
            QMessageBox.critical(None,"Error",f"An error occurred while executing code: {e}")
        finally:
            sys.stdin,sys.stdout=a
        return result