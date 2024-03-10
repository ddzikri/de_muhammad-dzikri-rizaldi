def collect_chars(word, rooms):
    if not word or rooms <= 0:
        return "TidakSesuai"
    ruang = rooms // len(word)
    ruang1 = rooms % len(word)
    hasil = word * ruang + word[:ruang1]
    return hasil

print(collect_chars("alta", 10))  # altaaltaal
print(collect_chars("sepulsa", 20))  # sepulsasepulsasepuls
print(collect_chars("sepulsamantap", 20))  # sepulsamantapsepulsa