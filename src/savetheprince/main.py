import os
import typing

import pygame


def get_center(first_area: typing.Tuple[int, int], second_area: typing.Tuple[int, int]) -> typing.Tuple[int, int]:
    first_area_width_center = first_area[0] / 2.0
    first_area_height_center = first_area[1] / 2.0
    second_area_width_center = second_area[0] / 2.0
    second_area_height_center = second_area[1] / 2.0
    return (
        round(first_area_width_center - second_area_width_center),
        round(first_area_height_center - second_area_height_center),
    )


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
    hero_position = get_center((167, 137), hero.get_size())
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
