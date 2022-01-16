from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from coin_data_manager.util import CandleUnit


class Producer:
    def __init__(self, market, unit: CandleUnit, heartbeat: Optional[datetime] = None, order: Optional[str] = None):
        self.market = market
        self.unit = unit
        self.heartbeat = heartbeat
        self.order = order

    def __repr__(self):
        return f"Producer[{self.market}, {self.unit}]"


class ProducerData(BaseModel):
    market: str
    unit: str
