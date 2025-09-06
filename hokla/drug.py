from .drugs import InsulinVial, GrannyRecipe, BottleOfWine
from .base_drug import BaseDrug

class Drug:
    """
    Wrapper to keep old API
    """

    def __new__(cls, name: str, days_until_expiration: int, efficiency_percentage: int) -> BaseDrug:
        match name:
            case "Insulin vial":
                return InsulinVial(days_until_expiration, efficiency_percentage)
            case "Granny recipe":
                return GrannyRecipe(days_until_expiration, efficiency_percentage)
            case "Old bottle of wine":
                return BottleOfWine(days_until_expiration, efficiency_percentage)
            case _:
                return BaseDrug(name, days_until_expiration, efficiency_percentage)

