from drugs import InsulinVial, GrannyRecipe, BottleOfWine
from base_drug import BaseDrug

class Drug:
    """
    Wrapper to keep old API
    """

    def __new__(cls, name: str, days_until_expiration: int, efficiency_percentage: int) -> BaseDrug:
        match name:
            case "Insulin Vial":
                return InsulinVial(days_until_expiration, efficiency_percentage)
            case "Granny Recipe":
                return GrannyRecipe(days_until_expiration, efficiency_percentage)
            case "Old Bottle of Wine":
                return BottleOfWine(days_until_expiration, efficiency_percentage)
            case _:
                return BaseDrug(name, days_until_expiration, efficiency_percentage)

