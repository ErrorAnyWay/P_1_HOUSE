def main():
    x, y = 300, 200
    width, height = 200, 300
    draw_house(x, y, width, height)

def draw_house(x, y, width, height):
    """
    Функцуия корторая рисует домик ширины width и  высоты height  от опорной точки (x, y)
    котороя находимтя в середине нижней точки фундамента.
    :param x:  координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная щирина домика(фундамент или вылет крыши включены)
    :param height:  полная высота домика
    :return:
    """
    print(x,y,width,height)

    foundation_height = 0.05 * height # Высота фундамента - Вычисляем  5 процентов от высоты домика
    wall_height = 0.5 * height # Высота стен - вычисляем 50 процентов от выстоты домика
    wall_width = 0.9 * width # Ширина стен - вычисляем 90 процентов от ширины домика
    roof_height = height - foundation_height - wall_height # Высота криши: высота - высота фундамента - высота стены

    draw_house_foundation(x,y, width,foundation_height)  # хочу нарисовать фундамент, задаю ему параметры координаты x,y где он будет находится, и свою высоту и ширину, ширина будет иметь такое самое значение что и основной дом =) а высота будет вычислена в переменной foundation_height

    draw_house_walls(x, y - foundation_height, wall_width, wall_height) # Рисуем стену -
    draw_house_roof(x, y - foundation_height - wall_height, width , roof_height)


def draw_house_foundation(x,y, width , height):
    """
    Функцуия корторая рисует основание домика width и height  от опорной точки (x, y)
    котороя находимтя в середине нижней точки фундамента.
    :param x:  координата x середины фундамента
    :param y: координата y низа фундамента
    :param width: полная щирина фундамента
    :param height:  полная высота фундамента
    :return: None
    """

    print(x,y,width,height)

def draw_house_walls(x, y, height, width):
    print(x,y,width,height)


def draw_house_roof(x, y, width , height):
    print(x,y,width,height)

main()
