import os
import glob

def __list_all_modules():
    work_dir = os.path.dirname(__file__)
    module_paths = glob.glob(os.path.join(work_dir, "*", "*.py"))

    all_modules = [
        os.path.splitext(os.path.relpath(f, work_dir).replace(os.path.sep, "."))[0]
        for f in module_paths
        if os.path.isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules

ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
