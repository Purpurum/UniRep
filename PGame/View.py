import pygame
from pygame.locals import *

from Utils.ViewButton import *
from Utils.Const import *


class View(object):
    def __init__(self, model):

        self.cols = Columns
        self.rows = Rows

        self.button = Button
        #Синхронизируем с моделью(ради одного единственного события)
        self.model = model
        model.RegisterListener(self.ModelEvent)

        #Считаем размер клеток, создаём окно
        self.gameSize = WindowScreenWidth, WindowScreenHeight
        self.screenSize = GameScreenWidth, GameScreenHeight
        self.block_size = GameScreenWidth / model.cols

        #Убираем выделение, которое почему-то сразу появляется, если этого не сделать
        self.selection = None

        #Инициализируем пайгейм
        pygame.init()
        
        #Зададим шрифт
        self.font = pygame.font.SysFont('Arial', 40)

        #Присвоим счет и запросим таблицу лидеров
        self.score = 0
        self.LeaderBoardList = []

        pygame.display.set_caption('Pgame')
        self.screen = pygame.display.set_mode(self.gameSize)
        self.clock = pygame.time.Clock()

        #Создаём поверхность для отрисовки
        self.gameSurf = pygame.Surface(self.gameSize)
        self.gameSurf.set_colorkey(Transparent)

        #Создаём игровую область(поверхность)
        self.selectSurf = pygame.Surface(self.screenSize)
        self.selectSurf.set_colorkey(Transparent)

    #Читаем таблицу лидеров
    def GetLeaderBoard(self, list):
        self.LeaderBoardList = list
        self.LeaderBoardList.sort(key = lambda x: int(x[1]), reverse=True) 

    def DrawBlocks(self):
        #Рисуем блоки и ставим прозрачный фон
        self.gameSurf.fill(Transparent)

        for j in range(len(self.model.matrix)):
            for k in range(len(self.model.matrix[j])):
                value = self.model.matrix[j][k]
                if value:
                    #Изменяем размер блоков, в зависимости от экрана
                    blockRect = pygame.Rect(k * self.block_size, j * self.block_size, self.block_size, self.block_size)
                    #Заполняем игровое поле блоками
                    self.gameSurf.fill(Colors[value], blockRect)

    
    def DrawSelection(self):
        #Отрисовываем выбор
        self.selectSurf.fill(Transparent)
        if not self.selection:
            return
        for j in range(len(self.selection)):
            for k in range(len(self.selection[j])):
                if self.selection[j][k]:
                    blockRect = pygame.Rect(k * self.block_size, j * self.block_size, self.block_size, self.block_size)
                    self.selectSurf.fill(SelectionColor, blockRect)

    def DrawSidebar(self):
        #Отрисовываем сайдбар
        self.button(600, 0, SideBarImg, 1).draw(self.gameSurf)
        self.gameSurf.blit(self.font.render(f'Счёт: {self.score}', True, SoftPurple), (620, 17))
        self.gameSurf.blit(self.font.render('Игрок - cчёт', True, SoftPurple), (660, 89))
        for i in self.LeaderBoardList:
            self.gameSurf.blit(self.font.render(f"{i}".replace("[","").replace("]","").replace(","," -").replace("'",""), True, Red), (660, 100+((self.LeaderBoardList.index(i)+1)*70)))
            if self.LeaderBoardList.index(i) == 5:
                break

        
        
       
    def GetScore(self, newScore):
        self.score = newScore

    def ConvertMousepos(self, pos):
        return pos[1] / self.block_size, pos[0] / self.block_size
    
    def Redraw(self):
        self.DrawBlocks()
        self.DrawSelection()
        self.DrawSidebar()

    def Blit(self):
        #Задний фон, да, кнопкой
        self.button(1, 1, BackGroundImg, 20).draw(self.screen)

        self.DrawSidebar()
        self.screen.blit(self.gameSurf, (0, 0))
        if self.selection:
            self.screen.blit(self.selectSurf, (0, 0))
        pygame.display.flip()
        self.clock.tick(FrameRate)
        
    def ModelEvent(self, eventName):
        #Сообщаем о том, что клетке пора бы уже подняться
        if eventName == "dropcell":
            self.DrawBlocks()
            self.Blit()

   

