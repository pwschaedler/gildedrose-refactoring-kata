"""Gilded rose tests."""

from gilded_rose import GildedRose, Item


def test_foo() -> None:
    """Placeholder test."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name
