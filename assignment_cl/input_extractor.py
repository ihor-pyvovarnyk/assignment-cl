from abc import ABC, abstractmethod
from typing import Iterator


class BaseInputExtractor(ABC):
    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        yield


class TxtInputExtractor(BaseInputExtractor):
    def __init__(self, input_file: str):
        self.input_file = input_file

    def __iter__(self) -> Iterator[str]:
        with open(self.input_file, "r") as f:
            for line in f.read().split("\n"):
                if line and not line.startswith("#"):
                    yield line
