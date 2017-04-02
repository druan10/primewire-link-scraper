# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib3, sys, re

if __name__ == "__main__":
    primewire_domain = 'http://www.primewire.ag/'
    episode_list_url = 'Insert url fragment here' #'watch-4131-The-Simpsons-online-free' for the simpsons for example
    primewire_url = primewire_domain + episode_list_url
    http = urllib3.PoolManager()
    r = http.request('GET', primewire_url)
    html = (r.data.decode('utf-8'))
    
    soup = BeautifulSoup(html) 

    print("Scraping Links and saving to ./results.txt")
    
    #Each page contains the external link hosts we'll need to test
    episode_page_urls = []

    #Gather the link pages we'll need to check
    for episode_div in soup.find_all('div', class_="tv_episode_item"):
        
        episode_subdirectory = re.search("tv.*episode\-\d+", str(episode_div.a))
        episode_page_urls.append(primewire_domain + episode_subdirectory.string[episode_subdirectory.start():episode_subdirectory.end()])
    
    working_links = [""]*len(episode_page_urls)
    
    #write links to file
    results_file = open("results.txt","w") 
    
    for url in episode_page_urls:
        
        results_file.write(url + "\n") 
        
    results_file.close();
    
    print("exit")
    sys.exit