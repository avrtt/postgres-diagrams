from typing import NamedTuple

from postgres-diagrams.column import Column


class ColEdge(NamedTuple):
    tail: Column
    head: Column


class TblEdge(NamedTuple):
    tail: str
    head: str
