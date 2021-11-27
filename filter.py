from PIL import Image
import numpy as np


def fill_square(inp_arr, inp_square_side_size, inp_grayscale_step, inp_coordinates_of_square):
    '''
    Определяет оттенок серого для области исходного изображения по заданным координатам, и закрашивает его в полученный цвет.
            Параметры:
                    inp_arr (List[int]): исходное изображение в формате матрицы
                    inp_square_side_size (int): длина стороны квадрата, в пикселях
                    inp_grayscale_step (int): длина стороны квадрата, в пикселях
                    inp_coordinates_of_square (int[int]): координаты закрашиваемой области
    '''
    new_color = np.average(inp_arr[
               inp_coordinates_of_square[0]:inp_coordinates_of_square[0] + inp_square_side_size,
               inp_coordinates_of_square[1]:inp_coordinates_of_square[1] + inp_square_side_size])
    inp_arr[
    inp_coordinates_of_square[0]:inp_coordinates_of_square[0] + inp_square_side_size,
    inp_coordinates_of_square[1]:inp_coordinates_of_square[1] + inp_square_side_size] = \
        int(new_color // inp_grayscale_step) * inp_grayscale_step


def filter_the_image(inp_arr, inp_max_y, inp_max_x, inp_square_side_size, inp_grayscale_steps):
    '''
    Определяет шаг градации оттенков серого, вычисляет и закрашивает каждую область на исходном изображении в соответствующий
    оттенок серого
            Параметры:
                    inp_arr (List[int]): исходное изображение в формате матрицы
                    inp_square_side_size (int): длина стороны квадрата, в пикселях
                    inp_grayscale_step (int): длина стороны квадрата, в пикселях
                    inp_coordinates_of_square (int[int]): координаты закрашиваемой области
    '''
    grayscale_step = 255 // inp_grayscale_steps
    coordinates_of_squares = [[y, x]
                              for y in np.arange(0, inp_max_y, inp_square_side_size)
                              for x in np.arange(0, inp_max_x, inp_square_side_size)]
    for i in coordinates_of_squares:
        fill_square(inp_arr, inp_square_side_size, grayscale_step, i) #вообще не понял как это сделать


img = Image.open(input('Введите название исходного ихображения'))
arr = np.array(img)
print('1')
max_y = len(arr)
max_x = len(arr[1])
square_side_size = 10
grayscale_steps = 5
filter_the_image(arr, max_y, max_x, square_side_size, grayscale_steps)
print('2')
res = Image.fromarray(arr)
res.save('res.jpg')
