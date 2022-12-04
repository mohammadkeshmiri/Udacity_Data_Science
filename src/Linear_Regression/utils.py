
import os
import inspect

def change_wd_to_current_file():
    """
    Change working directory to caller path.
    """

    frame = inspect.stack()[1]
    p = frame[0].f_code.co_filename
    abspath =  os.path.realpath(p)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
