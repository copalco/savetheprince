import unittest

from savetheprince.presenter import Presenter
from tests.factories.area import AreaFactory


class TestPresenter(unittest.TestCase):

    def test_stores_current_hero_location(self) -> None:
        area = AreaFactory.create()
        new_area = AreaFactory.create()
        presenter = Presenter(area)
        presenter.store_hero_location(new_area)
        self.assertEqual(presenter.locate_hero(), new_area)
