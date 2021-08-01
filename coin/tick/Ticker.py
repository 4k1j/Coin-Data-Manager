class Ticker:
    def __init__(
        self,
        market,
        trade_date,
        trade_time,
        trade_date_kst,
        trade_time_kst,
        trade_timestamp,
        opening_price,
        high_price,
        low_price,
        trade_price,
        prev_closing_price,
        change,
        change_price,
        change_rate,
        signed_change_price,
        signed_change_rate,
        trade_volume,
        acc_trade_price,
        acc_trade_price_24h,
        acc_trade_volume,
        acc_trade_volume_24h,
        highest_52_week_price,
        highest_52_week_date,
        lowest_52_week_price,
        lowest_52_week_date,
        timestamp,
    ):
        """
        :param market	종목 구분 코드
        :param trade_date	최근 거래 일자(UTC)
        :param trade_time	최근 거래 시각(UTC)
        :param trade_date_kst	최근 거래 일자(KST)
        :param trade_time_kst	최근 거래 시각(KST)
        :param opening_price	시가
        :param high_price	고가
        :param low_price	저가
        :param trade_price	종가
        :param prev_closing_price	전일 종가
        :param change	EVEN : 보합, RISE : 상승, FALL : 하락
        :param change_price	변화액의 절대값
        :param change_rate	변화율의 절대값
        :param signed_change_price	부호가 있는 변화액
        :param signed_change_rate	부호가 있는 변화율
        :param trade_volume	가장 최근 거래량
        :param acc_trade_price	누적 거래대금(UTC 0시 기준)
        :param acc_trade_price_24h	24시간 누적 거래대금
        :param acc_trade_volume	누적 거래량(UTC 0시 기준)
        :param acc_trade_volume_24h	24시간 누적 거래량
        :param highest_52_week_price	52주 신고가
        :param highest_52_week_date	52주 신고가 달성일
        :param lowest_52_week_price	52주 신저가
        :param lowest_52_week_date	52주 신저가 달성일
        :param timestamp	타임스탬프
        """
        self.market = market
        self.trade_date = trade_date
        self.trade_time = trade_time
        self.trade_date_kst = trade_date_kst
        self.trade_time_kst = trade_time_kst
        self.trade_timestamp = trade_timestamp
        self.opening_price = opening_price
        self.high_price = high_price
        self.low_price = low_price
        self.trade_price = trade_price
        self.prev_closing_price = prev_closing_price
        self.change = change
        self.change_price = change_price
        self.change_rate = change_rate
        self.signed_change_price = signed_change_price
        self.signed_change_rate = signed_change_rate
        self.trade_volume = trade_volume
        self.acc_trade_price = acc_trade_price
        self.acc_trade_price_24h = acc_trade_price_24h
        self.acc_trade_volume = acc_trade_volume
        self.acc_trade_volume_24h = acc_trade_volume_24h
        self.highest_52_week_price = highest_52_week_price
        self.highest_52_week_date = highest_52_week_date
        self.lowest_52_week_price = lowest_52_week_price
        self.lowest_52_week_date = lowest_52_week_date
        self.timestamp = timestamp

    @staticmethod
    def from_response(response: dict):
        market = response["market"]
        trade_date = response["trade_date"]
        trade_time = response["trade_time"]
        trade_date_kst = response["trade_date_kst"]
        trade_time_kst = response["trade_time_kst"]
        trade_timestamp = response["trade_timestamp"]
        opening_price = response["opening_price"]
        high_price = response["high_price"]
        low_price = response["low_price"]
        trade_price = response["trade_price"]
        prev_closing_price = response["prev_closing_price"]
        change = response["change"]
        change_price = response["change_price"]
        change_rate = response["change_rate"]
        signed_change_price = response["signed_change_price"]
        signed_change_rate = response["signed_change_rate"]
        trade_volume = response["trade_volume"]
        acc_trade_price = response["acc_trade_price"]
        acc_trade_price_24h = response["acc_trade_price_24h"]
        acc_trade_volume = response["acc_trade_volume"]
        acc_trade_volume_24h = response["acc_trade_volume_24h"]
        highest_52_week_price = response["highest_52_week_price"]
        highest_52_week_date = response["highest_52_week_date"]
        lowest_52_week_price = response["lowest_52_week_price"]
        lowest_52_week_date = response["lowest_52_week_date"]
        timestamp = response["timestamp"]

        return Ticker(
            market,
            trade_date,
            trade_time,
            trade_date_kst,
            trade_time_kst,
            trade_timestamp,
            opening_price,
            high_price,
            low_price,
            trade_price,
            prev_closing_price,
            change,
            change_price,
            change_rate,
            signed_change_price,
            signed_change_rate,
            trade_volume,
            acc_trade_price,
            acc_trade_price_24h,
            acc_trade_volume,
            acc_trade_volume_24h,
            highest_52_week_price,
            highest_52_week_date,
            lowest_52_week_price,
            lowest_52_week_date,
            timestamp,
        )
