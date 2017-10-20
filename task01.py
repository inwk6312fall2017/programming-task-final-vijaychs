with open("Book1.txt","r") as f1, open("Book2.txt","r") as f2, open("Book3.txt","r") as f3:
	book_1 = sorted(f1.read().split())
	book_2 = sorted(f2.read().split())
	book_3 = sorted(f3.read().split())
	all_books = []
	all_books.extend(book_2)
	all_books.extend(book_3)
	
#	print(all_books)
	
	longest_of_books = ""

	for each_word in all_books:
		if len(each_word) > len(longest_of_books):
			longest_of_books = each_word
	print("the longest word in books: ",longest_of_books)
