#!/usr/bin/env python

import sys

# Membaca input dari stdin
for line in sys.stdin:
    # Memecah baris menjadi kata-kata
    words = line.strip().split()
    
    # Memproses setiap kata
    for word in words:
        # Mengirimkan pasangan kunci-nilai ke stdout
        print(word, "1")
