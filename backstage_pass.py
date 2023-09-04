"""Module for backstage pass inventory items."""

from gilded_rose import DefaultUpdater, GildedRose, Item

BACKSTAGE_PASS = 'Backstage passes to a TAFKAL80ETC concert'


@GildedRose.register_updater(BACKSTAGE_PASS)
class BackstagePassUpdater(DefaultUpdater):
    """Updater for backstage pass items."""

    def update_quality(self, item: Item) -> None:
        """Update the quality of an item."""
        if item.sell_in <= 0:
            item.quality = 0
            return

        item.quality += 1
        if item.sell_in <= 10:
            item.quality += 1
        if item.sell_in <= 5:
            item.quality += 1
