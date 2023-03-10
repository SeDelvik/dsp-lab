from PIL import Image, ImageDraw  # Подключим необходимые библиотеки.
from gui import Gui

def main():
    # mode = int(input('mode:'))  # Считываем номер преобразования.
    image = Image.open("./input/test_image.jpg")  # Открываем изображение.

    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    # pix = image.load()  # Выгружаем значения пикселей.
    gray = image.convert("L")
    draw = ImageDraw.Draw(gray)  # Создаем инструмент для рисования.
    gray_pix = gray.load()
    print(gray_pix[0, 0])



    # image.save("ans.jpg", "JPEG")  # сохранение результата
    # del draw  # удаление кисти
    Gui()


if __name__ == '__main__':
    main()
