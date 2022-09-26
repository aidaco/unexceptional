from importlib.machinery import PathFinder

SILENT = True


def excepthook(fn):
    def inner(*args, **kwargs):
        if not SILENT:
            fn(*args, **kwargs)

    return inner


def hooked_finder(target_name, hook):
    find = PathFinder.find_spec

    def find_spec(name, *args, **kwargs):
        if target_name in name:
            try:
                spec = find(name, *args, **kwargs)
                if spec is None:
                    return None
                exec_module = spec.loader.exec_module

                def hooked_exec(mod):
                    exec_module(mod)
                    hook(mod)

                spec.loader.exec_module = hooked_exec
            except Exception as e:
                print(e)
            return spec

    p = PathFinder()
    p.find_spec = find_spec
    return p


def exechook(ipy):
    try:
        fn = ipy.InteractiveShell.showtraceback

        def silence(*args, **kwargs):
            if not SILENT:
                fn(*args, **kwargs)

        ipy.InteractiveShell.showtraceback = silence
    except Exception as e:
        print(e)


def install(sys):
    sys.excepthook = excepthook(sys.__excepthook__)
    sys.meta_path.insert(0, hooked_finder("IPython.core.interactiveshell", exechook))
