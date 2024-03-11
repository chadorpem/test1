from queue import LifoQueue
backward_history=LifoQueue()
forward_history=LifoQueue()
current_page=None
NoOfVisit=int(input('Enter the number of url history:'))
print('Enter URLS to visit:')
for i in range(NoOfVisit):
    url=input('URL:')
    print(f'visiting {url}')
    backward_history.put(current_page)
    current_page=url
    print(f'current_page:{current_page}')
while input('Do you want to go back(yes/no)').lower()=='yes':
    if not backward_history.empty():
        forward_history.put(current_page)
        current_page=backward_history.get()
        print(f'going back to{current_page}')
else:
    print('No forward page available')
