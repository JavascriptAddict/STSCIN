from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EstateFilter(_message.Message):
    __slots__ = ("state", "residenceName", "type", "startTransactionDate", "endTransactionDate", "minPrice", "maxPrice")
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESIDENCENAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STARTTRANSACTIONDATE_FIELD_NUMBER: _ClassVar[int]
    ENDTRANSACTIONDATE_FIELD_NUMBER: _ClassVar[int]
    MINPRICE_FIELD_NUMBER: _ClassVar[int]
    MAXPRICE_FIELD_NUMBER: _ClassVar[int]
    state: str
    residenceName: str
    type: str
    startTransactionDate: str
    endTransactionDate: str
    minPrice: float
    maxPrice: float
    def __init__(self, state: _Optional[str] = ..., residenceName: _Optional[str] = ..., type: _Optional[str] = ..., startTransactionDate: _Optional[str] = ..., endTransactionDate: _Optional[str] = ..., minPrice: _Optional[float] = ..., maxPrice: _Optional[float] = ...) -> None: ...

class EstateData(_message.Message):
    __slots__ = ("state", "area", "type", "transactionDate", "price", "estateId", "residenceName")
    STATE_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONDATE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    ESTATEID_FIELD_NUMBER: _ClassVar[int]
    RESIDENCENAME_FIELD_NUMBER: _ClassVar[int]
    state: str
    area: str
    type: str
    transactionDate: str
    price: float
    estateId: str
    residenceName: str
    def __init__(self, state: _Optional[str] = ..., area: _Optional[str] = ..., type: _Optional[str] = ..., transactionDate: _Optional[str] = ..., price: _Optional[float] = ..., estateId: _Optional[str] = ..., residenceName: _Optional[str] = ...) -> None: ...

class EstateList(_message.Message):
    __slots__ = ("estates",)
    ESTATES_FIELD_NUMBER: _ClassVar[int]
    estates: _containers.RepeatedCompositeFieldContainer[EstateData]
    def __init__(self, estates: _Optional[_Iterable[_Union[EstateData, _Mapping]]] = ...) -> None: ...
