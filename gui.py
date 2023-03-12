from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  # Подключим необходимые библиотеки.

from edge_detection import create_image


class Gui:

    def __init__(self):
        self.variables = {}

        self.window = Tk()
        self.window.title("Добро пожаловать")
        self.window.geometry('950x650')
        self.methode_var = IntVar(value=0)

        lbl = Label(self.window, text="Укажите scr-файл")
        lbl.grid(column=0, row=0, columnspan=2)
        btn = Button(self.window, text="Выбрать", command=self.get_image)
        btn.grid(column=0, row=1)
        self.lbl_src = Label(self.window, text="")
        self.lbl_src.grid(column=1, row=1)

        # создание двух канвас для отображения входного изображения и с выделенными контурами
        self.image_input = None
        self.photo_input = None

        self.canvas_input = Canvas(self.window, height=400, width=400)
        self.c_image_input = None
        self.canvas_input.grid(row=2, column=0)

        self.image_output = None
        self.photo_output = None

        self.canvas_output = Canvas(self.window, height=400, width=400)
        self.c_image_output = None
        self.canvas_output.grid(row=2, column=1)

        self.create_radio_buttons()  # создание кнопок для выбора нужного алгоритма

        btn_start = Button(self.window, text="Начать", command=self.create_edge_image)
        btn_start.grid(column=0, row=8)

        self.window.mainloop()

    def get_image(self):
        """
        Вызов окна выбора файла, получение пути до изображения и вставка его в канвас.
        :return:
        """
        file = filedialog.askopenfilename(filetypes=(("img", ".jpg .bmp .png .pcx"),
                                                     ("all files", "*.*")))
        self.lbl_src.configure(text=f"{file}")
        self.variables["src"] = file
        print(self.variables["src"])
        self.image_input = Image.open(file)
        width, height = self.image_input.size
        if width > height:
            height = int(height / width * 400)
            width = 400
        else:
            width = int(width / height * 400)
            height = 400
        self.image_input = self.image_input.resize((width, height), Image.ANTIALIAS)
        self.photo_input = ImageTk.PhotoImage(self.image_input)
        self.c_image_input = self.canvas_input.create_image(0, 0, anchor='nw', image=self.photo_input)

    def create_edge_image(self):
        """
        Вызов алгоритмов выделения контуров и вставка результата в канвас.
        :return:
        """
        if "src" not in self.variables:
            return
        src_out = create_image(self.variables["src"], self.methode_var.get())
        self.image_output = Image.open(src_out)
        self.image_output = self.image_output.resize((400, 400), Image.ANTIALIAS)
        self.photo_output = ImageTk.PhotoImage(self.image_output)
        self.c_image_output = self.canvas_output.create_image(0, 0, anchor='nw', image=self.photo_output)

    def create_radio_buttons(self):
        """
        Создание радиобаттон для выбора нужного алгоритма.
        :return:
        """
        btn1 = Radiobutton(self.window, text="Выделение линий", value=0, variable=self.methode_var)
        btn2 = Radiobutton(self.window, text="Курсовые градиентные", value=1, variable=self.methode_var)
        btn3 = Radiobutton(self.window, text="Лаплас", value=2, variable=self.methode_var)
        btn4 = Radiobutton(self.window, text="Робертс", value=3, variable=self.methode_var)
        btn5 = Radiobutton(self.window, text="Превитт", value=4, variable=self.methode_var)
        btn6 = Radiobutton(self.window, text="Собел", value=5, variable=self.methode_var)
        btn7 = Radiobutton(self.window, text="Кирш", value=6, variable=self.methode_var)

        lbl_line_algs = Label(self.window, text="Линейные алгоритмы")
        lbl_not_line_algs = Label(self.window, text="Не линейные алгоритмы")
        lbl_line_algs.grid(column=0, row=3)
        lbl_not_line_algs.grid(column=1, row=3)

        btn1.grid(column=0, row=4)
        btn2.grid(column=0, row=5)
        btn3.grid(column=0, row=6)
        btn4.grid(column=1, row=4)
        btn5.grid(column=1, row=5)
        btn6.grid(column=1, row=6)
        btn7.grid(column=1, row=7)
