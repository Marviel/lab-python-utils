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


def heref():
    """
    Gets the absolute path of the calling context's file
    """
    return inspect.getouterframes(inspect.currentframe())[1][1]


def here():
    """
    Gets the absolute path of the calling context's directory.

    Will throw with an ugly error message if there is no directory, such as in the case of stdin.
    """
    return os.path.dirname(inspect.getouterframes(inspect.currentframe())[1][1])


