
import os,sys
import pytest
import traceback

def find_em():
    import importlib
    spec = importlib.util.find_spec('pynet')
    if spec is None:
        return False
    else:
        return True

def good_import():
    import pynet
    return True

def load_em():
    if not find_em():
        filepath = os.path.abspath(__file__)
        dirpath = os.path.dirname(filepath)
        rootpath = os.path.dirname(dirpath)
        srcpath = os.path.join(rootpath,'src')
        sys.path.insert(0,srcpath)
    assert good_import()



def test_import():
    import importlib
    spec = importlib.util.find_spec('pynet')
    if spec is not None:
        if 'site-packages' in spec.origin:
            ### Finding the installed version, skip
            return
        else:
            assert spec.origin.endswith('src/pynet/__init__.py')
    else:
        with pytest.raises(ImportError):
            import pynet
        load_em()

