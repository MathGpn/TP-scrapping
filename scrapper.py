from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from pytube import extract
import json
import argparse

class Scrap:
    def __init__(self, web):
        s=Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument('--headless')
        #options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=s, chrome_options=options)
        time.sleep(2)
        self.driver.get(web)
        self.soup = BeautifulSoup(self.driver.page_source, "html.parser")
        self.web = web

    def get_title(self):
        title=self.soup.find("meta", itemprop="name")["content"]
        return title

    def get_author(self):
        auteur = self.soup.find("span", itemprop="author").next.next["content"]
        return auteur

    def get_likes(self):
        raw_like = self.soup.find("button", {"class": "yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"})
        like = raw_like['aria-label']
        if like[0] == 'C':
            nb_like = like.split("Cliquez sur \"J'aime\" pour cette vidéo comme ")[1].split(" autres internautes.")[0]
        else:
            nb_like = like.split("like this video along with ")[1].split(" other people")[0]
        return nb_like

    def get_description(self):
        self.driver.get(self.web)
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
        element.click()
        element = self.driver.find_element(By.XPATH, "//*[@id=\"expand\"]")
        element.click()
        time.sleep(1)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        descDiv = soup.find("yt-formatted-string", {"class": "style-scope ytd-text-inline-expander"})
        return descDiv.text

    def get_links(self):
        self.driver.get(self.web)
        time.sleep(1)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        descDiv = soup.find("yt-formatted-string", {"class": "style-scope ytd-text-inline-expander"})
        listLiens = []
        liens = descDiv.find_all("a")
        for lien in liens:
            if lien["href"][0] == '/':
                listLiens.append("https://www.youtube.com"+lien["href"])
            else:
                listLiens.append(lien["href"])
        return listLiens


    def get_video_id(self):
        id=extract.video_id(self.web)
        return id

    def get_comms(self):
        N = 5
        commentaires = []
        element = self.driver.find_element(By.XPATH, "//*[@id=\"comments\"]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        commentsList = soup.find_all("ytd-comment-thread-renderer", {"class": "style-scope ytd-item-section-renderer"}, limit = N)
        while commentsList == []:
            time.sleep(1)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            commentsList = soup.find_all("ytd-comment-thread-renderer", {"class": "style-scope ytd-item-section-renderer"}, limit = N)
        for comment in commentsList:
            commentaires.append(comment.find("yt-formatted-string", {"id": "content-text"}).text)
        return commentaires


def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', action="store")
    parser.add_argument('--output', action="store")

    args = parser.parse_args()
    inp = args.input
    out = args.output

    #web = 'https://www.youtube.com/watch?v=K6q2Tryw7bs'  
    url_tab = []
    f = open(inp)
    data = json.load(f)
    for i in data["videos_id"]:
        url_tab.append('https://www.youtube.com/watch?v='+i)
    f.close()

    data= []
    for url in url_tab:
        #result1, result2 = get_page(url)
        obj = Scrap(url)
        titre = obj.get_title()
        auteur = obj.get_author()
        like = obj.get_likes()
        description = obj.get_description()
        link = obj.get_links()
        id = obj.get_video_id()
        comms = obj.get_comms()

        dict = {}
        dict['Titre'] = titre
        dict['Auteur'] = auteur
        dict['Likes'] = like
        dict['Description'] = description
        dict['Liens'] = link
        dict['Video ID'] = id
        dict['Commentaires'] = comms

        data.append(dict)

    with open(out, "w") as file:
        file.write(json.dumps(data, indent=4))



if __name__ == '__main__':
    main()
