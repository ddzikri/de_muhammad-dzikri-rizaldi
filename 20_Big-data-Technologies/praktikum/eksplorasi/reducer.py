#!/usr/bin/env python

import sys

# Membaca input dari stdin
for line in sys.stdin:
    # Memecah pasangan kunci-nilai menjadi kunci dan nilai
    word, _ = line.strip().split()
    
    # Memeriksa apakah kata merupakan palindrom
    if word == word[::-1]:
        print(word, "True")
    else:
        print(word, "False")