import pygame

from pygame.locals import *

from Utils.ViewButton import *
from Utils.Const import *


class ViewMenu(object):
    def __init__(self):

        self.button = Button

        #Устанавливаем размер окна
        self.gameSize = WindowScreenWidth, WindowScreenHeight

        #Инициализируем пайгейм
        pygame.init()
        
        #Зададим шрифт
        self.font = pygame.font.SysFont('Arial', 25)

        #Присвоим счет и запросим таблицу лидеров
        self.LeaderBoardList = []

        pygame.display.set_caption('PGame')
        self.screen = pygame.display.set_mode(self.gameSize)
        self.clock = pygame.time.Clock()

        #Создаём поверхность для отрисовки
        self.gameSurf = pygame.Surface(self.gameSize)
        self.gameSurf.set_colorkey(Transparent)


    #Читаем таблицу лидеров
    def GetLeaderBoard(self, list):
        self.LeaderBoardList = list
        self.LeaderBoardList.sort(key = lambda x: int(x[1]), reverse=True) 


    def DrawMenu(self):
        #Создаём кнопки 
        self.startButton = self.button(20, 480, SartImg, 7)
        self.oneColorDiffButton = self.button(700, 245, OneImg, 7)
        self.twoColorDiffButton = self.button(700, 360, TwoImg, 7)
        self.threeColorDiffButton = self.button(700, 475, ThreeImg, 7)
        self.oneDiffButton = self.button(425, 130, OneImg, 7)
        self.twoDiffButton = self.button(425, 245, TwoImg, 7)
        self.threeDiffButton = self.button(425, 360, ThreeImg, 7)

        #Создаём пластины с текстом
        diffThumb = self.button(350, 20, DiffImg, 7)
        ColorThumb = self.button(600, 120, ColorImg, 8)

        #Рисуем всё это безобразие
        self.startButton.draw(self.gameSurf)
        diffThumb.draw(self.gameSurf) 
        ColorThumb.draw(self.gameSurf)  
        self.oneDiffButton.draw(self.gameSurf)
        self.twoDiffButton.draw(self.gameSurf)
        self.threeDiffButton.draw(self.gameSurf)
        self.oneColorDiffButton.draw(self.gameSurf)
        self.twoColorDiffButton.draw(self.gameSurf)
        self.threeColorDiffButton.draw(self.gameSurf)  

    


    def Blit(self):
        #Задний фон, да, кнопкой
        self.button(1, 1, BackGroundImg, 20).draw(self.gameSurf)

        self.DrawMenu()
        self.screen.blit(self.gameSurf, (0, 0))
        pygame.display.flip()
        self.clock.tick(FrameRate)
        

    

   

