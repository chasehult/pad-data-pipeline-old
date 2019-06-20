from pad.db.sql_item import SimpleSqlItem


class Awakening(SimpleSqlItem):
    """Monster awakening."""
    TABLE = 'awakening'
    KEY_COL = 'awakening_id'

    @staticmethod
    def from_json(o):
        return Awakening(awakening_id=o['pad_awakening_id'],
                         name_jp=o['name_jp'],
                         name_na=o['name_na'],
                         name_kr=o['name_kr'],
                         desc_jp=o['desc_jp'],
                         desc_na=o['desc_na'],
                         desc_kr=o['desc_kr'],
                         adj_hp=o['adj_hp'],
                         adj_atk=o['adj_atk'],
                         adj_rcv=o['adj_rcv'])

    def __init__(self,
                 awakening_id: int = None,
                 name_jp='',
                 name_na: str = '',
                 name_kr: str = '',
                 desc_jp: str = '',
                 desc_na: str = '',
                 desc_kr: str = '',
                 adj_hp: int = 0,
                 adj_atk: int = 0,
                 adj_rcv: int = 0,
                 tstamp: int = None):
        self.awakening_id = awakening_id
        self.name_jp = name_jp
        self.name_na = name_na
        self.name_kr = name_kr
        self.desc_jp = desc_jp
        self.desc_na = desc_na
        self.desc_kr = desc_kr
        self.adj_hp = adj_hp
        self.adj_atk = adj_atk
        self.adj_rcv = adj_rcv
        self.tstamp = tstamp
