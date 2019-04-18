import os
import inspect

class open_makedirs(object):
    """
    Open a file like open, but make all directories on the way.
    """
    def __init__(self,
                  filename,
                  mode='r',
                  buffering=-1,
                  encoding=None,
                  errors=None,
                  newline=None,
                  closefd=True,
                  opener=None,
                  exist_ok=False):
        os.makedirs(os.path.dirname(filename),
                    exist_ok=exist_ok)
        self.f = open(filename,
                      mode=mode,
                      buffering=buffering,
                      encoding=encoding,
                      errors=errors,
                      newline=newline,
                      closefd=closefd,
                      opener=opener)

    def __enter__(self):
        return self.f

    def __exit__(self, type, value, traceback):
        self.f.close()


def here():
    """
    Gets the absolute path of the current file's directory.
    """
    return inspect.getouterframes(inspect.currentframe())[1][1]
