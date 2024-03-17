from projekt import *
from uruchomienie import main
import pytest
import numpy as np

def test_create_ship():
    ship1 = Ship(-10)
    assert ship1.draft() == -10

def test_create_ship_incorrect_value():
    with pytest.raises(DraftValueError):
        Ship(20)

def test_create_ship_non_int_value():
    with pytest.raises(DraftValueError):
        Ship("a")

def test_set_new_draft():
    ship1 = Ship(-10)
    ship1.set_draft(-15)
    assert ship1.draft() == -15

def test_create_matrix():
    matrix_with_heights1 = [[1,2],[3,4]]
    matrix1 = Matrix(2,matrix_with_heights1)
    assert matrix1.size() == 2
    assert np.all(matrix1.matrix_with_heights() == np.array(matrix_with_heights1))

def test_create_matrix_with_negative_size():
    matrix_with_heights1 = [[1,2],[3,4]]
    with pytest.raises(MatrixSizeError):
        Matrix(-4,matrix_with_heights1)

def test_create_matrix_with_non_int_size():
    matrix_with_heights1 = [[1,2],[3,4]]
    with pytest.raises(MatrixSizeError):
        Matrix("1o",matrix_with_heights1)
    
def test_create_matrix_with_different_sizes1():
    matrix_with_heights1 = [[1,2],[3,4],[2,8]]
    with pytest.raises(MatrixSizeError):
        Matrix(2 ,matrix_with_heights1)

def test_create_matrix_with_different_sizes2():
    matrix_with_heights1 = [[1,2,5],[3,4]]
    with pytest.raises(MatrixSizeError):
        Matrix(2 ,matrix_with_heights1)

def test_create_matrix_with_letters():
    matrix_with_heights1 = [["a",2],["okoń",4]]
    with pytest.raises(MatrixError):
        Matrix(2 ,matrix_with_heights1)

def test_create_matrix_non_matrix():
    matrix_with_heights1= 1
    with pytest.raises(MatrixError):
        Matrix(1,matrix_with_heights1)   

def test_set_new_matrix():
    matrix_with_heights1 = [[1,2],[3,4]]
    matrix1 = Matrix(2,matrix_with_heights1)
    matrix1.set_size(3)
    matrix1.set_matrix([[1,2,-4],[3,4,-4],[1,4,8]])
    matrix_with_heights2 = [[1,2,-4],[3,4,-4],[1,4,8]]
    assert matrix1.size() == 3
    assert np.all(matrix1.matrix_with_heights() == np.array(matrix_with_heights2))

def test_convert_for_chart():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-20,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    a = pilotagemap1.convert_for_chart()
    assert np.all(a == np.array([[-1,-1,1],[0,-1,1],[0,-1,-1]]))

def test_find_route():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-20,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    for_chart = pilotagemap1.convert_for_chart()
    route = pilotagemap1.find_route(for_chart)
    assert route == [(0,0),(1,0),(1,1),(1,2),(2,2)]

def test_find_complex_route():
    ship1 = Ship(-30)
    matrix_with_heights1 = [[-31,-32,-33,-33,-34],[-32,-20,-20,-21,-35],[-31,-19,-42,-41,-40],[-33,-22,-43,30,40],[-34,-35,-36,-37,-40]]    
    matrix1 = Matrix(5, matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    for_chart = pilotagemap1.convert_for_chart()
    route = pilotagemap1.find_route(for_chart)
    assert route == [(0,0),(0,1),(0,2),(0,3),(0,4),(1,4),(2,4),(3,4),(4,4)]    

def test_give_x_points():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-20,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    for_chart = pilotagemap1.convert_for_chart()
    route = pilotagemap1.find_route(for_chart)
    pointsX = pilotagemap1.give_pointsX(route)
    assert pointsX == [0,1,1,1,2]

def test_give_y_points():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-20,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    for_chart = pilotagemap1.convert_for_chart()
    route = pilotagemap1.find_route(for_chart)
    pointsY = pilotagemap1.give_pointsY(route)
    assert pointsY == [0,0,1,2,2]

def test_route_found():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-20,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    show = pilotagemap1.show_map()
    assert show == 'Route found'

def test_no_route_found():
    ship1 = Ship(-10)
    matrix_with_heights1 = [[-11,-10,1],[-2,-15,2],[-3,-9,-10]]
    matrix1 = Matrix(3,matrix_with_heights1)
    pilotagemap1 = PilotageMap(ship1, matrix1)
    show = pilotagemap1.show_map()
    assert show == 'Route cannot be found'

def test_incorrect_path():
    ourpath = "infoaaaation.json"
    with pytest.raises(FileNotFoundError):
        open(ourpath, "r")