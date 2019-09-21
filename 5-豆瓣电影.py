import requests
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100'
res = requests.get(url).json()
for i in res:
    title = i.get('title')
    pic = i.get('cover_url')
    actors = str(i.get('actors')).replace('[','').replace(']','').replace(',','、').replace("'","")
    time = i.get('release_date')
    country = i.get('regions')[0]
    types = str(i.get('types')).replace('[','').replace(']','').replace(',','/').replace("'","")
    url = i.get('url')
    comment = i.get('vote_count')
    score = i.get('score')

    s = f'影名：{title}\n'+f'主演：{ actors}\n'+f'{time}\t {country} \t{types}\n'+f'{score}\t{comment}评论\n'+f'链接：{url}\n\n'
    with open('douban.txt','a',encoding='utf-8')as f:
        f.write(s)



