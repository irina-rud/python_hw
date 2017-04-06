import sys
import random
import copy


def constant(f):
    def fset(self, value):
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


class creature_type(object):
    """It is a constant class to define predator,
    prey(let's name catch) and empty sell id.
    If we don't know spicification, it's trouble
    """
    @constant
    def predator():
        return 1

    @constant
    def catch():
        return 2

    @constant
    def empty():
        return 3

    @constant
    def trouble():
        return -1


class Creature:
    def __init__(self, death_p=0.2, reproduce_p=0.1, stay_on_sell_p=0.5, id=creature_type.trouble):
        self.properties = {'d': death_p, 'r': reproduce_p, 's': stay_on_sell_p,
                           'k': 0.0, 'h': 0, 'id': id}

    def count_cell(self, position, empty_neib, catch_neib, ocean):
        if random.random() < self.properties['d']:
            return None
        if len(empty_neib) == 0:
            return position
        if random.random() < self.properties['r']:
            child = random.choice(empty_neib)
            ocean[child] = ocean[position]
            empty_neib.remove(child)
        if random.random() < self.properties['s'] or len(empty_neib) == 0:
            return position
        new_position = random.choice(empty_neib)
        return new_position


class Predator(Creature):
    def __init__(self, death_p=0.2, rep_p=0.1, stay_p=0.5, kill_p=1.0, starv_rate=5):
        super().__init__(death_p, rep_p, stay_p, id=creature_type.predator)
        self.properties['k'] = kill_p
        self.properties['starv_rate'] = starv_rate
        self.properties['h'] = 0

    def count_cell(self, position, empty_neib, catch_neib, ocean):
        ++self.properties['h']
        if self.properties['h'] > self.properties['starv_rate']:
            return None
        position = super().count_cell(position, empty_neib, catch_neib, ocean)
        if position is None:
            return None
        for catch in catch_neib:
            if random.random() < self.properties['r']:
                ocean[catch] = Empty()
                self.properties['h'] = 0
                return position


class Catch(Creature):
    def __init__(self, death_p=0.2, reproduce_p=0.1, stay_on_sell_p=0.5):
        super().__init__(death_p=0.2, reproduce_p=0.1, stay_on_sell_p=0.5, id=creature_type.catch)


class Empty(Creature):
    def __init__(self):
        super().__init__(id=creature_type.empty)


class Ocean:
    """Class of the real ocean with creatures and emptiness
    """
    def fill(self):
        for i in range(self.shape_n):
            line = []
            for j in range(self.shape_m):
                if random.random() > self.random_rate:
                    if random.random() > self.random_rate:
                        line.append(copy.deepcopy(self.predator_class))
                    else:
                        line.append(copy.deepcopy(self.catch_class))
                else:
                    line.append(Empty())
            self.field.append(line)

    def __init__(self, shape=(10, 100), random_rate=0.5, predator_class=Predator(),
                 catch_class=Catch()):
        self.predator_class = predator_class
        self.catch_class = catch_class
        self.shape_n = shape[0]
        self.shape_m = shape[1]
        self.dij = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        self.field = []
        self.random_rate = random_rate
        self.fill()

    def process_cell(self, position):
        neibs = self.neighbor_indices(position)
        empty_neib = [ind for ind in neibs if self[ind].properties['id'] == creature_type.empty]
        catch_neib = [ind for ind in neibs if self[ind].properties['id'] == creature_type.catch]
        new_position = self[position].count_cell(position, empty_neib, catch_neib, self)
        if new_position is None:
            self[position] = Empty()
        elif new_position != position:
            self[new_position] = self[position]
            self[position] = Empty()

    def step(self):
        for i in range(self.shape_n):
            for j in range(self.shape_m):
                self.process_cell((i, j))

    def __getitem__(self, position):
        return self.field[position[0]][position[1]]

    def __setitem__(self, pos, value):
        self.field[pos[0]][pos[1]] = value

    def neighbor_indices(self, pos):
        i, j = pos
        if 0 < i < self.shape_n - 1 and 0 < j < self.shape_m - 1:
            return [(i + di, j + dj) for (di, dj) in self.dij]
        cells = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                if i + di < 0 or i + di >= self.shape_n:
                    continue
                if j + dj < 0 or j + dj >= self.shape_m:
                    continue
                cells.append((i + di, j + dj))
        return cells

    def __str__(self):
        st = ""
        for i in range(self.shape_n):
            for j in range(self.shape_m):
                if (self.field[i][j].p['id'] == creature_type.empty):
                    st += " "
                elif (self.field[i][j].p['id'] == creature_type.catch):
                    st += "o"
                elif (self.field[i][j].p['id'] == creature_type.predator):
                    st += "X"
                else:
                    st += "?"
            st += '\n'
        return st

if __name__ == '__main__':
    oc = Ocean()

    for i in range(10):
        oc.step()
