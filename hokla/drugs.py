from .base_drug import BaseDrug


class InsulinVial(BaseDrug):

    def __init__(self, days_until_expiration: int, efficiency_percentage: int) -> None:
        super().__init__("Insulin vial", days_until_expiration, efficiency_percentage)

    def _degrade_efficiency_unexpired(self):
        if self.days_until_expiration <= 0:
            self.efficiency_percentage = 0
        if self.days_until_expiration  <= 7:
            self.efficiency_percentage -= 3
        elif self.days_until_expiration <= 30:
            self.efficiency_percentage -= 2
        else:
            self.efficiency_percentage -= 1


class GrannyRecipe(BaseDrug):

    def __init__(self, days_until_expiration: int, efficiency_percentage: int) -> None:
        super().__init__("Granny recipe", days_until_expiration, efficiency_percentage)

    def _degrade_efficiency_unexpired(self):
        pass

    def _update_expiration(self) -> None:
        pass



class BottleOfWine(BaseDrug):

    def __init__(self, days_until_expiration: int, efficiency_percentage: int) -> None:
        super().__init__("Old bottle of wine", days_until_expiration, efficiency_percentage)


    def _degrade_efficiency_unexpired(self):
        self.efficiency_percentage += 1



class RnaVaccin(BaseDrug):

    def __init__(self, days_until_expiration: int, efficiency_percentage: int) -> None:
        super().__init__("ARN vaccine", days_until_expiration, efficiency_percentage)

    def _degrade_efficiency_unexpired(self):
        self.efficiency_percentage -= 2
