import arcade
from mpmath import mp
import time

def draw_axes():
    for x in range(0, 601, 15):
        arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 1)
    for y in range(0, 601, 15):
        arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 1)

def draw_function(a: int, b: int):
    x1 = 0
    y1 = (float(a) * x1 - (float(a) * 300 - 300)) + (float(b) * 15)
    x2 = 600
    y2 = (float(a) * x2 - (float(a) * 300 - 300)) + (float(b) * 15)
    arcade.draw_line(0, 300, 600, 300, arcade.color.BLACK, 3)
    arcade.draw_text('x', 580, 272, arcade.color.BLACK, 24)
    arcade.draw_line(300, 0, 300, 600, arcade.color.BLACK, 3)
    arcade.draw_text('y', 280, 575, arcade.color.BLACK, 24)
    arcade.draw_line(x1, y1, x2, y2, arcade.color.RED, 3)

def menu():
    print('Program rozwiazujacy rodzaj obliczen podany przez uzytkownika.')
    print('Autor: Wiktor Wasinski')
    print('')
    print('1 - rysowanie funkcji liniowej')
    print('2 - czy funkcje liniowe sa prostopadle?')
    print('3 - czy funkcje liniowe sa rownolegle?')
    print('4 - punkt przeciecia funkcji liniowych (wkrotce)')
    print('5 - funkcja liniowa jest stala, rosnaca czy malejaca?')
    print('6 - liczba π')
    option = int(input('Wybierz rodzaj obliczen: '))
    print('')
    match option:
        case 1: option1()
        case 2: option2()
        case 3: option3()
        case 4: option4()
        case 5: option5()
        case 6: option6()
        case _: invalid_option()

def option1(): # Rysowanie funkcji liniowej
    # Wprowadzanie wspolczynnikow
    a = input('Wprowadz "a": ')
    b = input('Wprowadz "b": ')
    funkcja = 'y=' + a + 'x+' + b
    print(funkcja)
    # Rysowanie funkcji
    arcade.open_window(600, 600, 'Wykres funkcji ' + funkcja)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_axes()
    draw_function(a,b)
    arcade.finish_render()
    arcade.run()

def option2():  # Czy funkcje liniowe sa prostopadle?
    # Wprowadzanie wspolczynnikow
    a1 = input('Wprowadz "a1": ')
    b1 = input('Wprowadz "b1": ')
    a2 = input('Wprowadz "a2": ')
    b2 = input('Wprowadz "b2": ')
    funkcja1 = 'y=' + a1 + 'x+' + b1
    print(funkcja1)
    funkcja2 = 'y=' + a2 + 'x+' + b2
    print(funkcja2)
    # Czy funkcje liniowe sa prostopadle?
    if float(a1) * float(a2) == -1:
        print('Funkcje sa prostopadle.')
    else:
        print('Funkcje nie sa prostopadle.')
    input('Wcisnij dowolny klawisz aby zakonczyc.')

def option3():  # Czy funkcje liniowe sa rownolegle?
    # Wprowadzanie wspolczynnikow
    a1 = input('Wprowadz "a1": ')
    b1 = input('Wprowadz "b1": ')
    a2 = input('Wprowadz "a2": ')
    b2 = input('Wprowadz "b2": ')
    funkcja1 = 'y=' + a1 + 'x+' + b1
    print(funkcja1)
    funkcja2 = 'y=' + a2 + 'x+' + b2
    print(funkcja2)
    # Czy funkcje liniowe sa rownolegle?
    if a1 == a2 and b1 == b2:
        print('Funkcje pokrywaja sie.')
    elif a1 == a2:
        print('Funkcje sa rownolegle.')
    else:
        print('Funkcje nie sa rownolegle.')
    input('Wcisnij dowolny klawisz aby zakonczyc.')

def option4():  # Punkt przeciecia funkcji liniowych
    # TODO
    input('Wkrotce...')

def option5():  # Funkcja liniowa jest stala, rosnaca czy malejaca?
    # Wprowadzanie wspolczynnikow
    a = input('Wprowadz "a": ')
    b = input('Wprowadz "b": ')
    funkcja = 'y=' + a + 'x+' + b
    print(funkcja)
    # Funkcja liniowa jest stala, rosnaca czy malejaca?
    if float(a) > 0:
        print('Funkcja jest rosnaca.')
    elif float(a) < 0:
        print('Funkcja jest malejaca.')
    else:
        print('Funkcja jest stala.')
    input('Wcisnij dowolny klawisz aby zakonczyc.')

def option6():  # Liczba π
    dokladnosc = input('Wprowadz liczbe cyfr do wyswietlenia: ')
    mp.dps = int(dokladnosc)
    tik = time.perf_counter()
    print('π=' + str(mp.pi))
    tak = time.perf_counter()
    print(f'Ukonczono w {tak - tik:0.4f} sekund.')
    input('Wcisnij dowolny klawisz aby zakonczyc.')

def invalid_option():
    input('Podano niepoprawna wartosc. Sprobuj jeszcze raz, uruchamiajac ponownie program.')

menu() # <--- Here start program