
"""modules are separate files with varibale/function definitions, which can be used via `import` and `from` """#docstring for the file

def adds(a, b):
    """add parameters together"""#docstring for the function
    return a+b
help(adds)


#(ai) environment
#pydoc module: show in the terminal
#pydoc -w module: wrote module.html
#start module.html

"""
import module
module.adds(3,4)

from module import adds
adds(3,4)
"""

a = 2
b = 3
a,b = b,a+b #same time executed
print(a,b) #3,5

#python caches inported modules in \sys.modules\, so running \import module\ a second time does not re-read the file. if you edit module.py and want the new version in the same session, use \improtlib.relaod\
import importlib
import module
module.adds(2,3)
#...edit and save module.py...
importlib.reload(module)
module.adds(2,3)

#reload updates the module object, but a name you already copied out of it with fron...import... still points to the old function
import importlib
from module import adds
adds(2,3)
#...edit and save module.py...
importlib.reload(module)
module.adds(2,3) #new
adds(2,3) #still old function
adds = module.adds # or again: form module import adds

"""In jupyter:auto-reload,run once at the top
%load_ext autoreload
%autoreload 2"""