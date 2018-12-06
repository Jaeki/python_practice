# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import shutil


def crawl_naver_webtoon(episode_url, num):
    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')
    img_list=[]
    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())
    comic_title = '고수'
    print(ep_title)
    img_count=0
    total_width = 0
    total_height = 0
    for img_tag in soup.select('.wt_viewer img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title, str(i))
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))
        # print(image_file_url.split('_')[-1])
        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        # print(image_file_path)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content

        # img_list.append(image_file_data)
        open(image_file_path, 'wb').write(image_file_data)
        tmp = Image.open(image_file_path)
        img_list.append(tmp)
        (w, h) = img_list[-1].size
        if total_width < w:
            total_width = w
        total_height = total_height + h
        # os.removedirs(image_dir_path)
        # close(image_file_path)
        # tmp.close()

    # shutil.rmtree(image_dir_path)
    new_img = Image.new('RGB', (total_width, total_height), 'white')
    box = (0,0)
    total_height = 0
    for a_im in img_list:
        new_img.paste(a_im, box)
        (width, height) = a_im.size
        total_height += height
        box = (0, total_height)
        # print("box=", box)
    filename = 'toon' + str(num) + '.png'
    ffile = os.path.join(os.path.dirname(__file__), comic_title, filename)
    # ffile = os.path.join(image_dir_path, filename)
    new_img.save(ffile, 'PNG')

    print('Completed !')

if __name__ == '__main__':

    for i in range(147,163):
        episode_url = 'https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=' + str(i) + '&weekday=wed'
        crawl_naver_webtoon(episode_url, i)