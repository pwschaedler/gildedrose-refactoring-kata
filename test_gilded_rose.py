"""Gilded rose tests."""

from gilded_rose import GildedRose, Item


def test_passed_sell_by_double_quality_degrade() -> None:
    """Once the sell by date has passed, Quality degrades twice as fast."""
    items = [Item('foo', 0, 2)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0


def test_quality_never_negative() -> None:
    """The Quality of an item is never negative."""
    items = [Item('foo', 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
