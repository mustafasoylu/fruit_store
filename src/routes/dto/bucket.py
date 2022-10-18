from dataclasses import dataclass, field


@dataclass(frozen=True)
class PostRequest:
    fruits: dict = field(default_factory=dict)


@dataclass
class GetResponse:
    fruits: dict = field(default_factory=dict)
    timestamp: float = None
