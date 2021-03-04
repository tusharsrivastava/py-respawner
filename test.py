#!/usr/bin/env python
import os
import sys

print(f"Hello World! from PID {os.getpid()}")

try:
    while True:
        k = input("Press 'r' (then Enter) to raise an exception or 'q' to normally terminate: ")
        if k == 'r':
            raise Exception("Unhandled Exception")
        elif k == 'q':
            break
except EOFError:
    sys.exit(0)
except Exception:
    raise
