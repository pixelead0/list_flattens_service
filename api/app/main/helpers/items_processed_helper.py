from more_itertools import collapse
from ast import literal_eval
import logging

logger = logging.getLogger(__name__)


class ItemsProcessedHelper(object):
    """Helper for items processed."""

    def flatten(self, input_items):
        try:
            items = literal_eval(input_items)
        except Exception as e:
            items = input_items
            logger.info(e)
        return list(collapse(items))
