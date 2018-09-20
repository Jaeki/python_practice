from imagebtn import *
from tkinter import *
from random import *
import time

class Maintable(Frame):
    def __init__(self, master, images, figure, width):
        super(Maintable, self).__init__()
        self.master = master
        self.width = width
        self.num = width * width
        self.images = images
        self.selected_image = None

        self.hidden_image = figure

        #self.shuffle()

        # TODO
        # 16개의 ImageButton 객체 생성 및 이벤트 핸들러 바인딩
        for i in range(0, self.width):
            for j in range(0, self.width):
                b = ImageButton(self.master, image=images[i*4 + j], relief=SOLID, overrelief=RIDGE, borderwidth=1)
                b.grid(column=j, row=i)
                b.bind("<Button-1>", self.show_hidden_image)
                b.bind("<ButtonRelease-1>", self.hide_image)

    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.num), self.num)

    # TODO
    # 마우스 눌렀을 때 이벤트 처리. 
    # 알파벳 이미지를 도형 이미지로 교체
    # event.widget.config 사용
    def show_hidden_image(self, event):
        #print("show_hiddin_image")

        #self.selected_image = event.widget.config

        # pyimageXX 와 같이 image 값이 나오고 있어 앞 pyimage 부분 빼고 7부터는 숫자임
        image_index = int(event.widget.cget("image")[7:]) - 1
        event.widget.config(image=self.hidden_image[image_index])
        self.selected_image = image_index

        #event.widget.config = self.hidden_image

    # TODO
    # 마우스 release 이벤트 처리
    # 도형 이미지를 원래 알파벳 이미지로 교체
    def hide_image(self, event):
        #print("hiddin_image")
        event.widget.config(image=self.images[self.selected_image])
        self.selected_image = None