import os

import pygame
from savetheprince.area import Area
from savetheprince.map_hero import MapHero
from savetheprince.maparea import MapArea
from savetheprince.maparea import AreaId
from savetheprince.circle import Circle
from savetheprince.position import Position
from savetheprince.presenter import Presenter
from savetheprince.size import Size


def run() -> None:
    pygame.init()
    display = pygame.display.set_mode((1280, 800), pygame.DOUBLEBUF)
    background = pygame.image.load(os.path.join('data', 'map.png'))
    background = pygame.transform.scale(background, (1280, 800))
    background.convert()
    hero = pygame.image.load(os.path.join('data', 'dwarf.png'))
    hero.convert()
    areas = [
        MapArea(AreaId('village'), Size(161, 137), Position(0, 0)),
        MapArea(AreaId('field-one'), Size(67, 137), Position(167, 0)),
        MapArea(AreaId('forest-one'), Size(78, 137), Position(240, 0)),
        MapArea(AreaId('forest-two'), Size(120, 137), Position(324, 0)),
        MapArea(AreaId('forest-three'), Size(110, 137), Position(450, 0)),
        MapArea(AreaId('forest-four'), Size(136, 137), Position(566, 0)),
        MapArea(AreaId('church'), Size(150, 137), Position(708, 0)),
        MapArea(AreaId('field-two'), Size(90, 137), Position(864, 0)),
        MapArea(AreaId('field-three'), Size(82, 137), Position(960, 0)),
        MapArea(AreaId('field-four'), Size(90, 137), Position(1046, 0)),
        MapArea(AreaId('town'), Size(136, 150), Position(1142, 0)),
        MapArea(AreaId('hut'), Size(116, 116), Position(1160, 166)),
        MapArea(AreaId('snow-forest'), Size(116, 146), Position(1160, 288)),
        MapArea(AreaId('mountain-hut'), Size(116, 76), Position(1160, 438)),
        MapArea(AreaId('snow-mountain'), Size(116, 88), Position(1160, 520)),
        MapArea(AreaId('barren-field-one'), Size(116, 50), Position(1160, 612)),
        MapArea(AreaId('dark-fortress'), Size(106, 130), Position(1172, 666)),
        MapArea(AreaId('barren-field-two'), Size(138, 130), Position(1028, 666)),
        MapArea(AreaId('temple'), Size(100, 130), Position(922, 666)),
        MapArea(AreaId('savannah'), Size(94, 130), Position(823, 666)),
        MapArea(AreaId('jungle-outside'), Size(126, 130), Position(692, 666)),
        MapArea(AreaId('barren-hills'), Size(158, 130), Position(530, 666)),
        MapArea(AreaId('bridge'), Size(90, 140), Position(436, 656)),
        MapArea(AreaId('mountains-one'), Size(102, 140), Position(329, 656)),
        MapArea(AreaId('mountains-two'), Size(114, 140), Position(210, 656)),
        MapArea(AreaId('field-five'), Size(70, 140), Position(137, 656)),
        MapArea(AreaId('capital'), Size(132, 156), Position(0, 640)),
        MapArea(AreaId('road-one'), Size(132, 90), Position(0, 543)),
        MapArea(AreaId('road-two'), Size(132, 92), Position(0, 445)),
        MapArea(AreaId('bridge-of-death'), Size(132, 102), Position(0, 338)),
        MapArea(AreaId('watchtower'), Size(132, 108), Position(0, 225)),
        MapArea(AreaId('road-to-village'), Size(132, 78), Position(0, 142)),
    ]
    game_areas = [
        Area(AreaId('village')),
        Area(AreaId('field-one')),
        Area(AreaId('forest-one')),
        Area(AreaId('forest-two')),
        Area(AreaId('forest-three')),
        Area(AreaId('forest-four')),
        Area(AreaId('church')),
        Area(AreaId('field-two')),
        Area(AreaId('field-three')),
        Area(AreaId('field-four')),
        Area(AreaId('town')),
        Area(AreaId('hut')),
        Area(AreaId('snow-forest')),
        Area(AreaId('mountain-hut')),
        Area(AreaId('snow-mountain')),
        Area(AreaId('barren-field-one')),
        Area(AreaId('dark-fortress')),
        Area(AreaId('barren-field-two')),
        Area(AreaId('temple')),
        Area(AreaId('savannah')),
        Area(AreaId('jungle-outside')),
        Area(AreaId('barren-hills')),
        Area(AreaId('bridge')),
        Area(AreaId('mountains-one')),
        Area(AreaId('mountains-two')),
        Area(AreaId('field-five')),
        Area(AreaId('capital')),
        Area(AreaId('road-one')),
        Area(AreaId('road-two')),
        Area(AreaId('bridge-of-death')),
        Area(AreaId('watchtower')),
        Area(AreaId('road-to-village')),
    ]
    circle = Circle(*areas)
    presenter = Presenter(*areas)
    display.blit(background, (0, 0))
    map_hero = MapHero(Size(*hero.get_size()))
    hero_position = presenter.position_hero(map_hero, AreaId('village'))
    current_area = areas[0]
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
                    current_area = circle.next(current_area)
                    hero_position = presenter.position_hero(
                        map_hero, current_area.id,
                    )
                    display.blit(hero, hero_position)
                if event.key == pygame.K_LEFT:
                    display.blit(background, (0, 0))
                    current_area = circle.previous(current_area)
                    hero_position = presenter.position_hero(
                        map_hero, current_area.id,
                    )
                    display.blit(hero, hero_position)
            pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    run()
