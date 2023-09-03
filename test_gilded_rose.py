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


def test_aged_brie_increases_quality() -> None:
    """ "Aged Brie" actually increases in Quality the older it gets."""
    items = [Item('Aged Brie', 1, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1

    # Past its sell by date, it increases in quality by 2
    gilded_rose.update_quality()
    assert items[0].quality == 3


def test_quality_never_more_than_50() -> None:
    """The Quality of an item is never more than 50."""
    items = [Item('Aged Brie', 0, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 50
