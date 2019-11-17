from dataclasses import dataclass
import os
import typing

import pygame


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

    def centered(self, size: Size) -> Position:
        half_width = self._size.width / 2.0
        half_height = self._size.height / 2.0
        half_other_width = size.width / 2.0
        half_other_height = size.height / 2.0
        return Position(
            round(half_width - half_other_width) + self._position.x,
            round(half_height - half_other_height) + self._position.y,
        )


class UnknownArea(Exception):

    pass


class Circle(object):

    def __init__(self, *areas: Area) -> None:
        self._areas = areas

    def next(self, current_area: Area) -> Area:
        for index, area in enumerate(self._areas):
            if area == current_area:
                try:
                    return self._areas[index + 1]
                except IndexError:
                    return self._areas[0]
        raise UnknownArea()

    def previous(self, current_area: Area) -> Area:
        for index, area in enumerate(self._areas):
            if area == current_area:
                return self._areas[index - 1]
        raise UnknownArea()


class Game:

    def __init__(self, current_area: Area) -> None:
        self._current_hero_location: Area = current_area

    def store_hero_location(self, area: Area) -> None:
        self._current_hero_location = area

    def locate_hero(self) -> Area:
        return self._current_hero_location


def run() -> None:
    pygame.init()
    display = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF)
    background = pygame.image.load(os.path.join('data', 'map.png'))
    background = pygame.transform.scale(background, (1280, 800))
    background.convert()
    hero = pygame.image.load(os.path.join('data', 'dwarf.png'))
    hero.convert()
    areas = [
        Area(Size(161, 137), Position(0, 0)),
        Area(Size(67, 137), Position(167, 0)),
        Area(Size(78, 137), Position(240, 0)),
        Area(Size(120, 137), Position(324, 0)),
        Area(Size(110, 137), Position(450, 0)),
        Area(Size(136, 137), Position(566, 0)),
        Area(Size(150, 137), Position(708, 0)),
        Area(Size(90, 137), Position(864, 0)),
        Area(Size(82, 137), Position(960, 0)),
        Area(Size(90, 137), Position(1046, 0)),
        Area(Size(136, 150), Position(1142, 0)),
        Area(Size(116, 116), Position(1160, 166)),
        Area(Size(116, 146), Position(1160, 288)),
        Area(Size(116, 76), Position(1160, 438)),
        Area(Size(116, 88), Position(1160, 520)),
        Area(Size(116, 50), Position(1160, 612)),
        Area(Size(106, 130), Position(1172, 666)),
        Area(Size(138, 130), Position(1028, 666)),
        Area(Size(100, 130), Position(922, 666)),
        Area(Size(94, 130), Position(823, 666)),
        Area(Size(126, 130), Position(692, 666)),
        Area(Size(158, 130), Position(530, 666)),
        Area(Size(90, 140), Position(436, 656)),
        Area(Size(102, 140), Position(329, 656)),
        Area(Size(114, 140), Position(210, 656)),
        Area(Size(70, 140), Position(137, 656)),
        Area(Size(132, 156), Position(0, 640)),
        Area(Size(132, 90), Position(0, 543)),
        Area(Size(132, 92), Position(0, 445)),
        Area(Size(132, 102), Position(0, 338)),
        Area(Size(132, 108), Position(0, 225)),
        Area(Size(132, 78), Position(0, 142)),
    ]
    circle = Circle(*areas)
    game = Game(areas[0])
    current_area = areas[0]
    display.blit(background, (0, 0))
    hero_position = current_area.centered(Size(*hero.get_size()))
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
                    hero_location = game.locate_hero()
                    game.store_hero_location(circle.next(hero_location))
                    current_area = circle.next(current_area)
                    hero_position = current_area.centered(
                        Size(*hero.get_size())
                    )
                    display.blit(hero, hero_position)
                if event.key == pygame.K_LEFT:
                    display.blit(background, (0, 0))
                    hero_location = game.locate_hero()
                    game.store_hero_location(circle.previous(hero_location))
                    current_area = circle.previous(current_area)
                    hero_position = current_area.centered(
                        Size(*hero.get_size())
                    )
                    display.blit(hero, hero_position)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    run()
