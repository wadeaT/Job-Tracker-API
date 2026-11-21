"""
Schemas describe the JSON going in and out of the API (requests and responses)
"""
from pydantic import BaseModel, Field, field_validator, EmailStr, ConfigDict
# Pydantic Help us to check the data against the type hints and convert it into python objects, if something wrong it raises a ValidationError
# BaseModel is the class that we will inhert from so our class gets all of Pydantic behaviour (validation and convertion of the data)
# Field is used to add extra rules for a single field (or description\examples which appears in /docs)
# field_validator: a decorator that attaches our own function to a field; it runs after
#   the type check, and whatever the function RETURNS becomes the field's value
#   (raising ValueError rejects the value instead)


# response 
# contains id and email
class UserOut(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

# request to register - the client sends the real password, once
# contains email, password
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("email")
    @classmethod
    def convert_to_lowercase(cls, value: str) -> str:
        return value.lower()
