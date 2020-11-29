from enum import Enum


class ParsableEnum(Enum):
    @classmethod
    def parse(cls, value):
        for m in cls.__members__:
            if m == value:
                return cls[m]
        else:
            raise ValueError(
                f"{value} is not a valid {cls.__name__}"
                + " - "
                + f"must be one of {', '.join(cls.__members__)}."
            )
