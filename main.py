import pygame
import sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Wordle | Main Menu")

BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        EASY_BUTTON = Button(
            image=None,
            pos=(640, 150),
            text_input="EASY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        DIFF_BUTTON = Button(
            image=None,
            pos=(640, 300),
            text_input="DIFFICULT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        EXPERT_BUTTON = Button(
            image=None,
            pos=(640, 450),
            text_input="EXPERT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        OPTIONS_BACK = Button(
            image=None,
            pos=(640, 600),
            text_input="BACK",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for button in [EASY_BUTTON, DIFF_BUTTON, EXPERT_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    import wordle
                if DIFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    import wordlediff
                if EXPERT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    import wordlexpert
                if DIFF_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("WORDLE|MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(
            image=pygame.image.load("assets/Play Rect.png"),
            pos=(640, 300),
            text_input="PLAY",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )
        QUIT_BUTTON = Button(
            image=pygame.image.load("assets/Quit Rect.png"),
            pos=(640, 450),
            text_input="QUIT",
            font=get_font(75),
            base_color="#d7fcd4",
            hovering_color="White"
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main_menu()