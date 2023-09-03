"""Gilded Rose Refactoring Kata"""

from __future__ import annotations

from typing import Iterable

AGED_BRIE = 'Aged Brie'
SULFURAS = 'Sulfuras, Hand of Ragnaros'
BACKSTAGE_PASS = 'Backstage passes to a TAFKAL80ETC concert'


class GildedRose:
    """Main wrapper class."""

    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items
        """NOTE: Do not change attribute."""

    def update_quality(self) -> None:
        """Update quality for all items at the end of each day."""
        for item in self.items:
            self.update_single_quality(item)
            self.update_single_sell_in(item)

    def update_single_quality(self, item: Item) -> None:
        """Update the quality for a single item before sell-in updates."""
        if item.name == SULFURAS:
            return
        if item.name == BACKSTAGE_PASS and item.sell_in <= 0:
            item.quality = 0
            return

        quality_modifier = -1
        if item.name == AGED_BRIE:
            quality_modifier = 1
        if item.name == BACKSTAGE_PASS and 5 < item.sell_in <= 10:
            quality_modifier = 2
        if item.name == BACKSTAGE_PASS and 0 < item.sell_in <= 5:
            quality_modifier = 3
        if item.sell_in <= 0:
            quality_modifier *= 2

        item.quality = max(0, min(item.quality + quality_modifier, 50))
        return

    def update_single_sell_in(self, item: Item) -> None:
        """Update the sell-in for a single item."""
        if item.name == SULFURAS:
            return
        item.sell_in -= 1


class Item:
    """
    A single inventory item.
    NOTE: Do not change class.
    """

    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        """Item name."""

        self.sell_in = sell_in
        """Number of days left to sell the item."""

        self.quality = quality
        """How valuable the item is."""

    def __repr__(self) -> str:
        return f'{self.name}, {self.sell_in}, {self.quality}'
