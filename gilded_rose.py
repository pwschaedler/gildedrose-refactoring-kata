"""Gilded Rose Refactoring Kata"""

from __future__ import annotations

from typing import Iterable


class GildedRose:
    """Main wrapper class."""

    def __init__(self, items: Iterable[Item]) -> None:
        self.items = items
        """NOTE: Do not change attribute."""

    def update_quality(self) -> None:
        """Update quality for all items at the end of each day."""
        for item in self.items:
            self.update_single_quality_pre_sellin(item)
            self.update_single_sell_in(item)
            self.update_single_quality_post_sellin(item)

    def update_single_quality_pre_sellin(self, item: Item) -> None:
        """Update the quality for a single item before sell-in updates."""
        if (
            item.name != 'Aged Brie'
            and item.name != 'Backstage passes to a TAFKAL80ETC concert'
        ):
            if item.quality > 0:
                if item.name != 'Sulfuras, Hand of Ragnaros':
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == 'Backstage passes to a TAFKAL80ETC concert':
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1

    def update_single_quality_post_sellin(self, item: Item) -> None:
        """Update the quality for a single item after sell-in updates."""
        if item.sell_in < 0:
            if item.name != 'Aged Brie':
                if item.name != 'Backstage passes to a TAFKAL80ETC concert':
                    if item.quality > 0:
                        if item.name != 'Sulfuras, Hand of Ragnaros':
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

    def update_single_sell_in(self, item: Item) -> None:
        """Update the sell-in for a single item."""
        if item.name != 'Sulfuras, Hand of Ragnaros':
            item.sell_in = item.sell_in - 1


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
