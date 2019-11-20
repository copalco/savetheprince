import unittest

from savetheprince.map_hero import MapHero
from savetheprince.position import Position
from savetheprince.presenter import MapAreaNotFound
from savetheprince.presenter import Presenter
from savetheprince.size import Size
from tests.factories.map_area import MapAreaFactory
from tests.factories.area_id import AreaIdFactory


class TestPresenter(unittest.TestCase):

    def test_returns_position_for_hero_image(self) -> None:
        area = MapAreaFactory.create(Size(20, 40), Position(0, 0))
        hero = MapHero(size=Size(10, 20))
        presenter = Presenter(area)
        self.assertEqual(
            presenter.position_hero(hero, area.id),
            Position(5, 10),
        )

    def test_raises_map_area_not_found_if_no_area_with_a_given_id(
            self) -> None:
        presenter = Presenter()
        hero = MapHero(size=Size(10, 20))
        with self.assertRaises(MapAreaNotFound):
            presenter.position_hero(hero, AreaIdFactory.create())
