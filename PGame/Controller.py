import math
import pygame

from Utils.Const import *
from pygame.locals import *

class MainController(object):
    def __init__(self, model, view, viewM):
        self.model = model
        self.view = view
        self.viewM = viewM
        self.running = True

    def GiveStateToMain(self):
        return self.model.GiveState()

    def GiveLeaderBoardToView(self):
        list = self.model.GiveLeaderBoard()
        self.view.GetLeaderBoard(list)

    def ProcessMenuInput(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == MOUSEBUTTONDOWN:
                if self.viewM.startButton.draw(self.viewM.gameSurf):
                    self.model.GetRecordsFromCSV()
                    self.GiveLeaderBoardToView()
                    self.model.ChangeState(1)
                    self.model.FillMatrix()
                    self.view.Redraw()

                    while self.running:
                        self.ProcessGameInput()
                        self.view.Blit()
                        
                if self.viewM.oneColorDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyCCount(NumValues1)
                   
                if self.viewM.twoColorDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyCCount(NumValues2)
                    
                if self.viewM.threeColorDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyCCount(NumValues3)

                if self.viewM.oneDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyMatches(NeededMatchCount1)
                
                if self.viewM.twoDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyMatches(NeededMatchCount2)

                if self.viewM.threeDiffButton.draw(self.viewM.gameSurf):
                    self.model.ChangeDifficultyMatches(NeededMatchCount3)
                    
                    


    def ProcessGameInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.model.SaveRecordToCSV()
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button:
                    row, col = self.view.ConvertMousepos(event.pos)
                    row = int(math.floor(row))
                    col = int(math.floor(col))
                    if self.view.selection:
                        if self.view.selection[row][col]:
                            self.view.selection = None
                            self.model.SelectBlocks(row, col)
                            self.view.GetScore(self.model.score)
                        else:
                            self.view.selection = (
                                    self.model.GetNeighbours(row, col))
                    else:
                        self.view.selection = (
                                    self.model.GetNeighbours(row, col))
                    self.view.Redraw()
