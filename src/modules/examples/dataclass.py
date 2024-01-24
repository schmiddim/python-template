from __future__ import annotations

from attrs import define, field
from attrs import validators


@define
class User:
    id: int = field(validator=validators.instance_of(int))
    name: str = field(converter=str)
    email: str = field(repr=False)

    @email.default
    def _email_default(self):
        return f"{self.name}@example.com"
