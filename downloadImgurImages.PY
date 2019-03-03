import imguralbum
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def downloadImages(imgurLink):
    downloader = imguralbum.ImgurAlbumDownloader(imgurLink)
    print("This albums has %d images" % downloader.num_images())
    downloader.save_images()
    return(imgurLink[imgurLink.rfind('/')])
