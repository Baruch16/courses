import os
import requests
from bs4 import BeautifulSoup
import random
from tqdm import tqdm

# A function to get the urls of all images in a given link
def get_images_urls(link):
	images = []
	html = requests.get(link)
	if html.status_code==200:
		html_page = html.text
		soup = BeautifulSoup(html_page,'html.parser')
		links = soup.find_all('img')
		for img in soup.findAll('img'):
			images.append(fix_url(img.get('src')))
	return images

# A function to get the urls of all links in a given link
def get_urls_links(url_link):
	urls = []
	html = requests.get(url_link)
	if html.status_code==200:
		html_page = html.text
		soup = BeautifulSoup(html_page,'html.parser')
		links = soup.find_all('a')
		for tag in links:
			url = tag.get('href',None)
			if url is not None and not url.startswith("#"):
				urls.append(fix_url(url))
	return urls

# A function to download all images from the function above + using tqdm to monitor the progress
def downlods_images(images_urls, folder_name):
	os.chdir(folder_name) 
	for i in tqdm(range(len(images_urls))):
		response = requests.get(images_urls[i])
		if response.status_code==200:
			fp = open(f'{i}.png', 'wb')
			fp.write(response.content)
			fp.close()
	os.chdir('..')
# A function to fix broken urls 
def fix_url(url_link):
	prefix_wiki = 'https://en.wikipedia.org'
	
	if url_link.startswith('https'):
		return url_link
	elif url_link.startswith('//'):
		url_fix_link = 'https:' + url_link
	elif url_link.startswith('/wiki') or url_link.startswith('/static') or url_link.startswith('/w/'):
		url_fix_link = prefix_wiki + url_link
	else:
		url_fix_link = url_link
	return url_fix_link
	
# A function to remove any duplicate urls 	
def remove_duplicates(list_urls):
	result = []
	for url in list_urls:
		if url not in result:
			result.append(url)
	return result
	
# A function to retrun and clean the folder names from the last part of the url
def folder_name(page_link):
	split_url = page_link.split('/')
	if split_url[-1] == '':
		split_url[-1]=split_url[-2]
	split_url[-1].translate({ord('i'):None for i in '1234567890`~@#$%^&*'})
	return split_url[-1]
	
# A function that is responsible for the crawler itself by creting a loop to open the directories inside of each other bt the specified depth
def crawl(page_link, depth, width):
		name_of_folder = folder_name(page_link)
		if not os.path.isdir(name_of_folder):
			print(name_of_folder)
			os.mkdir(name_of_folder)
			urls_images = get_images_urls(page_link)
			uniqe_urls_images = remove_duplicates(urls_images)
			downlods_images(uniqe_urls_images, name_of_folder, )
			if depth > 1 :
				os.chdir(name_of_folder)
				urls_links = get_urls_links(page_link)
				width_places = random.sample(range(0 , len(urls_links)) ,min(width,len(urls_links)))
				for width_place in width_places:
					crawl(urls_links[width_place], depth-1, width)
				os.chdir('..')
def main ():
	page_link = input("enter your wiki web page")
	width = int(input(" enter width"))
	depth = int(input(" enter depth"))
	crawl(page_link, width, depth)
	
if __name__=="__main__":
	main()


