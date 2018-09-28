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

        self.shuffle()

        # TODO
        # 16개의 ImageButton 객체 생성 및 이벤트 핸들러 바인딩
        for i in range(0, self.width):
            for j in range(0, self.width):
                b = ImageButton(self.master.Maintable_frame, image=images[i*4 + j], relief=SOLID, overrelief=RIDGE, borderwidth=1)
                b.grid(column=j, row=i)
                b.bind("<Button-1>", self.show_hidden_image)
                b.bind("<ButtonRelease-1>", self.hide_image)

    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.num), self.num)


        answer = list(map(lambda x : x +1 , self.imagelist))
        print(answer)
        print("correct answer : ")
        for i in range(len(answer)):
            if( i % 4 == 0):
                print("\n")
            print(answer[i], end=",")

        print("\n")

    # TODO
    # 마우스 눌렀을 때 이벤트 처리. 
    # 알파벳 이미지를 도형 이미지로 교체
    # event.widget.config 사용
    def show_hidden_image(self, event):
        # pyimageXX 와 같이 image 값이 나오고 있어 앞 pyimage 부분 빼고 7부터는 숫자임
        image_index = int(event.widget.cget("image")[7:]) - 1
        event.widget.config(image=self.get_figure_image(image_index))
        self.selected_image = image_index

    # TODO
    # 마우스 release 이벤트 처리
    # 도형 이미지를 원래 알파벳 이미지로 교체
    def hide_image(self, event):

        event.widget.config(image=self.images[self.selected_image])

        # 선택한 image 의 index를 return 한다. 값은 0 부터
        # suffle 된 값을 찾기 위해서 imagelist를 이용한다.
        self.master.compare_images(self.imagelist[self.selected_image])
        self.selected_image = None

    # 숨겨진 그림을 보여주기 위해서 선택된 index의 image를 return 해준다.
    def get_figure_image(self, index):
        return self.hidden_image[self.imagelist[index]]
