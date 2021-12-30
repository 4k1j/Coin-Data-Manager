from datetime import datetime
from typing import Optional


class Producer:
    def __init__(self, market, unit, heartbeat=Optional[datetime], order=Optional[str]):
        self.market = market
        self.unit = unit
        self.heartbeat = heartbeat
        self.order = order
