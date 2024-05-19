from googlesearch import search

query = input("Type your search here: ")

for user_search in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(user_search)
