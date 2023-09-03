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


def test_sulfuras() -> None:
    """
    "Sulfuras", being a legendary item, never has to be sold or decreases in
    Quality.
    """
    items = [Item('Sulfuras, Hand of Ragnaros', 10, 80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 10
    assert items[0].quality == 80


def test_backstage_passes_quality_increases_before_concert() -> None:
    """
    "Backstage passes", like aged brie, increases in Quality as its SellIn value
    approaches.
    """
    items = [Item('Backstage passes to a TAFKAL80ETC concert', 10, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality > 0


def test_backstage_passes_quality_increases_by_2_10_days_before() -> None:
    """
    Backstage pass quality increases by 2 where there are 6-10 days left,
    inclusive.
    """
    items = [Item('Backstage passes to a TAFKAL80ETC concert', 10, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()  # 10 days left
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()  # 6 days left
    assert items[0].quality == 10


def test_backstage_passes_quality_increases_by_3_5_days_before() -> None:
    """Backstage pass quality increases by 3 where there are <= 5 days left."""
    items = [Item('Backstage passes to a TAFKAL80ETC concert', 5, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()  # 5 days left
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()
    gilded_rose.update_quality()  # 1 day left
    assert items[0].quality == 15


def test_backstage_passes_quality_0_after_concert() -> None:
    """Backstage pass quality drops to 0 after the concert."""
    items = [Item('Backstage passes to a TAFKAL80ETC concert', 0, 50)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
