from GoogleNews import GoogleNews
googlenews = GoogleNews()
googlenews = GoogleNews(period='7d')
googlenews.search('marvel')
result=googlenews.result()

for x in result:
    print('\n','-'*50,'\n')
    print("Title--", x['title'])
    print("Date/Time--", x['date'])
    print("Description--", x['desc'])
    print("Link--", x['link'])