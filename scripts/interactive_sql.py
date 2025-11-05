#!/usr/bin/env python3
"""
CLI script for interactive SQL shell
Usage: python scripts/interactive_sql.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.interactive_sql import main

if __name__ == "__main__":
    main()

