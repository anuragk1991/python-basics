import re
import csv
import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
handler = logging.FileHandler('../log_files/bs4_scrape.log')

handler.setFormatter(formatter)
logger.addHandler(handler)

source = requests.get('https://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

with open('data.csv', 'w') as file:
	fields = ['title', 'published_at', 'content', 'url']
	csv_writer = csv.DictWriter(file, fieldnames=fields)
	csv_writer.writeheader()

	for article in soup.find_all('article'):
		title = article.header.h2.a.text
		published_at = article.header.p.time.text
		content = article.div.p.text

		print('Title: ', title)
		print('Published At: ', published_at)
		print('Content: ', content)
		print('')

		try:
			video_src = article.find('iframe', class_='youtube-player')['src']
			pattern = re.compile(r'/embed/([a-zA-Z0-9_-]+)\?')
			result = pattern.finditer(video_src)
			video_url = 'https://www.youtube.com/watch?v='
			for match in result:
				video_url += match.group(1)
		except Exception:
			video_url = None

		csv_writer.writerow({'title': title, 'published_at': published_at, 'content': content, 'url':video_url})
		logger.info('Data added to csv file -> Title: {}, published at : {}'.format(title, published_at))
