"""Module for aged brie inventory items."""

from gilded_rose import DefaultUpdater, Item, register_updater

AGED_BRIE = 'Aged Brie'


@register_updater(AGED_BRIE)
class AgedBrieUpdater(DefaultUpdater):
    """Updater for aged brie items."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        modifier = 1
        if item.sell_in <= 0:
            modifier *= 2
        item.quality = max(0, min(item.quality + modifier, 50))
