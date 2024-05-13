books_list=[]
authors_set=set()
books_dict={}
books_list.append('python programing')
authors_set.add('john smith')
books_dict['python programing']='john smith'

books_list.append('data structure and algorim')
authors_set.add('jone doe')
books_dict['data structure and algorithms']='jone doe'

books_list.append('machine learning basics')
authors_set.add('alice johnson')
books_dict['machine learning basics']='alice johnson'

search_title=input('Enter the title of the books:')
if search_title in books_list:
    print(f'book found! {books_dict[search_title]}')
else:
    print('Book not found')

print('List of Books')
for book in books_list:
    print(book)

remove_title=input('Enter the title of the book to remove:')
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list=books_dict[remove_title]
    authors_list.remove(remove_title)
    del books_dict[remove_author]
    print('Books removed sucessfully!')
    print('Books available:' , books_list)

else:
    print('Book not found')       