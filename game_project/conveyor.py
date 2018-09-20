from tkinter import *
from random import *

class Conveyor(Frame):
    def __init__(self, master, images, width):
        super(Conveyor, self).__init__()
        self.imagelist = []

        self.master = master
        self.width = width
        self.num = width*(width-1)+1
        self.images = images
        self.labels = []
        self.shuffle()

        # 추가된 변수들
        self.cur_idx =9
        self.arrow_canvas = None
        self.final_label = None
        

        # TODO
        # Label widget 생성

        for i in range(0, self.num):
            l = Label(self.master.Conveyer_frame, image=images[i], borderwidth=1, relief=SOLID)
            l.grid(column=i, row=1)
            self.labels.append(l)

        self.init_canvas()

    # TODO
    # marker와 FINAL 글씨를 그리는 부분. tkinter canvas 사용
    def init_canvas(self):

        arrow_width, arrow_height = 50, 16
        self.arrow_canvas = Canvas(self.master.Conveyer_frame, width=arrow_width, height=arrow_height)
        self.arrow_canvas.create_polygon(0,0, arrow_width/2,arrow_height, arrow_width,0 , fill="#005500")
        self.arrow_canvas.grid(column=self.cur_idx, row=0)

        self.final_label = Label(self.master.Conveyer_frame, text="FINAL", fg="red")
        self.final_label.grid(column=12, row=0)

        
    # TODO
    # 이미지 shuffle하는 함수
    def shuffle(self):
        self.imagelist = sample(range(0, self.width*self.width), self.num)

    # TODO
    # 현재 이미지와 일치하는 이미지를 선택했을 경우
    def correct_match_config(self):
        # FINAL 일 떄
        if self.cur_idx == self.num - 1:
            print("correct_match final ")
            return 1
        # FINAL 바로 전 일 떄
        elif self.cur_idx == self.num - 2:
            self.cur_idx += 1
            self.arrow_canvas.grid(column=self.cur_idx, row=0)

            self.final_label.grid_forget()
            self.final_label.pack_forget()
        # 그 외 일반적인 상황
        else:
            self.cur_idx += 1
            self.arrow_canvas.grid(column=self.cur_idx, row=0)
            return -1
        
    # TODO
    # 현재 이미지와 일치하는 이미지를 선택하지 못했을 경우
    def wrong_match_config(self):
        # 마지막일 때
        if(self.cur_idx == 0):
            sys.exit()
            
        # FINAL일 때
        elif self.cur_idx == self.num-1:
            self.cur_idx -= 1
            self.arrow_canvas.grid(column=self.cur_idx, row=0)

            self.final_label.grid(column=12, row=0)
        # 그 외 일반적인 상황
        else:
            self.cur_idx -= 1
            self.arrow_canvas.grid(column=self.cur_idx, row=0)
        

    # TODO
    # 오답 시 새로운 이미지를 추가하는 함수
    def get_new_image(self):
        pass

    # TODO
    # 오답시 왼쪽으로 1칸씩 이동하고 새 이미지를 추가하는 함수
    def lshift_images(self, new_image):
        pass
