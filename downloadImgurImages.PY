import imguralbum
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
downloader = imguralbum.ImgurAlbumDownloader("http://imgur.com/a/uOOju")
print("This albums has %d images" % downloader.num_images())
downloader.save_images(foldername='uploadedImages')
