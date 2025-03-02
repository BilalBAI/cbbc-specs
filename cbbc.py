import datetime
import time


class cbbc:
    def __init__(self,
                 type='BULL',
                 underlying='BTC',
                 strike=60000,
                 expiry=168,
                 conversion_ratio=1000,
                 category='N'):
        ###
        self.type = type
        self.underlying = underlying
        self.strike = strike
        self.expiry = expiry
        self.conversion_ratio = conversion_ratio
        self.category = category
        ###
        self.called = False
        self.issurance_timestamp = datetime.datetime.now()
        self.expiry_datetime = self.issurance_timestamp + \
            datetime.timedelta(hours=168)

    def get_ticker(self):
        return f"{self.underlying}-{self.strike}-{self.expiry_datetime.strftime('%Y%m%d%H')}-{self.type}"

    def update_spot_price(self):
        # get underlying spot price from Oracle
        # every hour
        self.spot = None

    def calc_intrinsic_value(self):
        intrinsic_value = self.spot - self.strike
        if intrinsic_value <= 0:
            self.called = True
            return 0
        else:
            return intrinsic_value
