from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import bs4
import re
import requests
import urllib.parse
import os
#PeterP
#By: Danny
def main():
    try:
        os.mkdir("webcache")
        print("Folder made")
    except:
        print("Folder made")
    dic = open('main.dic', 'r')
    Lines = dic.readlines()
    count = 0
    f = open("terms.inf", "a", encoding="utf-8")
    # Strips the newline character
    for line in Lines:
        count += 1
        keyword = line.strip()
        keyword = str(keyword.replace(" ", "+"))
        keyword = str(keyword.replace(".", ""))
        keyword = str(keyword.replace(":", ""))
        keyword = str(keyword.replace("-", ""))
        keyword = str(keyword.replace("&", "_"))
        keyword = str(keyword.replace(",", ""))
        print(keyword)
        getweb(keyword)
        getweb2(keyword)
        getweb3(keyword)
        getimg(keyword)
        getvid(keyword)
        f.write("[terms]" + "\n")
        f.write("term=" + keyword + "\n")
        
def getweb(keyword):
    print("Getting web results")
    url = str("https://www.ask.com/web?q=" + keyword)
    request_result=requests.get( url )
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    links = []
    rawdata = []
    results = 0
    f = open("web.txt", "a", encoding="utf-8")
    for link in soup.findAll('a'):
        rawdata.append(link.get('href'))
        rawdata.append(link.string)
    for i in range(38, 56):
        url = str(rawdata[i])
        i += 1
        title = str(rawdata[i])
        source = getsource(url, title)
        sourceurl = getsourceurl(url)
        preview = getimgname(source, title)
        preview = preview.replace(' ', "")
        preview = preview.replace("|", "")
        preview = preview.replace(" | ", "")
        if url.find("https://") == -1:
            results += 0
        else:
            print(url)
            urlkit = url.replace("https://", "")
            urlkit = "https://" + urlkit
            getwebimg0(urlkit, preview)
            getwebimg0(urlkit, preview)
            getwebimg1(urlkit, preview)
            getwebimg2(urlkit, preview)
            getwebimg3(urlkit, preview)
            getwebimg4(urlkit, preview)
            getwebimg5(urlkit, preview)
            results += 1
            print(str(results) + " Results found")
            f.write("url='" + url + "';\n")
            f.write("preview='../webcache/" + preview + "';\n")
            f.write("title='" + title + "'l\n")
            f.write("source='" + source + ";\n")
            f.write("sourceurl='" + sourceurl + "';\n")
            f.write("tag='" + keyword + "'\n")
            f.write('webtmp=[url, preview, title, source, sourceurl, tag]; \n')
            f.write('web.push(webtmp); \n')

def getweb2(keyword):
    url = str("https://www.ask.com/web?q=" + keyword + "&page=2")
    request_result=requests.get( url )
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    links = []
    rawdata = []
    results = 0
    f = open("web.txt", "a", encoding="utf-8")
    for link in soup.findAll('a'):
        rawdata.append(link.get('href'))
        rawdata.append(link.string)
    for i in range(38, 56):
        url = str(rawdata[i])
        i += 1
        title = str(rawdata[i])
        source = getsource(url, title)
        sourceurl = getsourceurl(url)
        preview = getimgname(source, title)
        preview = preview.replace(' ', "")
        preview = preview.replace("|", "")
        preview = preview.replace(" | ", "")
        if url.find("https://") == -1:
            results += 0
        else:
            print(url)
            urlkit = url.replace("https://", "")
            urlkit = "https://" + urlkit
            getwebimg0(urlkit, preview)
            getwebimg0(urlkit, preview)
            getwebimg1(urlkit, preview)
            getwebimg2(urlkit, preview)
            getwebimg3(urlkit, preview)
            getwebimg4(urlkit, preview)
            getwebimg5(urlkit, preview)
            results += 1
            print(str(results) + " Results found")
            f.write("url='" + url + "';\n")
            f.write("preview='../webcache/" + preview + "';\n")
            f.write("title='" + title + "'l\n")
            f.write("source='" + source + ";\n")
            f.write("sourceurl='" + sourceurl + "';\n")
            f.write("tag='" + keyword + "'\n")
            f.write('webtmp=[url, preview, title, source, sourceurl, tag]; \n')
            f.write('web.push(webtmp); \n')

def getweb3(keyword):
    url = str("https://www.ask.com/web?q=" + keyword + "&page=3")
    request_result=requests.get( url )
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    links = []
    rawdata = []
    results = 0
    f = open("web.txt", "a", encoding="utf-8")
    for link in soup.findAll('a'):
        rawdata.append(link.get('href'))
        rawdata.append(link.string)
    for i in range(38, 56):
        url = str(rawdata[i])
        i += 1
        title = str(rawdata[i])
        source = getsource(url, title)
        sourceurl = getsourceurl(url)
        preview = getimgname(source, title)
        preview = preview.replace(' ', "")
        preview = preview.replace("|", "")
        preview = preview.replace(" | ", "")
        if url.find("https://") == -1:
            results += 0
        else:
            print(url)
            urlkit = url.replace("https://", "")
            urlkit = "https://" + urlkit
            getwebimg0(urlkit, preview)
            getwebimg0(urlkit, preview)
            getwebimg1(urlkit, preview)
            getwebimg2(urlkit, preview)
            getwebimg3(urlkit, preview)
            getwebimg4(urlkit, preview)
            getwebimg5(urlkit, preview)
            results += 1
            print(str(results) + " Results found")
            f.write("url='" + url + "';\n")
            f.write("preview='../webcache/" + preview + "';\n")
            f.write("title='" + title + "'l\n")
            f.write("source='" + source + ";\n")
            f.write("sourceurl='" + sourceurl + "';\n")
            f.write("tag='" + keyword + "'\n")
            f.write('webtmp=[url, preview, title, source, sourceurl, tag]; \n')
            f.write('web.push(webtmp); \n')


def getsource(url, title):
    if '-' in title:
        source = title
        sourcetmp = str(source.split(' - ', 1)[0])
        scombo1 = " - " + sourcetmp
        scombo2 = sourcetmp + " - "
        source = source.replace(scombo1, "")
        source = source.replace(scombo2, "")
        source = source.capitalize()
        return source
    else:
        source = url
        sourceurlget = url.rsplit("/", 2)
        source = str(sourceurlget[0])
        source = str(source.replace('https://www.', ''))
        source = str(source.replace('/', ''))
        source = str(source.replace('.com', ''))
        source = str(source.replace('.net', ''))
        source = str(source.replace('.org', ''))
        source = str(source.replace('.gov', ''))
        source = str(source.replace('.us', ''))
        source = str(source.replace('.uk', ''))
        source = str(source.replace('.pl', ''))
        source = str(source.replace('.jp', ''))
        source = source.capitalize()
        return source
def getsourceurl(url):
    sourceurl = url
    sourceurlget = url.rsplit("/", 2)
    sourceurl = str(sourceurlget[0])
    if (sourceurl == "https:/"):
        sourceurl = url
    return sourceurl

def getimgname(source, title):
    title = title.replace(" ", "_")
    title = title.replace(":", "")
    title = title.replace(";", "")
    title = title.replace("/", "")
    title = title.replace('\ ', "")
    title = title.replace("|", "")
    title = title.replace(" | ", "")
    title = title.replace(":", "")
    title = title.replace("*", "")
    title = title.replace("?", "")
    title = title.replace("<", "")
    title = title.replace(">", "")
    title = title.replace('"', "")
    title.lower()
    souce = source.lower()
    preview = source + "_" + title + ".png"
    return preview
def getwebimg0(url, preview):
    BASE = 'https://image.thum.io/get/maxAge/12/width/1024/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
def getwebimg1(url, preview):
    BASE = 'https://render-tron.appspot.com/screenshot/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
def getwebimg2(url, preview):
    BASE = 'https://mini.s-shot.ru/1024x0/JPEG/1024/Z100/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
def getwebimg3(url, preview):
    BASE = 'https://mini.s-shot.ru/1024x0/PNG/1024/Z100/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
def getwebimg4(url, preview):
    BASE = 'https://mini.s-shot.ru/1024x1024/JPEG/1024/Z100/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)
def getwebimg5(url, preview):
    BASE = 'https://mini.s-shot.ru/1024x1024/PNG/1024/Z100/'
    path = "webcache/" + preview
    target = url
    response = requests.get(BASE + target, stream=True)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            for chunk in response:
                file.write(chunk)

def getimg(keyword):
    print("Getting image results")
    f = open("img.txt", "a", encoding="utf-8")
    url = 'https://www.ask.com/web?q=' + keyword
    request_result=requests.get( url )
    rawdata = []
    result = 0
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    for link in soup.findAll('a'):
        rawdata.append(link.get('href'))
    for i in range(19, 37):
        url = rawdata[i]
        try:
            img = findimg(url, keyword)
            if (img == "NULL"):
                result += 0
            else:
                title = str(findimgtitle(url))
                title = title.replace("<title>", "")
                title = title.replace("</title>", "")
                source = str(getsource(url, title))
                sourceurl = str(getsourceurl(url))
                f.write("url='" + url + "';\n")
                f.write("preview=" + img + "\n")
                f.write("title='" + title + "';\n")
                f.write("source='" + source + "';\n")
                f.write("sourceurl=" + sourceurl + "\n")
                f.write("'tag='" + keyword + "';\n")
                f.write(' imgtmp=[url, preview, title, source, sourceurl, tag]; \n')
                f.write('img.push(imgtmp); \n')
                result+= 1
                print(str(result) + " results found")
        except:
            result += 0
        
def findimg(url, keyword):
    img = "NULL"
    request_result=requests.get( url )
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    images = soup.findAll('img')
    for image in images:
        if keyword in str(image['src']):
            img = str(image['src'])
            img = img.replace("//i0.wp.com/", "")
    return img

def findimgtitle(url):
    title = "NULL"
    request_result=requests.get( url )
    rawdata = []
    result = 0
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    title = soup.title
    return title

def getvid(keyword):
    print("Getting video results")
    f = open("vid.txt", "a", encoding="utf-8")
    url = 'https://www.ask.com/web?q=' + keyword + "+site:youtube.com&ad=dirN&o=0"
    request_result=requests.get( url )
    rawdata = []
    result = 0
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    for link in soup.findAll('a'):
        if "https://www.youtube.com/watch?v=" in str(link.get('href')):
            rawdata.append(link.get('href'))
        else:
            result += 0
    for i in range(0, len(rawdata)):
        url = rawdata[i]
        title = findvidname(url)
        preview = getembed(url)
        sourceurl = findsourceurl(url)
        source = findsource(sourceurl)
        f.write("url=';" + url + "';\n")
        f.write("preview='" + preview + "';\n")
        f.write("title=';" + title + "';\n")
        f.write("source='" + source + "';\n")
        f.write("sourceurl='" + sourceurl + "';\n")
        f.write("tag='" + keyword + "';\n")
        f.write('vidtmp=[url, preview, title, source, sourceurl, tag]; \n')
        f.write('vid.push(vidtmp); \n')
        result += 1
        print("Results found: " + str(result))
def getembed(url):
    preview = url
    preview = preview.replace("https://www.youtube.com/watch?v=", "http://www.youtube.com/embed/")
    return preview
def findvidname(url):
    title = "NULL"
    request_result=requests.get( url )
    rawdata = []
    result = 0
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    title = str(soup.title)
    title = title.replace(" - YouTube", "")
    title = title.replace("<title>", "")
    title = title.replace("</title>", "")
    return title
def findsource(url):
    source = "NULL"
    request_result=requests.get( url )
    rawdata = []
    result = 0
    soup = bs4.BeautifulSoup(request_result.text, "html.parser")
    source = str(soup.title)
    source = source.replace(" - YouTube", "")
    source = source.replace("<title>", "")
    source = source.replace("</title>", "")
    return source
def findsourceurl(url):
    sourceurl = ""
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 7.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url, headers = HEADERS )
    html = html.text
    soup = BeautifulSoup(html, "html.parser")
    metas = soup.find_all("meta")
    metas = str(metas)
    precut = metas.split('itemprop="paid"/>,', 1)[0]
    channelid = metas.replace(precut, "")
    channelid = channelid.replace(':android:package"/>, <meta content="', "")
    channelid = channelid.split('" i', 1)[0]
    channelid = channelid.replace('itemprop="paid"/>, <meta content="', "")
    sourceurl = "https://www.youtube.com/channel/" + channelid
    return sourceurl
main()
