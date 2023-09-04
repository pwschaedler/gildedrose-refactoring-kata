"""Module for conjured inventory items."""

from gilded_rose import DefaultUpdater, Item, register_updater

CONJURED = 'Conjured Item'


@register_updater(CONJURED)
class ConjuredUpdater(DefaultUpdater):
    """Updater for conjured items."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        modifier = -2
        if item.sell_in <= 0:
            modifier *= 2
        item.quality = max(0, min(item.quality + modifier, 50))
