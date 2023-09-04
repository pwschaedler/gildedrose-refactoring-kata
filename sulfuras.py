"""Module for Sulfuras."""

from gilded_rose import DefaultUpdater, Item, register_updater

SULFURAS = 'Sulfuras, Hand of Ragnaros'


@register_updater(SULFURAS)
class SulfurasUpdater(DefaultUpdater):
    """Updater for Sulfuras."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        return

    def update_sell_in(self, item: Item) -> None:
        """Update the sell-in days for an item."""
        return
