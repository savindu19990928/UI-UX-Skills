#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Top-level runner for UI/UX Pro Max Design Intelligence Search.
Proxies all arguments to skills/ui-ux-pro-max/scripts/search.py.
"""
import sys
import subprocess
from pathlib import Path

SKILL_SCRIPT = Path(__file__).parent.parent / "skills" / "ui-ux-pro-max" / "scripts" / "search.py"

if __name__ == "__main__":
    if not SKILL_SCRIPT.exists():
        print(f"Error: Could not find search engine at {SKILL_SCRIPT}", file=sys.stderr)
        sys.exit(1)
    
    cmd = [sys.executable, str(SKILL_SCRIPT)] + sys.argv[1:]
    proc = subprocess.run(cmd)
    sys.exit(proc.returncode)
