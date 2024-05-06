from pydantic import BaseModel, Field, field_validator
from typing import List
import re


class ConverterInput(BaseModel):
    price : float = Field(gt=0)
    to_currencies = List[str]

    @field_validator
    def validate_to_currencies(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'invalid currency {currency}')
        
        return value
