#!/usr/bin/env python3

import subprocess

print("Starting server on http://localhost:8000")
subprocess.run(["python", "-m", "http.server", "8000"])