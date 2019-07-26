# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .MoneroTransactionRsigData import MoneroTransactionRsigData

if __debug__:
    try:
        from typing import Dict, List, Optional
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class MoneroTransactionInitAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 502

    def __init__(
        self,
        hmacs: List[bytes] = None,
        rsig_data: MoneroTransactionRsigData = None,
    ) -> None:
        self.hmacs = hmacs if hmacs is not None else []
        self.rsig_data = rsig_data

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('hmacs', p.BytesType, p.FLAG_REPEATED),
            2: ('rsig_data', MoneroTransactionRsigData, 0),
        }