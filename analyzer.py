#!/usr/bin/env python3
"""
Security File Analyzer
Provides basic file integrity checking
"""

import hashlib
import sys
import os

def analyze_file(filepath):
    """Analyze file for security anomalies"""
    try:
        with open(filepath, 'rb') as f:
            data = f.read()
            hash_md5 = hashlib.md5(data).hexdigest()
            hash_sha256 = hashlib.sha256(data).hexdigest()
            
        print(f"MD5: {hash_md5}")
        print(f"SHA256: {hash_sha256}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <filepath>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("File not found")
        sys.exit(1)
    
    analyze_file(filepath)

if __name__ == "__main__":
    main()
