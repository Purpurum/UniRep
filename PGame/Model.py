import random
import csv

from Utils.Const import *

class Model(object):
    def __init__(self):
        #Реализация машины состояний мне показалась нерациональной в текущей ситуации, потому вот:
        self.gameState = 0

        #Настройки сложности
        self.neededMatches = NeededMatchCount1
        self.colorCount = NumValues1

        self.playerName = "Player"
        self.leaderBoard = []
        self.cols = Columns
        self.rows = Rows
        self.score = 0
        # Штука для синхронизации
        self.listeners = []

        #Для работы с CSV
        self.matches = [NeededMatchCount1, NeededMatchCount2, NeededMatchCount3]
        self.colors = [NumValues1, NumValues2, NumValues3]

        # Создание одного и того же семени в тестовых нуждах(в инит добавить seed=None)
        '''
        if seed:
            random.seed(seed)
        '''
        
        

    def ChangeState(self, num):
        self.gameState = num

    def GiveState(self):
        return self.gameState

    def ChangeDifficultyMatches(self, count):
        self.neededMatches = count
        print(f"changed to {count}")
    
    def ChangeDifficultyCCount(self, val):
        self.colorCount = val
        print(f"changed to {val}")

    def FillMatrix(self):
        self.matrix = [[random.choice(self.colorCount) for x in range(self.cols)]
            for y in range(self.rows)]

    def RegisterListener(self, listener):
        self.listeners.append(listener)

    def Notify(self, eventName, data):
        for listener in self.listeners:
            listener(eventName)

    #Проверялка соседних клеток
    def GetNeighbours(self, row, col):
        #Делает так, чтобы нули в матрице не проверялись
        if self.matrix[row][col] == 0:
            return None
        #Функция для отметки, чтоб 100500 раз её не пихать
        def mark_hotspots(row, col, n_row, n_col):
            #Проверяем совпадения
            if self.matrix[row][col] == self.matrix[n_row][n_col]:
                hotspot = (n_row, n_col)
                #Допольнительный список, чтоб не глючило
                #Перепроверяем при помощи доп. списка
                if not hotspot in tested:
                    #Говорим, что подходит
                    matches[n_row][n_col] = 1
                    #Добавляем в пачку подходящих, теперь можно переходить к следующим
                    stack.append(hotspot)
                    #Делаем так, чтобы оно не проверяло повторно проверенное
                    tested.append(hotspot)

        #Берём нулевую матрицу
        matches = [[0 for x in range(self.cols)]
                    for y in range(self.rows)]
        #Выбираем первую клетку
        matches[row][col] = 1
        #Добавляем её в дополнительный список и в пачку для тестирования
        tested = [(row, col)]
        stack = [(row, col)]
        while len(stack) > 0:
            #Проверяем соседние клетки
            row, col = stack.pop()
            if (col > 0):
                mark_hotspots(row, col, row, col - 1)
            if (col < self.cols - 1):
                mark_hotspots(row, col, row, col + 1)
            if (row > 0):
                mark_hotspots(row, col, row - 1, col)
            if (row < self.rows - 1):
                mark_hotspots(row, col, row + 1, col)
        #Подсчитываем количество совпавших клеток
        if sum([row.count(1) for row in matches]) > self.neededMatches: #последнее число - количество для выбора
            return matches
        else:
            return None

    def MatchRemove(self, matches):
        for r in range(self.rows):
            for c in range(self.cols):
                if matches[r][c] == 1:
                    self.matrix[r][c] = 0

    def GrawitateUp(self):
        tVar = 2
        while tVar != 0:
            for c in range(self.cols):
                #Выбираем стартовую строку
                r = self.rows - 1 #19
                while r > 0:
                    # Если клетка не пустая и над ней есть пустое место, то оно запускает этот иф
                    if self.matrix[r][c] > 0 and self.matrix[r - 1][c] == 0:
                        #Обмениваем клетки, чтобы создать эффект "Поднимания" вверх
                        self.matrix[r - 1][c] = self.matrix[r][c]
                        self.matrix[r][c] = 0
                        #Сообщая об этом, чтобы кто-то мог узнать об изменении матрицы
                        self.Notify('dropcell', [[r, c], [r - 1, c]])
                        #поднимаемся вверх для повторной проверки, если есть куда подниматься
                        if r < self.rows - 1:
                            r = r + 1
                    else:
                        #Если двигать нечего, то опускаемся вниз и проверяем верхние клетки
                        r = r - 1
            tVar = tVar - 1
    
    def DelDuplicates(self, list):
        cleanedList = []
        for l in list:
            if l not in cleanedList:
                cleanedList.append(l)
        return cleanedList

    def GiveLeaderBoard(self):
        return self.leaderBoard
        

    def GravitateLeft(self):
        def SideEmpty(col):
            #Проверяет, есть ли в соседней колонке данные
            for row in range(0, self.rows):
                if self.matrix[row][col] > 0:
                    return False
            return True

        def TransferColumn(col):
            #Копирует данные колонки
            for row in range(0, self.rows):
                self.matrix[row][col] = self.matrix[row][col + 1]
                self.matrix[row][col + 1] = 0
        #Запуск функции тут
        col = 0
        while col < self.cols - 1:
            if SideEmpty(col) and not SideEmpty(col + 1):
                TransferColumn(col)
                col = 0
            else:
                col = col + 1

    def SelectBlocks(self, row, col):
        m = self.GetNeighbours(row, col)
        if m:
            self.score = self.score + self.CountScore(m)
            self.MatchRemove(m)
            self.GrawitateUp()
            self.GravitateLeft()

    def CountScore(self, matches):
        count = 0
        
        for row in matches:
            count = count + row.count(1)
        return count * count

    
    def SaveRecordToCSV(self):
        for i in self.matches:
            for a in self.colors:
                if (self.neededMatches == i and self.colorCount == a):
                    self.leaderBoard.append([self.playerName, self.score])
                    with open(f'LeaderBoards/LeaderBoard{self.matches.index(i)+1}-{self.colors.index(a)+1}.csv', 'w', newline='') as csvfile:    
                        write = csv.writer(csvfile)
                        write.writerows(self.leaderBoard)
    
    def GetRecordsFromCSV(self):
        try:
            for i in self.matches:
                for a in self.colors:
                    if (self.neededMatches == i and self.colorCount == a):
                        file = open(f'LeaderBoards/LeaderBoard{self.matches.index(i)+1}-{self.colors.index(a)+1}.csv', "r", newline='')
                        rawLeaderBoard = list(csv.reader(file, delimiter=","))
                        self.leaderBoard = self.DelDuplicates(rawLeaderBoard)
                        file.close()
        except:
            print("whoops")