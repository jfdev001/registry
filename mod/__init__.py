import importlib.util
import os 
import pdb


# this calls the register function and populates the registry
import mod.plot 

def import_from_path(module_name, file_path):
    # Load the module specification
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    # Create a new module based on the specification
    module = importlib.util.module_from_spec(spec)
    # Execute the module in its own namespace
    spec.loader.exec_module(module)
    return module

fpath = os.path.realpath(__file__)
if ".venv" in fpath:
    print("i'm a package of a project!")
    project_dir = fpath.split(".venv")[0]
    print(project_dir)
    print("project dir:", project_dir)
    register_fpath = os.path.join(project_dir, ".register")
    if os.path.exists(register_fpath):
        with open(register_fpath, "r") as fp:
            for path_to_module_with_register_decorators in fp.readlines():
                path_to_module_with_register_decorators = \
                    path_to_module_with_register_decorators.strip()
                # absolute path
                if os.path.exists(path_to_module_with_register_decorators):
                    import_path = path_to_module_with_register_decorators
                # otherwise try relative path
                elif os.path.exists(
                    os.path.join(project_dir, 
                        path_to_module_with_register_decorators)):
                    import_path = os.path.join(
                        project_dir, path_to_module_with_register_decorators) 
                else:
                    raise ValueError(f"{path_to_module_with_register_decorators} dne!") 
                module_name = os.path.basename(import_path.rstrip(".py"))
                import_from_path(module_name, import_path)       
else:
    print("i'm in development repo!") 
