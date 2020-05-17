import concurrent.futures
import time
import requests

img_urls = [
	'https://images.unsplash.com/photo-1531003772135-4e2ea23ff14d', 
	'https://images.unsplash.com/photo-1585587309633-efa024307833',
	'https://images.unsplash.com/photo-1581230207770-33fff19553a9',
	'https://images.unsplash.com/photo-1584088743546-db0289ee9b07',
	'https://images.unsplash.com/photo-1571970449546-e3f94afe6abd',
	'https://images.unsplash.com/photo-1589703546423-1b9b38037a72'
]

def download_image(url):
	print(f'Downloading image from {url} ')
	filename = 'photos/photo_{}.jpg'.format(url.split('/')[-1])
	print(filename)
	img_data = requests.get(url).content

	with open(filename, 'wb') as img:
		img.write(img_data)
	print(f'Image ({url}) downloaded and saved')

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
	executor.map(download_image, img_urls)

end = time.perf_counter()

print(f'Task completed in {round(end-start,2)} seconds')