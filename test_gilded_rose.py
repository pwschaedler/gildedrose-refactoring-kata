"""Gilded rose tests."""

from aged_brie import AGED_BRIE
from backstage_pass import BACKSTAGE_PASS
from conjured import CONJURED
from gilded_rose import Item, update_quality
from sulfuras import SULFURAS


def test_passed_sell_by_double_quality_degrade() -> None:
    """Once the sell by date has passed, Quality degrades twice as fast."""
    items = [Item('foo', 0, 2)]
    update_quality(items)
    assert items[0].quality == 0


def test_quality_never_negative() -> None:
    """The Quality of an item is never negative."""
    items = [Item('foo', 0, 0)]
    update_quality(items)
    assert items[0].quality == 0


def test_aged_brie_increases_quality() -> None:
    """ "Aged Brie" actually increases in Quality the older it gets."""
    items = [Item(AGED_BRIE, 1, 0)]
    update_quality(items)
    assert items[0].quality == 1

    # Past its sell by date, it increases in quality by 2
    update_quality(items)
    assert items[0].quality == 3


def test_quality_never_more_than_50() -> None:
    """The Quality of an item is never more than 50."""
    items = [Item(AGED_BRIE, 0, 50)]
    update_quality(items)
    assert items[0].quality == 50


def test_sulfuras() -> None:
    """
    "Sulfuras", being a legendary item, never has to be sold or decreases in
    Quality.
    """
    items = [Item(SULFURAS, 10, 80)]
    update_quality(items)
    assert items[0].sell_in == 10
    assert items[0].quality == 80


def test_backstage_passes_quality_increases_before_concert() -> None:
    """
    "Backstage passes", like aged brie, increases in Quality as its SellIn value
    approaches.
    """
    items = [Item(BACKSTAGE_PASS, 10, 0)]
    update_quality(items)
    assert items[0].quality > 0


def test_backstage_passes_quality_increases_by_2_10_days_before() -> None:
    """
    Backstage pass quality increases by 2 where there are 6-10 days left,
    inclusive.
    """
    items = [Item(BACKSTAGE_PASS, 10, 0)]
    update_quality(items)  # 10 days left
    update_quality(items)
    update_quality(items)
    update_quality(items)
    update_quality(items)  # 6 days left
    assert items[0].quality == 10


def test_backstage_passes_quality_increases_by_3_5_days_before() -> None:
    """Backstage pass quality increases by 3 where there are <= 5 days left."""
    items = [Item(BACKSTAGE_PASS, 5, 0)]
    update_quality(items)  # 5 days left
    update_quality(items)
    update_quality(items)
    update_quality(items)
    update_quality(items)  # 1 day left
    assert items[0].quality == 15


def test_backstage_passes_quality_0_after_concert() -> None:
    """Backstage pass quality drops to 0 after the concert."""
    items = [Item(BACKSTAGE_PASS, 0, 50)]
    update_quality(items)
    assert items[0].quality == 0


def test_conjured() -> None:
    """ "Conjured" items degrade in Quality twice as fast as normal items."""
    items = [Item(CONJURED, 1, 6)]
    update_quality(items)
    assert items[0].quality == 4
    update_quality(items)
    assert items[0].quality == 0
