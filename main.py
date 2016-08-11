import pygame
import random
from city_scroller import Scroller
from runnerSpriteClass import RunnerSprite

#ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit
pygame.init()

done = False
clock = pygame.time.Clock()
frameRate = 60 #fps

screenWidth = 600
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

backgroundColor = (0, 0, 50)

gameFont = pygame.font.SysFont("Verdana", 45)
fontColor = (255, 255, 255)

score = 0
#ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit-ScreenInit

#SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-

allSprites = pygame.sprite.Group()
goodSprites = pygame.sprite.Group()

#SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-SpriteGroupInit-

#ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-
FRONT_SCROLLER_COLOR = (102, 102, 255)
MIDDLE_SCROLLER_COLOR = (75, 75, 255)
BACK_SCROLLER_COLOR = (50, 50, 255)

sidewalk = 50

front_scroller = Scroller(screenWidth, 50, screenHeight - sidewalk, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(screenWidth, 100, screenHeight - sidewalk, MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(screenWidth, 250, screenHeight - sidewalk, BACK_SCROLLER_COLOR, 1)
#ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-ScrollerInit-

#RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-
mainCharacterColor = (180, 255, 255)
mainCharacterSize = (20, 30)
mainCharacterImage = "mainCharacterImage.png"

mainCharacter = RunnerSprite(mainCharacterImage)
allSprites.add(mainCharacter)
#RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-RunnerSpriteInit-

#GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-
goodSpriteCount = 0
goodSpriteSeconds = 0.75 * frameRate # a new sprite occurs every x seconds
goodSpriteSize = (30, 30)
goodSpritesImage = "goodSpriteImage.gif"
goodSpriteSpeed = 1

#GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-GoodSpritesInit-

#****************************************************************************************************************************************************************
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(backgroundColor)
################################################################################################################################################################
    # Setting up the background
    back_scroller.draw_buildings(screen)
    back_scroller.move_buildings()
    middle_scroller.draw_buildings(screen)
    middle_scroller.move_buildings()
    front_scroller.draw_buildings(screen)
    front_scroller.move_buildings()
    
    #Getting the mouse position
    mousePosition = pygame.mouse.get_pos()
    mouseX = mousePosition[0]
    mouseY = mousePosition[1]
    
    #Moving the runner on the screen
    mainCharacter.moveWithMouse(mouseX, mouseY)
    
    #Draw all the sprites
    allSprites.draw(screen)
    
    #Write score on screen
    screen.blit(gameFont.render( "Score: " + str(score), True, fontColor), [0, 0])
    
    #Check if the mainCharacter touched a goodSprite, up the score, and remove it from the list
    hitSpriteList = pygame.sprite.spritecollide(mainCharacter, goodSprites, True)
    for hitSprite in hitSpriteList:
        score += 1
        #print(score)
        allSprites.remove(hitSprite)
        hitSpriteList.remove(hitSprite)
    
    #Update good and bad sprites
    for goodSprite in goodSprites.sprites():
        goodSprite.move(goodSpriteSpeed)
        goodSprite.update(screenWidth, screenHeight)
    
    # Add a new goodSprite to the edge of the screen after every move
    if goodSpriteCount >= goodSpriteSeconds: 
        tempSprite = RunnerSprite(goodSpritesImage)
        tempSprite.setPosition(screenWidth, random.randint(goodSpriteSize[1], screenHeight - sidewalk))
        goodSprites.add(tempSprite)
        allSprites.add(tempSprite)
        goodSpriteCount = 0
    else:
        goodSpriteCount += 1
    
    if score % 10 == 0 and  score > 0:
        goodSpriteSeconds /= 1.05
        score += 1
    
################################################################################################################################################################
    pygame.display.flip()
    
    clock.tick(frameRate)

pygame.quit()
exit()