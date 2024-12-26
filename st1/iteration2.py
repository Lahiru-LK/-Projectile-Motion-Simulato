#-import pygame, math, sys--------------------------------------------------------------------------------

import pygame
import math
import sys

#-initialization----------------------------------------------------------------------------------------------

pygame.init()

#-constant-----------------------------------------------------------------------------------------------------

FPS = 60
FontSize = 24
DarkBlue = (25, 25, 112)
Red = (255, 99, 71)
Green = (34, 139, 34)
Blue = (100, 149, 237)
Gray = (200, 200, 200)
Black = (0, 0, 0)
White = (255, 255, 255)
WindowHeight = 700
WindowWidth = 1000

#-UI-Class-----------------------------------------------------------------------------------------------------------

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, FontSize)
        self.inputBoxes = self.createInputBoxes()
    def createInputBoxes(self):
        labels = ["Velocity", "Angle", "Mass", "Air Resistance", "Gravity", "Radius", "Air Density"]
        YPosition = [55, 95, 135, 175, 215, 255, 295]
        return [INPUTS(100, y, 130, 30, "0", self.font) for y in YPosition]
    def drawUi(self, screen, isSettingsVisible):
        if isSettingsVisible:
            pygame.draw.rect(screen, DarkBlue, pygame.Rect(10, 10, 300, WindowHeight - 230))
            pygame.draw.rect(screen, Blue, pygame.Rect(10, 10, 300, 40))
            titleText = self.font.render("Parameters", True, White)
            screen.blit(titleText, (20, 15))
            labels = ["Velocity", "Angle", "Mass", "Air Resistance", "Gravity", "Radius", "Air Density"]
            labelX = 20
            boxX = 150
            yOffset = 60
            rowSpacing = 40
            for i, label in enumerate(labels):
                labelSurface = self.font.render(label, True, White)
                screen.blit(labelSurface, (labelX, yOffset))
                self.inputBoxes[i].rect.x = boxX
                self.inputBoxes[i].rect.y = yOffset - 5
                self.inputBoxes[i].update(screen)
                yOffset += rowSpacing

    def simulationControl(self, screen):
        buttonX = WindowWidth - 150
        buttonY = 20
        buttonWidth, buttonHeight = 120, 40
        buttonSpacing = 50
        pygame.draw.rect(screen, Green, pygame.Rect(buttonX, buttonY, buttonWidth, buttonHeight))
        pygame.draw.rect(screen, Blue, pygame.Rect(buttonX, buttonY + buttonSpacing, buttonWidth, buttonHeight))
        pygame.draw.rect(screen, Red, pygame.Rect(buttonX, buttonY + 2 * buttonSpacing, buttonWidth, buttonHeight))
        screen.blit(self.font.render("Start", True, White), (buttonX + 30, buttonY + 10))
        screen.blit(self.font.render("Pause", True, White), (buttonX + 30, buttonY + buttonSpacing + 10))
        screen.blit(self.font.render("Reset", True, White), (buttonX + 30, buttonY + 2 * buttonSpacing + 10))
        return (
            pygame.Rect(buttonX, buttonY, buttonWidth, buttonHeight),
            pygame.Rect(buttonX, buttonY + buttonSpacing, buttonWidth, buttonHeight),
            pygame.Rect(buttonX, buttonY + 2 * buttonSpacing, buttonWidth, buttonHeight),
        )


#-INPUT-Class-----------------------------------------------------------------------------------------------------------

class INPUTS:
    def __init__(self, x, y, w, h, initialText, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = pygame.Color("LightSkyBlue3")
        self.text = initialText
        self.active = False
        self.change = False
        self.font = font
    def update(self, screen):
        txtSurface = self.font.render(self.text, True, self.color)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(txtSurface, (self.rect.x + 5, self.rect.y + 5))
    def handleEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = pygame.Color("DodgerBlue2") if self.active else pygame.Color("LightSkyBlue3")
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.change = True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.unicode.isdigit() or event.unicode in ".-":
                    self.text += event.unicode
    def getValue(self):
        try:
            return float(self.text)
        except ValueError:
            return 0.0


#-RENDERER-Class-----------------------------------------------------------------------------------------------------------

class RENDERER:
    def __init__(self):
        self.font = pygame.font.Font(None, FontSize)
    def drawProjectile(self, screen, projectile):
        if len(projectile.positions) > 1:
            pygame.draw.lines(screen, Black, False, [(int(pos[0]), int(pos[1])) for pos in projectile.positions], 2)

    def drawEquations(self, screen, projectile):
        if not projectile.running:
            textLines = [
                f"Velocity: {projectile.velocity:.2f}",
                f"Angle: {projectile.angle:.2f}",
                f"Mass: {projectile.mass:.2f}",
                f"Air Resistance: {projectile.airResistance:.2f}",
                f"Gravity: {projectile.gravity:.2f}",
                f"Radius: {projectile.radius:.2f}",
                f"Air Density: {projectile.airVelocity:.2f}",
                f"Max Vertical Height: {WindowHeight - projectile.maxHeight:.2f}",
                f"Horizontal Distance: {projectile.maxDistance:.2f}"
            ]
            yOffset = 10
            for line in textLines:
                textSurface = self.font.render(line, True, Black)
                screen.blit(textSurface, (WindowWidth - 350, yOffset))
                yOffset += FontSize + 5


#-PHYSICSENGINE-Class-----------------------------------------------------------------------------------------------------------

class PHYSICSENGINE:
    def __init__(self):
        self.vx = 0
        self.vy = 0
        self.radius = 0
        self.Area = 3.14159 * (self.radius ** 2)
        self.collision = False
        self.velocity = 0
        self.airResistance = 0
        self.airVelocity = 1.22
        self.angle = 0
        self.mass = 0
        self.gravity = 9.81
        self.x = 100
        self.y = WindowHeight - 50
        self.initial_y = self.y
        self.maxHeight = self.y
        self.maxDistance = self.x
        self.positions = [(self.x, self.y)]
        self.t = 0
        self.running = False
        self.bounceCoefficient = 0.75
    def start(self):
        self.running = True
    def reset(self):
        self.__init__()
    def pause(self):
        self.running = False
    def setVelocityANDangle(self, velocity, angle):
        self.velocity = velocity
        self.angle = angle
        self.vx = self.velocity * math.cos(math.radians(self.angle))
        self.vy = -self.velocity * math.sin(math.radians(self.angle))  # Negative for upward movement
    def update(self, dt):
            if not self.running:
                return
            speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
            drag = 0.5 * self.airResistance * self.airVelocity * self.Area * (speed ** 2)
            drag = drag / self.mass
            self.vx -= drag * (self.vx / speed) * dt
            self.vy -= drag * (self.vy / speed) * dt
            self.vy += self.gravity * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            if self.vy < 0 and self.y < self.maxHeight:
                self.maxHeight = self.y
                self.maxDistance = self.x
            if self.y >= WindowHeight - 50 - self.radius:
                self.y = WindowHeight - 50 - self.radius
                self.vy *= -self.bounceCoefficient
                if abs(self.vy) < 0.1:
                    self.vy = 0
                    self.running = False
            self.positions.append((self.x, self.y))

#-MAIN-Class-----------------------------------------------------------------------------------------------------------

class MAIN:
    def run(self):
        screen = pygame.display.set_mode((WindowWidth, WindowHeight))
        pygame.display.set_caption("PROJECTILE SIMULATOR")
        clock = pygame.time.Clock()
        ui = UI()
        renderer = RENDERER()
        projectile = PHYSICSENGINE()
        startButton, pauseButton, resetButton = None, None, None
        isSettingVisible = True
        running = True
        while running:
            dt = clock.tick(FPS) / 1000.00
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for box in ui.inputBoxes:
                    box.handleEvent(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if startButton and startButton.collidepoint(event.pos):
                        massValue = ui.inputBoxes[2].getValue()
                        if massValue == 0:
                            print("ERROR: Mass cannot BE ZERO")
                            ui.inputBoxes[2].color = pygame.Color("red")
                        else:
                            projectile.setVelocityANDangle(ui.inputBoxes[0].getValue(), ui.inputBoxes[1].getValue())
                            projectile.mass = massValue
                            projectile.airResistance = ui.inputBoxes[3].getValue()
                            projectile.gravity = ui.inputBoxes[4].getValue()
                            projectile.radius = ui.inputBoxes[5].getValue()
                            projectile.airVelocity = ui.inputBoxes[6].getValue()
                            projectile.start()
                            isSettingVisible = False
                    elif pauseButton and pauseButton.collidepoint(event.pos):
                        projectile.pause()
                    elif resetButton and resetButton.collidepoint(event.pos):
                        projectile.reset()
                        isSettingVisible = True
            if projectile.running:
                projectile.update(dt)
            screen.fill(White)
            startButton, pauseButton, resetButton = ui.simulationControl(screen)
            if isSettingVisible:
                ui.drawUi(screen, True)
            renderer.drawProjectile(screen, projectile)
            renderer.drawEquations(screen, projectile)
            pygame.display.flip()
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    MAIN().run()
