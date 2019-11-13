import time

import pygame


def run() -> None:
    pygame.init()
    screen = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF)
    background = pygame.Surface(screen.get_size())
    background.convert()
    screen.blit(background, (0, 0))
    should_continue = True
    while should_continue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_continue = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    should_continue = False
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    run()
