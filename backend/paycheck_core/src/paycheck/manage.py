#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pprint import pprint


def main():
    """Run administrative tasks."""
    import pdb

    # project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    # src_root = os.path.join(project_root, "src")
    #
    # if src_root not in sys.path:
    #     sys.path.append(src_root)

    if src_root not in sys.path:
        sys.path.append(src_root)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
