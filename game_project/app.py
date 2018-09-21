from maintable import *
from conveyor import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

class App(Frame):
    def __init__(self, master, num):
        super(App, self).__init__()
        self.master = master
        self.num = num
        self.load_images()

        # TODO
        # Conveyor 객체 생성
        self.app_frame = Frame(master)

        self.app_frame.grid(row=0, column=0)

        self.Conveyer_frame = Frame(self.app_frame)
        self.Conveyer_frame.grid(row=3, column=0)

        self.conveyor = Conveyor(self, self.resized_images, num)
        
        # TODO
        # MainTable 객체 생성
        self.Maintable_frame = Frame(self.app_frame)
        self.Maintable_frame.grid(row=0, column=0)

        self.table = Maintable(self, self.alphabet_images, self.figure_images , num)


    def load_images(self):
        self.figure_images = list(Image.open("picture\\%d.JPG" % (i+1)) for i in range(self.num*self.num + 2))
        self.alphabet_images = list(PhotoImage(file="alphabet\\%d.GIF" % (i+1)) for i in range(self.num*self.num))
        self.resized_images = list(ImageTk.PhotoImage(self.figure_images[i].resize((50,50), Image.ANTIALIAS)) for i in range(self.num*self.num))
        self.figure_images = list(ImageTk.PhotoImage(self.figure_images[i]) for i in range(self.num*self.num +2))

    # TODO
    # MainTable에서 선택한 도형 이미지와 Conveyor에서 Marker가 현재 가리키는 이미지를 비교한 후 비교 결과에 따라 처리한다.
    def compare_images(self, clicked_index):

        print("convery index", self.conveyor.cur_idx)
        print("clicked index", clicked_index)
        # 이미지가 일치하지 않는 경우

        # convery의 현재 index와 clicked index가 같은 경우는 맞음
        if( self.conveyor.cur_idx == clicked_index):
            # success
            if(self.conveyor.correct_match_config() == 1):
                self.finish(True)


        else :
            # 끝까지 틀렸을 경우 1를 return 함
            if self.conveyor.wrong_match_config() == 1:
                self.finish(False)
        print("compare_images")
    # TODO
    # 종료 조건 만족 시 실행
    def finish(self, win):
        if(win == True):
            finish_index = 16
        else:
            finish_index = 17

        self.app_frame.grid_forget()
        self.app_frame.pack_forget()

        b = ImageButton(self.master, image=self.figure_images[finish_index], relief=SOLID, overrelief=RIDGE, borderwidth=1)
        b.grid(column=0, row=0)
        b.bind("<Button-1>", sys.exit)

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
