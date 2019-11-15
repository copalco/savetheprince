import os

import pygame


def run() -> None:
    pygame.init()
    display = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF)
    background = pygame.image.load(os.path.join('data', 'map.png'))
    background = pygame.transform.scale(background, (1280, 800))
    background.convert()
    hero = pygame.image.load(os.path.join('data', 'dwarf.png'))
    hero.convert()
    hero_size = hero.get_size()
    display.blit(background, (0, 0))
    field1_center_height = 137 / 2.0
    field1_center_width = 161 / 2.0
    hero_center_width = hero_size[0] / 2.0
    hero_center_height = hero_size[1] / 2.0
    hero_position = (
            round(field1_center_width - hero_center_width),
            round(field1_center_height - hero_center_height),
    )
    display.blit(hero, hero_position)
    pygame.display.set_caption('Save The Prince')
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
