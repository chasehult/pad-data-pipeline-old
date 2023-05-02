from datetime import timedelta
from typing import Optional

from pad.common.monster_id_mapping import server_monster_id_fn
from pad.common.shared_types import MonsterNo
from pad.db.sql_item import SimpleSqlItem
from pad.raw.exchange import Exchange as ExchangeModel


class Exchange(SimpleSqlItem):
    """Monster exchanges."""
    TABLE = 'exchanges'
    KEY_COL = {'trade_id', 'server_id'}

    @staticmethod
    def from_raw_exchange(e: ExchangeModel):
        id_mapper = server_monster_id_fn(e.server)
        target_monster_id = id_mapper(e.monster_id)
        req_monster_csv_str = ','.join(['({})'.format(id_mapper(idx)) for idx in e.required_monsters])
        permanent = int(timedelta(seconds=(e.end_timestamp - e.start_timestamp)) > timedelta(days=60))
        return Exchange(trade_id=e.trade_id,
                        server_id=e.server.value,
                        target_monster_id=target_monster_id,
                        target_monster_amount=e.monster_amount,
                        required_monster_ids=req_monster_csv_str,
                        required_count=e.required_count,
                        start_timestamp=e.start_timestamp,
                        end_timestamp=e.end_timestamp,
                        permanent=permanent,
                        menu_idx=e.menu_idx,
                        order_idx=e.display_order,
                        flags=e.flag_type)

    def __init__(self,
                 trade_id: int = None,
                 server_id: int = None,
                 target_monster_id: int = None,
                 target_monster_amount: int = None,
                 required_monster_ids: str = None,  # TODO: Remove this
                 required_count: int = None,
                 start_timestamp: int = None,
                 end_timestamp: int = None,
                 permanent: int = None,
                 menu_idx: int = None,
                 order_idx: int = None,
                 flags: int = None,
                 tstamp: int = None):
        self.trade_id = trade_id
        self.server_id = server_id
        self.target_monster_id = target_monster_id
        self.target_monster_amount = target_monster_amount
        self.required_monster_ids = required_monster_ids
        self.required_count = required_count
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.permanent = permanent
        self.menu_idx = menu_idx
        self.order_idx = order_idx
        self.flags = flags
        self.tstamp = tstamp

    def __str__(self):
        return 'Exchange ({}-{}): {} [{}]'.format(self.trade_id, self.server_id, self.target_monster_id,
                                                  self.required_count)


class ExchangeMonster(SimpleSqlItem):
    """Monster exchanges."""
    TABLE = 'exchange_monsters'
    KEY_COL = {'trade_id', 'server_id', 'monster_id'}

    @staticmethod
    def from_raw(e: ExchangeModel, m_id: MonsterNo, amount: int):
        id_mapper = server_monster_id_fn(e.server)
        m_id = id_mapper(m_id)
        return ExchangeMonster(trade_id=e.trade_id,
                               server_id=e.server.value,
                               monster_id=m_id,
                               required_count=amount)

    def __init__(self,
                 trade_id: int,
                 server_id: int,
                 monster_id: int,
                 required_count: Optional[int],
                 tstamp: int = None):
        self.trade_id = trade_id
        self.server_id = server_id
        self.monster_id = monster_id
        self.required_count = required_count
        self.tstamp = tstamp

    def __str__(self):
        return 'ExchangeMonster({}):'.format(self.key_str())
