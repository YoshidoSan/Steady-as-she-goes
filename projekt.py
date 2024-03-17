import numpy as np
import collections
import matplotlib.pyplot as plt

class DraftValueError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

class MatrixError(Exception):
    pass


class Ship:
    def __init__(self, draft):
        if type(draft) is not int or draft >= 0:
            raise DraftValueError('Draft of the ship must be a negative number')
        self._draft = draft
    
    def draft(self):
        return self._draft
    
    def set_draft(self, new_draft):
        if type(new_draft) is not int or new_draft >= 0:
            raise DraftValueError('New draft of the ship must be a negative number')
        self._draft = new_draft
    
    def info(self):
        return(f'Ship draft is {self._draft}. It can sail through water with a depth of at least {self._draft} meters b.s.l.')
    
    def __str__(self):
        return self.info()


class Matrix:
    def __init__(self, size, matrix_with_heights):
        if type(size) is not int or size <= 0:
            raise MatrixSizeError('Size of the matrix must be a positive number')
        self._size = size
        if type(matrix_with_heights) is not list:
            raise MatrixError('Wrong matrix')
        if len(matrix_with_heights) is not self._size:
            raise MatrixSizeError('Matrix Size is wrong')
        for row in matrix_with_heights:
            if len(row) is not self._size:
                raise MatrixSizeError('Matrix size is wrong')
            for point in row:
                if type(point) is not int:
                    raise MatrixError('Matrix must contain only numbers')
        self._matrix_with_heights = np.array(matrix_with_heights)
    
    def size(self):
        return self._size
    
    def set_size(self, new_size):
        if type(new_size) is not int or new_size <= 0:
            raise MatrixSizeError('New size of the matrix must be a positive number')
        self._size = new_size
    
    def matrix_with_heights(self):
        return self._matrix_with_heights
    
    def set_matrix(self, new_matrix_with_heights):
        if len(new_matrix_with_heights) is not self._size:
            raise MatrixSizeError('Matrix Size is wrong')
        for row in new_matrix_with_heights:
            if len(row) is not self._size:
                raise MatrixSizeError('Matrix size is wrong')
            for point in row:
                if type(point) is not int:
                    raise MatrixError('Matrix must contain only numbers')
        self._matrix_with_heights = np.array(new_matrix_with_heights)

    def info(self):
        return(f'Size of the matrix is: {self._size}.\n Matrix: \n {self._matrix_with_heights}')
    
    def __str__(self):
        return self.info()


class PilotageMap:
    def __init__(self, ship, matrix):
        self._matrix = matrix
        self._ship = ship

    def convert_for_chart(self):
        points = []
        for row in self._matrix._matrix_with_heights:
            for i in range(0,self._matrix._size) :
                if row[i] >= 0 :
                    points += [1]
                if row[i] < 0 :
                    if row[i] <= self._ship._draft:
                        points += [-1]
                    else:
                        points += [0]
        map_chart_before_reshape = np.array(points)
        map_for_chart = map_chart_before_reshape.reshape(self._matrix._size,self._matrix._size)
        return map_for_chart

    def find_route(self, map_for_chart):
        possible_route = collections.deque([[(0,0)]])
        discovered = [(0,0)]
        while possible_route:
            route = possible_route.popleft()            
            j, i = route[-1]
            if j == (self._matrix._size - 1) and i == (self._matrix._size - 1):
                return route
            for j2, i2 in ((j+1,i), (j-1,i), (j,i+1), (j,i-1)):
                if 0 <= j2 < self._matrix._size and 0 <= i2 < self._matrix._size and map_for_chart[i2][j2] != 1 and map_for_chart[i2][j2] != 0 and (j2, i2) not in discovered:
                    possible_route += [route + [(j2, i2)]]
                    discovered += [(j2, i2)]

    def give_pointsX(self, route):
        x = []
        for point in route:
            x += [point[0]]
        return x

    def give_pointsY(self, route):
        y = []
        for point in route:
            y += [point[1]]
        return y

    def show_map(self):
        map_for_chart = self.convert_for_chart()
        route = self.find_route(map_for_chart)
        if route is None:
            return('Route cannot be found')
        else:
            xpoints = self.give_pointsX(route)
            ypoints = self.give_pointsY(route)

            plt.xticks(xpoints)
            plt.yticks(ypoints)
            plt.figure(1)
            plt.imshow(map_for_chart, interpolation='nearest')
            plt.grid(True)
            plt.plot(xpoints, ypoints,'o-r')
            plt.show()
            return('Route found')
