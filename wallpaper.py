from bs4 import BeautifulSoup
import requests
import wget

class wallpaper:
    def __init__(self, url, size):
        self.url = url
        self.size = size

    def month_url(self, month):
        page = requests.get(self.url).text
        soup = BeautifulSoup(page, "lxml")
        for link in soup.findAll("a", {"class" : "cr"}):
            if month in str(link.get("href")):
                self.m_url = link.get("href")

    def __image_url(self):
        page = requests.get(self.m_url).text
        soup = BeautifulSoup(page, "lxml")
        images = []
        for link in soup.findAll("a"):
            img = str(link.get("href"))
            if self.size in img and "nocal" not in img:
                images.append(link.get("href"))
        return images

    def download_img(self):
        img_url = self.__image_url()
        for img in img_url:
            wget.download(img)
        
if __name__ == "__main__":
    wall = wallpaper("https://www.smashingmagazine.com/tag/wallpapers", "1680x1050")
    wall.month_url("may")
    wall.download_img()
