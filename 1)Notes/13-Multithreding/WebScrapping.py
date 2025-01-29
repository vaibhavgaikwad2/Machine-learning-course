# Web scrapping involves making numerous network request to fetch
# web pages. These tasks are I/O bound they spend a lot of
# time waiting for responses from servers. Multithreading can significantly
# improves the performance by allowing multiple web pages to fetched concurrently

'''

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''



import threading
import requests
from bs4 import BeautifulSoup


url=[
    

'https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/'

]

def fetched_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"Fetched :{soup.text} from url")
    


threads=[]

for url in url:
    thread=threading.Thread(target=fetched_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")


