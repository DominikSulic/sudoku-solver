import pygame

pygame.init()
COLOR_ACTIVE = pygame.Color('#00FF00')
COLOR_INACTIVE = pygame.Color('#FFFFFF')
COLOR_WRONG = pygame.Color('#FF0000')
GIVEN_NUMBERS_COLOR = pygame.Color('#000000')
USER_CHOSEN_NUMBER_COLOR = pygame.Color('#808080')
GIVEN_FONT = pygame.font.SysFont("comicsans", 40)
USER_FONT = pygame.font.SysFont("comicsans", 35)

# Given numbers are numbers that are given at the start, you cant change them
class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x+3, y+3, width-6, height-6)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txtSurface = USER_FONT.render(text, True, self.color)
        self.whiteSurface = pygame.Surface((int(width - 12), int(height - 12)))
        # Used to "erase" the surface when you want to delete a number
        self.whiteSurface.fill(pygame.Color('#FFFFFF'))
        self.active = False
        self.erase = False
        self.containsANumber = False
        self.givenNumber = False


    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        # https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.erase = True
                    self.containsANumber = False

                if event.key == pygame.K_1:
                    self.text = '1'
                    self.containsANumber = True
                elif event.key == pygame.K_2:
                    self.text = '2'
                    self.containsANumber = True
                elif event.key == pygame.K_3:
                    self.text = '3'
                    self.containsANumber = True
                elif event.key == pygame.K_4:
                    self.text = '4'
                    self.containsANumber = True
                elif event.key == pygame.K_5:
                    self.text = '5'
                    self.containsANumber = True
                elif event.key == pygame.K_6:
                    self.text = '6'
                elif event.key == pygame.K_7:
                    self.text = '7'
                    self.containsANumber = True
                elif event.key == pygame.K_8:
                    self.text = '8'
                    self.containsANumber = True
                elif event.key == pygame.K_9:
                    self.text = '9'
                    self.containsANumber = True
                else:
                    self.text = ''

                self.txtSurface = USER_FONT.render(self.text, True, USER_CHOSEN_NUMBER_COLOR)
    

    def drawClickableButtons(self, screen):
        self.color = pygame.Color('#000000')
        self.txtSurface.fill(pygame.Color('#000000'))
        self.txtSurface = GIVEN_FONT.render(self.text, True, pygame.Color('#000000'))
        screen.blit(self.txtSurface, (self.rect.x, self.rect.y))
        #pygame.draw.rect(screen, self.color, self.rect, 3)

    def buttonClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
            else: return False

    def drawUserNumbers(self, screen):
        if self.active:
            pygame.draw.rect(screen, self.color, self.rect, 2)
        else:
            pygame.draw.rect(screen, self.color, self.rect, 2)

        if self.erase == True and not self.givenNumber:
            screen.blit(self.whiteSurface, (self.rect.x+5, self.rect.y+5))
            self.erase = False
        else:
            if self.containsANumber and not self.givenNumber:
                screen.blit(self.whiteSurface, (self.rect.x+5, self.rect.y+5))
            if not self.givenNumber: 
                screen.blit(self.txtSurface, (self.rect.x+5, self.rect.y+5))


    def drawGivenNumbers(self, screen, number):
        self.givenNumber = True
        self.text = number
        self.txtSurface = GIVEN_FONT.render(number, True, GIVEN_NUMBERS_COLOR)
        screen.blit(self.txtSurface, (self.rect.x+20, self.rect.y+15))


    def markWrong(self, isWrong):
        if isWrong:
            self.color = COLOR_WRONG
        else: 
            self.color = COLOR_INACTIVE
    
    def markWrongNumbers(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)