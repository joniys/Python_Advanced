from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: int
    name: str
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Age must be positive")
        return v


try:
    user = User(id=1, name="Gerti", age=16)
except ValueError as e:
    print(e)

class Address(BaseModel):
    street: str
    city: str
