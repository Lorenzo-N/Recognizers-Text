from typing import List
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).parent.resolve()))

from recognizers_text import Culture, ModelResult
from recognizers_number import recognize_number, recognize_ordinal, recognize_percentage
from recognizers_number_with_unit import recognize_age, recognize_currency, recognize_dimension, recognize_temperature
from recognizers_date_time import recognize_datetime


def parse_all(user_input: str, culture: str) -> List[List[ModelResult]]:
    return [
        *recognize_number(user_input, culture, fallback_to_default_culture=False),
        *recognize_ordinal(user_input, culture, fallback_to_default_culture=False),
        *recognize_percentage(user_input, culture, fallback_to_default_culture=False),
        *recognize_datetime(user_input, culture, fallback_to_default_culture=False),
        *recognize_age(user_input, culture, fallback_to_default_culture=False),
        *recognize_currency(user_input, culture, fallback_to_default_culture=False),
        *recognize_dimension(user_input, culture, fallback_to_default_culture=False),
        *recognize_temperature(user_input, culture, fallback_to_default_culture=False),
    ]
