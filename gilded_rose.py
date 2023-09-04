"""Gilded Rose Refactoring Kata"""

from __future__ import annotations

from typing import Callable, Iterable, Protocol

item_handlers: dict[str, type[SupportsUpdate]] = {}


class SupportsUpdate(Protocol):
    """Interface for item updater classes."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""

    def update_sell_in(self, item: Item) -> None:
        """Update the sell-in days for an item."""


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


class DefaultUpdater:
    """Updater for items with default behavior."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        modifier = -1
        if item.sell_in <= 0:
            modifier *= 2
        item.quality = max(0, min(item.quality + modifier, 50))

    def update_sell_in(self, item: Item) -> None:
        """Update the sell-in days for an item."""
        item.sell_in -= 1


def update_quality(items: Iterable[Item]) -> None:
    """Update quality for all items at the end of each day."""
    for item in items:
        updater = item_handlers.get(item.name, DefaultUpdater)()
        updater.update_quality(item)
        updater.update_sell_in(item)


def register_updater(
    label: str,
) -> Callable[[type[SupportsUpdate]], type[SupportsUpdate]]:
    """Register an updater."""

    def wrapper(updater: type[SupportsUpdate]) -> type[SupportsUpdate]:
        item_handlers[label] = updater
        return updater

    return wrapper
