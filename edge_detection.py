from PIL import Image, ImageDraw, ImageTk  # Подключим необходимые библиотеки.
from datetime import datetime


def create_image(src: str, methode: int) -> str:
    """
    Применяет нужный алгоритм на переданном изображении и создает новое преобразованное изображение. Возвращает путь до файла.
    :param src: Путь до файла.
    :param methode: Номер используемого метода.
    :return: Путь до нового файла.
    """
    image = Image.open(src)  # Открываем изображение.

    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    gray = image.convert("L")  # Переводим в чб
    gray_pix = gray.load()

    img = Image.new('L', (width, height), (0))
    draw = ImageDraw.Draw(img)  # Создаем инструмент для рисования.

    if methode == 0:
        simple_edge_detection(width, height, draw, gray_pix)
    elif methode == 1:
        gradient_mask_edge_detection(width, height, draw, gray_pix)
    elif methode == 2:
        laplas_mask_edge_detection(width, height, draw, gray_pix)
    elif methode == 3:
        roberts_mask_edge_detection(width, height, draw, gray_pix)
    elif methode == 4:
        previtt_mask_edge_detection(width, height, draw, gray_pix)
    elif methode == 5:
        sobel_mask_edge_detection(width, height, draw, gray_pix)
    else:
        kirsh_mask_edge_detection(width, height, draw, gray_pix)

    split_arr = src.split('/')
    name = split_arr[len(split_arr) - 1]
    print(name)
    src_out = f'./output/{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}_{name}'
    img.save(src_out, "JPEG")
    return src_out


# --------------------------------------------------
# Линейные алгоритмы
# --------------------------------------------------
def simple_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование порогового алгоритма выделения линий при помощи горизонтальных, вертикальных и наклонных масок.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H10 = [[-1, -1, -1], [2, 2, 2], [-1, -1, -1]]
    H11 = [[-1, -1, 2], [-1, 2, -1, ], [2, -1, -1]]
    H12 = [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]]
    H13 = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
    arr = [H10, H11, H12, H13]

    count_with_masks(arr, width, height, draw, pixels)


def gradient_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование алгоритма выделения контуров при помощи курсовых градиентных масок.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H10 = [[1, 1, 1], [1, -2, 1], [-1, -1, -1]]
    H11 = [[1, 1, 1], [-1, -2, 1], [-1, -1, 1]]
    H12 = [[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]]
    H13 = [[-1, -1, 1], [-1, -2, 1], [1, 1, 1]]
    H14 = [[-1, -1, -1], [1, -2, 1], [1, 1, 1]]
    H15 = [[1, -1, -1], [1, -2, -1], [1, 1, 1]]
    H16 = [[1, 1, -1], [1, -2, -1], [1, 1, -1]]
    H17 = [[1, 1, 1], [1, -2, -1], [1, -1, -1]]

    arr = [H10, H11, H12, H13, H14, H15, H16, H17]
    count_with_masks(arr, width, height, draw, pixels)


def laplas_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование порогового алгоритма выделения контуров при помощи оператора Лапласса.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    L1 = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    L2 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    L3 = [[1, -2, 1], [-2, 1, -2], [1, -2, 1]]

    arr = [L1, L2, L3]
    count_with_masks(arr, width, height, draw, pixels)


# --------------------------------------------------
# Нелинейные алгоритмы
# --------------------------------------------------
def roberts_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование алгоритма Робертса.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H18 = [[1, 0], [0, -1]]
    H19 = [[0, 1], [-1, 0]]
    arr = [H18, H19]
    count_with_masks(arr, width, height, draw, pixels)


def previtt_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование алгоритма Превитта.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H20 = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    H21 = [[-1, -1, -1], [0, 0, 0, ], [1, 1, 1]]
    H24 = [[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]
    H25 = [[-1, -1, 0], [-1, 0, 1], [0, 1, 1]]

    arr = [H20, H21, H24, H25]
    count_with_masks(arr, width, height, draw, pixels)


def sobel_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование алгоритма Собела.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H22 = [[-1, 0, 1], [-2, 0, 2], [-2, 0, 1]]
    H23 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    H26 = [[0, 1, 2], [1, 0, 1], [-2, -1, 0]]
    H27 = [[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]

    arr = [H22, H23, H26, H27]
    count_with_masks(arr, width, height, draw, pixels)


def kirsh_mask_edge_detection(width: int, height: int, draw: ImageDraw, pixels):
    """
    Использование алгоритма Кирша.
    :param height: Высота изображения.
    :param width: Ширина изображения.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    K1 = [[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]  # север
    K2 = [[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]  # северо-запад
    K3 = [[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]  # запад
    K4 = [[5, 5, -3], [5, 0, -3], [-3, -3, -3]]  # юго-запад
    K5 = [[5, -3, -3], [5, 0, -3], [5, -3, -3]]  # юг
    K6 = [[-3, -3, -3], [5, 0, -3], [5, 5, -3]]  # юго-восток
    K7 = [[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]  # восток
    K8 = [[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]  # северо-восток

    arr = [K1, K2, K3, K4, K5, K6, K7, K8]
    count_with_masks(arr, width, height, draw, pixels)


def count_with_masks(mask_arr: list[list[list[int]]], width: int, height: int, draw: ImageDraw, pixels):
    """
    Создает новое изображение через рисовалку на основе переданных параметров.
    :param mask_arr: Массив используемых масок.
    :param width: Ширина изображения.
    :param height: Высота изображения.
    :param draw: Ссылка-рисовалка.
    :param pixels: Массив чб пикселей.
    :return:
    """
    if len(mask_arr[0]) == 3:
        tmp_arr = three_mask(mask_arr, width, height, pixels)
    else:
        tmp_arr = two_mask(mask_arr, width, height, pixels)
    avr = 0
    for i in range(height):
        for j in range(width):
            avr += tmp_arr[i][j]
    avr = avr / (height * width)

    for i in range(height):
        for j in range(width):
            if tmp_arr[i][j] > avr:
                draw.point((j, i), (255))


def three_mask(mask_arr: list[list[list[int]]], width: int, height: int, pixels) -> list[list[int]]:
    """
    Обсчет масок 3X3.
    :param mask_arr: Массив масок.
    :param width: Ширина изображения.
    :param height: Высота изображения.
    :param pixels: Массив чб пикселей.
    :return: Массив чб пикселей нового изображения.
    """
    tmp_arr = []
    for i in range(height):
        tmp_arr.append([])
        for j in range(width):
            if i == 0 or i == height - 1 or j == width - 1 or j == 0:
                tmp_arr[i].append(0)
                continue
            value_arr = []
            for mask in mask_arr:
                value = mask[0][0] * pixels[j - 1, i - 1] + mask[0][0] * pixels[j - 1, i] + mask[0][0] * pixels[j - 1,
                                                                                                                i + 1] + \
                        mask[1][0] * pixels[j, i - 1] + mask[1][0] * pixels[j, i] + mask[1][0] * pixels[j, i + 1] + \
                        mask[2][0] * pixels[j + 1, i - 1] + mask[2][0] * pixels[j + 1, i] + mask[2][0] * pixels[j + 1,
                                                                                                                i + 1]
                value_arr.append(abs(value))
            tmp_arr[i].append(max(value_arr))
    return tmp_arr


def two_mask(mask_arr: list[list[list[int]]], width: int, height: int, pixels) -> list[list[int]]:
    """
     Обсчет масок 2X2.
    :param mask_arr: Массив масок.
    :param width: Ширина изображения.
    :param height: Высота изображения.
    :param pixels: Массив чб пикселей.
    :return: Массив чб пикселей нового изображения.
    """
    tmp_arr = []
    for i in range(height):
        tmp_arr.append([])
        for j in range(width):
            if i == height - 1 or j == width - 1:
                tmp_arr[i].append(0)
                continue
            value_arr = []
            for mask in mask_arr:
                value = mask[0][0] * pixels[j, i] + mask[0][1] * pixels[j, i + 1] + \
                        mask[1][0] * pixels[j + 1, i] + mask[1][1] * pixels[j + 1, i + 1]
                value_arr.append(abs(value))
            tmp_arr[i].append(max(value_arr))
    return tmp_arr
