from PIL import Image, ImageDraw, ImageTk  # Подключим необходимые библиотеки.


def create_image(src: str, methode: int) -> str:
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
        gradient_mask_edge_detection(draw, gray_pix)
    elif methode == 2:
        laplas_mask_edge_detection(draw, gray_pix)
    elif methode == 3:
        roberts_mask_edge_detection(draw, gray_pix)
    elif methode == 4:
        previtt_mask_edge_detection(draw, gray_pix)
    elif methode == 5:
        sobel_mask_edge_detection(draw, gray_pix)
    else:
        kirsh_mask_edge_detection(draw, gray_pix)

    img.show()


# --------------------------------------------------
# Линейные алгоритмы
# --------------------------------------------------
def simple_edge_detection(width, height, draw: ImageDraw, pixels):
    """
    Использование порогового алгоритма выделения линий при помощи горизонтальных, вертикальных и наклонных масок.
    :param draw:
    :param pixels:
    :return: Путь до получившегося изображения.
    """
    H10 = [[-1, -1, -1], [2, 2, 2], [-1, -1, -1]]
    H11 = [[-1, -1, 2], [-1, 2, -1, ], [2, -1, -1]]
    H12 = [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]]
    H13 = [[2, -1, -1], [-1, 2, -1], [-1, -1, 2]]
    arr = [H10, H11, H12, H13]

    tmp_arr = []
    for i in range(height):
        tmp_arr.append([])
        for j in range(width):
            if i == 0 or i == height - 1 or j == width - 1 or j == 0:
                tmp_arr[i].append(0)
                continue
            value_arr = []
            for mask in arr:
                value = mask[0][0] * pixels[j - 1, i - 1] + mask[0][0] * pixels[j - 1, i] + mask[0][0] * pixels[j - 1,
                                                                                                                i + 1] + \
                        mask[1][0] * pixels[j, i - 1] + mask[1][0] * pixels[j, i] + mask[1][0] * pixels[j, i + 1] + \
                        mask[2][0] * pixels[j + 1, i - 1] + mask[2][0] * pixels[j + 1, i] + mask[2][0] * pixels[j + 1,
                                                                                                                i + 1]
                value_arr.append(abs(value))
            tmp_arr[i].append(max(value_arr))

    avr = 0
    for i in range(height):
        for j in range(width):
            avr += tmp_arr[i][j]
    avr = avr / (height*width)

    for i in range(height):
        for j in range(width):
            if tmp_arr[i][j] > avr:
                draw.point((j, i), (255))


def gradient_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование алгоритма выделения контуров при помощи курсовых градиентных масок.
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
    H16 = [[1, 1, 1], [1, -2, -1], [1, -1, -1]]


def laplas_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование порогового алгоритма выделения контуров при помощи оператора Лапласса.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    L1 = [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
    L2 = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    L3 = [[1, -2, 1], [-2, 1, -2], [1, -2, 1]]


# --------------------------------------------------
# Нелинейные алгоритмы
# --------------------------------------------------
def roberts_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование алгоритма Робертса.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H18 = [[1, 0], [0, -1]]
    H19 = [[0, 1], [-1, 0]]


def previtt_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование алгоритма Превитта.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H20 = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    H21 = [[-1, -1, -1], [0, 0, 0, ], [1, 1, 1]]
    H24 = [[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]
    H25 = [[-1, -1, 0], [-1, 0, 1], [0, 1, 1]]


def sobel_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование алгоритма Собела.
    :param draw: Новое пустое изображение такого же размера как исходное.
    :param pixels: Массив чб пикселей исходного изображения.
    :return: Путь до получившегося изображения.
    """
    H22 = [[-1, 0, 1], [-2, 0, 2], [-2, 0, 1]]
    H23 = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    H26 = [[0, 1, 2], [1, 0, 1], [-2, -1, 0]]
    H27 = [[-2, -1, 0], [-1, 0, 1], [0, 1, 2]]


def kirsh_mask_edge_detection(draw: ImageDraw, pixels) -> str:
    """
    Использование алгоритма Кирша.
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
