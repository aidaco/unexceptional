# Unexceptional

Tired of all those pesky uncaught Exceptions?

````
pip install unexceptional
````
 
*In the REPL,*  
*In the CLI,*  
*In IPython & Jupyter,*  
__No exceptions.__ 

## *How do I escape this fresh hell?*
```
pip uninstall unexceptional
```

## What is even happening?

In order to achieve transparency to the user, this package is invoked at every interpreter startup by means of an included .pth file.
  
For the CPython interpreter, `sys.excepthook` is overridden with a no-op.
  
_For IPython, a crime is committed:_  
  
Because the .pth file is invoked before IPython, a bastardized `importlib.abc.MetaPathFinder` is inserted into `sys.meta_path` to intercept future imports of `IPython.core.interactiveshell`.
The `InteractiveShell.showtraceback` method is then overridden with the no-op after the module is executed.
