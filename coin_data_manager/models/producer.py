from datetime import datetime
from typing import Optional

from coin_data_manager.util import CandleUnit


class Producer:
    def __init__(self, market, unit: CandleUnit, heartbeat: Optional[datetime] = None, order: Optional[str] = None):
        self.market = market
        self.unit = unit
        self.heartbeat = heartbeat
        self.order = order
