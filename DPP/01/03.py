import threading
import urllib.request
import time


def downloadImage(imagePath, fileName):
    print("Downloading Image From", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("completed Download")


def executeThread(i):
    imageName = "temp/multi_image-" + str(i) + ".jpg"
    downloadImage("http://lorempixel.com/400/200/sports", imageName)


def main():
    t0 = time.time()
    threads = []

    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i, ))
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution Time {}".format(totalTime))


if __name__ == '__main__':
    main()
