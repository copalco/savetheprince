from dataclasses import dataclass
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


@dataclass(frozen=True)
class Size:
    width: int
    height: int


class Position(typing.NamedTuple):
    x: int
    y: int


class Area:

    def __init__(self, size: Size, position: Position):
        self._size = size
        self._position = position

    def get_centered(self, size: Size) -> Position:
        half_width = self._size.width / 2.0
        half_height = self._size.height / 2.0
        half_other_width = size.width / 2.0
        half_other_height = size.height / 2.0
        return Position(
            round(half_width - half_other_width) + self._position.x,
            round(half_height - half_other_height) + self._position.y,
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
                if event.key == pygame.K_RIGHT:
                    display.blit(background, (0, 0))
                    hero_position = get_center((67, 137), hero.get_size())
                    hero_position = (hero_position[0] + 167, hero_position[1])
                    display.blit(hero, hero_position)
                if event.key == pygame.K_LEFT:
                    display.blit(background, (0, 0))
                    hero_position = get_center((167, 137), hero.get_size())
                    hero_position = (hero_position[0], hero_position[1])
                    display.blit(hero, hero_position)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    run()
