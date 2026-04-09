# install functon - install.py

# Imports of import.
import importlib
import subprocess
import sys

# Defines a function that installs any required uninstalled libraries
def install(package):
    try:
        importlib.import_module(package)        # The function first tries to import the module
        print(f"{package} already installed")   # If the import is successful then print
    except ImportError:
        print(f"Installing {package}...")       # If the import failed then the lib is not installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])    # Installs lib