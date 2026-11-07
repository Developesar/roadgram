"""Entry point for PyInstaller (see build_exe.ps1). For normal use: `python -m tgpm` or the installed `tgpm`."""
import sys

from tgpm.cli import main

if __name__ == "__main__":
    sys.exit(main())
