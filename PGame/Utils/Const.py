import pygame

#НЕ МЕНЯТЬ БЕЗ НЕВЕРОЯТНО ВАЖНОЙ ПРИЧИНЫ!
GameScreenWidth = 600
GameScreenHeight = 600
WindowScreenWidth = 900
WindowScreenHeight = 600

#Фэпээсы
FrameRate = 120

#Желательно оставлять одинаковыми
Columns = 20
Rows = 20

#Цвета
Transparent = (255, 0, 255)
Black = (0, 0, 0)
White = (255, 255, 255)
SoftWhite = (230, 230, 230)
Yellow = (200, 200, 0)
Green = (0, 220, 0)
Red = (200, 0, 0)
SoftRed = (150, 0, 0)
Blue = (0, 0, 220)
DarkPurple = (100, 0, 100)
Purple = (200, 0, 200)
SoftPurple = (150, 50, 150)
MediumPurple = (150, 0, 150)
BGColor = Black
SelectionColor = Red

Colors = (Black, Purple, DarkPurple, MediumPurple, SoftWhite, SoftRed)

#Сложность 1
NeededMatchCount1 = 1
ColorsCout1 = 3
NumValues1 = [1, 2, 3]


#Сложность 2
NeededMatchCount2 = 2
ColorsCout2 = 4
NumValues2 = [1, 2, 3, 4]


#Сложность 3
NeededMatchCount3 = 3
ColorsCout3 = 5
NumValues3 = [1, 2, 3, 4, 5]


#Пути к картинкам
SartImg = pygame.image.load("src/STARTBTN.png")
DiffImg = pygame.image.load("src/DIFFICULTYBTN.png")
ColorImg = pygame.image.load("src/COLORBTN.png")
OneImg = pygame.image.load("src/1BTN.png")
TwoImg = pygame.image.load("src/2BTN.png")
ThreeImg = pygame.image.load("src/3BTN.png")
BackGroundImg = pygame.image.load("src/BACKGROUND.png")
SideBarImg = pygame.image.load("src/SIDEBAR.png")


