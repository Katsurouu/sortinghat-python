# =====PyGame en benodigde functies importen=====
import pygame
import sys
from pygame.locals import *
# =====Deze imports zijn nodig om de videos af te spelen=====
import subprocess
from platform import system
# =====PyGame Window maken=====
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Sorteerhoed Saradomin')
screen = pygame.display.set_mode((1105, 755), 0, 32)
# =====Images laden=====
menuImg = pygame.image.load("Artworks/bimg.png")
quizImg = pygame.image.load("Artworks/Kahoot.png")
easterImg = pygame.image.load("Artworks/Kahoot_edited.png")
helpImg = pygame.image.load("Artworks/Help.png")
resultImg = pygame.image.load("Artworks/Result.png")
lynnImg = pygame.image.load("Artworks/Lynn.png")
# =====Font selecteren=====
font = pygame.font.SysFont(None, 25)
font2 = pygame.font.SysFont(None, 25)
font3 = pygame.font.SysFont(None, 40)


# =====Muziek veranderen=====
def muziek_change(nr):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(f"Absolute Bangers/{nr}.mp3")
    pygame.mixer.music.play(-1)


# =====Vragen ophalen=====
def vragen_ophalen():
    with open("Nuclear Launch Codes/meerkeuzevragen.txt") as my_file:
        data = my_file.read()
    lijst_vragen = data.split('\n')
    vragenlijst = []
# =====Vragen en antwoorden splitten=====
    for item in lijst_vragen:
        if len(item) > 1:
            vraag_split = item.split(';')
            vragenlijst.append(vraag_split)
    return vragenlijst


# =====Functie om tekst op het scherm te tonen, centreert de tekst=====
def write(text, x, y, color, font):
    text = font.render(text, 1, pygame.Color(color))
    text_rect = text.get_rect(center=(x, y))
    screen.blit(text, text_rect)
    return text


# =====Globale variabelen (Sorry voor de luiheid :( )=====
click = False
vragen = vragen_ophalen()
spec = 0


# =====Main menu tonen=====
def main_menu():
    pygame.mixer.music.load("Absolute Bangers/Start_muziek.mp3")
    pygame.mixer.music.play(-1)
    while True:
        # =====Background img tonen=====
        global click
        screen.blit(menuImg, (0, 0))
        # ===== Muis positie bijhouden en knoppen een positie geven =====
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(15, 585, 525, 125)
        button_2 = pygame.Rect(560, 585, 525, 125)
        # ===== Knoppen klikbaar maken =====
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                help()

        # ===== Sluit app af op kruisje =====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# ===== Dit is de quiz =====
def game():
    # =====Variabelen=====
    global click
    click = False
    song = 1
    running = True
    vraagnummer = 0
    fict = 0
    se = 0
    bdam = 0
    iat = 0
    result = 0
    img = quizImg

    muziek_change(song)

    while running:
        # =====Laat een kahootscherm zien met de vraag=====
        screen.blit(img, (0, 0))
        write(vragen[vraagnummer][0], 552, 40, "Black", font)
        # =====Maakt de knoppen klikbaar en zet tekst in de knoppen=====
        mx, my = pygame.mouse.get_pos()
        # =====Rode knop=====
        button_1 = pygame.Rect(2, 500, 540, 110)
        write(vragen[vraagnummer][1], 300, 540, "White", font2)
        write(vragen[vraagnummer][2], 300, 555, "White", font2)
        write(vragen[vraagnummer][3], 300, 570, "White", font2)
        # =====Blauwe knop=====
        button_2 = pygame.Rect(560, 500, 540, 110)
        write(vragen[vraagnummer][4], 850, 540, "White", font2)
        write(vragen[vraagnummer][5], 850, 555, "White", font2)
        write(vragen[vraagnummer][6], 850, 570, "White", font2)
        # =====Gele knop=====
        button_3 = pygame.Rect(2, 629, 540, 110)
        write(vragen[vraagnummer][7], 300, 665, "White", font2)
        write(vragen[vraagnummer][8], 300, 680, "White", font2)
        write(vragen[vraagnummer][9], 300, 695, "White", font2)
        # =====Groene knop=====
        button_4 = pygame.Rect(560, 629, 540, 110)
        write(vragen[vraagnummer][10], 850, 665, "White", font2)
        write(vragen[vraagnummer][11], 850, 680, "White", font2)
        write(vragen[vraagnummer][12], 850, 695, "White", font2)
        # ====='Next' knop (muziek)=====
        button_5 = pygame.Rect(995, 106, 94, 46)
        # =====Easter egg knop=====
        button_6 = pygame.Rect(52, 233, 105, 105)
        # =====Gaat naar volgende vraag als er geklikt wordt=====
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            if click:
                fict += 1
                vraagnummer += 1
        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            if click:
                se += 1
                vraagnummer += 1
        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, (255, 255, 0), button_3)
            if click:
                bdam += 1
                vraagnummer += 1
        if button_4.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 255, 0), button_4)
            if click:
                iat += 1
                vraagnummer += 1
        # ===== Als er geklikt wordt op 'Skip', gaat hij naar het volgende liedje =====
        if button_5.collidepoint((mx, my)):
            pygame.draw.rect(screen, (0, 0, 255), button_5)
            if click:
                song += 1
                if song > 9:
                    song = 1
                muziek_change(song)
        # ===== Easter egg activeren =====
        if button_6.collidepoint((mx, my)):
            pos = pygame.mouse.get_pos()
            purple = (148, 0, 211)
            yellow = (255, 255, 0)
            if img == easterImg:
                colour = yellow
            else:
                colour = purple
            pygame.draw.circle(screen, colour, pos, 20)
            if click:
                if img == easterImg:
                    img = quizImg
                else:
                    img = easterImg
                screen.blit(img, (0, 0))

        # =====Als er op het kruisje geklikt wordt, sluit de applicatie=====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # =====Als er geklikt wordt, wordt dit door de applicatie waargenomen=====
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        # =====Als het einde van de list bereikt is, ga je naar de resultaten=====
        # =====Ik weet dat dit een hele onhandige methode is, sorry voor de spaghetticode =====
            if vraagnummer == 16:
                if fict > se:
                    if fict > bdam:
                        if fict > iat:
                            result = 1
                if se > fict:
                    if se > bdam:
                        if se > iat:
                            result = 2
                if bdam > fict:
                    if bdam > se:
                        if bdam > iat:
                            result = 3
                if iat > fict:
                    if iat > se:
                        if iat > bdam:
                            result = 4
                results(result)

        pygame.display.update()
        mainClock.tick(60)


# ====='Help' tonen=====
def help():
    running = True
    global click
    click = False
    while running:
        # ===== Laat help img zien=====
        screen.blit(helpImg, (0, 0))
        # ===== Main menu knop
        button_1 = pygame.Rect(400, 680, 300, 60)
        # ===== Main menu =====
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        # ===== Events =====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # =====Als er geklikt wordt, wordt dit door de applicatie waargenomen=====
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# ===== Resultaat =====
def results(spec):
    pygame.mixer.music.stop()
    running = True
    global click
    click = False
    # ===== Videos ======
    # ===== Controleert welke OS de gebruiker heeft =====
    if system() == "Windows":
        subprocess.run(['start', f"Filmpjes/{spec}.mp4"], shell=True)
    else:
        subprocess.run(['open', f"Filmpjes/{spec}.mp4"], check=True)
    while running:
        # ===== Laat resultaat img zien=====
        screen.blit(resultImg, (0, 0))
        # ===== Laat specialisatienummer zien =====
        write(str(spec), 552, 350, "White", font3)
        # ===== Knoppen =====
        button_1 = pygame.Rect(70, 680, 300, 60)
        button_2 = pygame.Rect(735, 680, 300, 60)
        # ===== Main menu =====
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        if button_2.collidepoint((mx, my)):
            if click:
                lynn()
        # ===== Events =====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # =====Als er geklikt wordt, wordt dit door de applicatie waargenomen=====
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# ===== Lynn heeft een speciale functie =====
def lynn():
    pygame.mixer.music.load("Absolute Bangers/Lynn.mp3")
    pygame.mixer.music.play(-1)
    running = True
    global click
    click = False
    while running:
        # ===== Laat lynn img zien=====
        screen.blit(lynnImg, (0, 0))
        # ===== Knoppen =====
        button_1 = pygame.Rect(70, 680, 300, 60)
        # ===== Main menu =====
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu()
        # ===== Events =====
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # =====Als er geklikt wordt, wordt dit door de applicatie waargenomen=====
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()
