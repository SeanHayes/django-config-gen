#!/usr/bin/env python
import sys
try:
    from django.core.management import execute_from_command_line
except ImportError:
    from django.core.management import execute_manager as execute_from_command_line

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
