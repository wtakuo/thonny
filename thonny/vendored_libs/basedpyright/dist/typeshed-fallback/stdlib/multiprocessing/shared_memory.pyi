import sys
from collections.abc import Iterable
from typing import Any, Generic, TypeVar, overload
from typing_extensions import Self

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ["SharedMemory", "ShareableList"]

_SLT = TypeVar("_SLT", int, float, bool, str, bytes, None)

class SharedMemory:
    if sys.version_info >= (3, 13):
        def __init__(self, name: str | None = None, create: bool = False, size: int = 0, *, track: bool = True) -> None: ...
    else:
        def __init__(self, name: str | None = None, create: bool = False, size: int = 0) -> None: ...

    @property
    def buf(self) -> memoryview:
        """A memoryview of contents of the shared memory block."""
        ...
    @property
    def name(self) -> str:
        """Unique name that identifies the shared memory block."""
        ...
    @property
    def size(self) -> int:
        """Size in bytes."""
        ...
    def close(self) -> None: ...
    def unlink(self) -> None: ...
    def __del__(self) -> None: ...

class ShareableList(Generic[_SLT]):
    shm: SharedMemory
    @overload
    def __init__(self, sequence: None = None, *, name: str | None = None) -> None: ...
    @overload
    def __init__(self, sequence: Iterable[_SLT], *, name: str | None = None) -> None: ...
    def __getitem__(self, position: int) -> _SLT: ...
    def __setitem__(self, position: int, value: _SLT) -> None: ...
    def __reduce__(self) -> tuple[Self, tuple[_SLT, ...]]: ...
    def __len__(self) -> int: ...
    @property
    def format(self) -> str:
        """The struct packing format used by all currently stored items."""
        ...
    def count(self, value: _SLT) -> int: ...
    def index(self, value: _SLT) -> int: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any, /) -> GenericAlias:
            """
            Represent a PEP 585 generic type

            E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
            """
            ...