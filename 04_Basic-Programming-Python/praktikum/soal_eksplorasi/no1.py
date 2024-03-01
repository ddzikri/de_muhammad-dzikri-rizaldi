print(15 *"*")
print("Program Anagram")
print(15 *"*")

def anagram(kata1, kata2):
	if(sorted(kata1)== sorted(kata2)):
		print(f"Output :\nAnagram\npembahasan: \nkata {kata1} merupakan anagram dari kata {kata2} karena jumlah frekuensi huruf pada dua kata tersebut adalah sama") 
	else:
	    print(f"Output :\nBukan Anagram\npembahasan: \nkata {kata1} bukan merupakan anagram dari kata {kata2} karena jumlah frekuensi huruf pada dua kata tersebut berbeda") 

kata1 = input("Masukkan Kata - 1 : ")
kata2 = input("Masukkan Kata - 2 : ")

anagram(kata1, kata2)
