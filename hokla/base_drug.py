class BaseDrug:
    """
    Core logic common to every drug, and the default logic
    """

    def __init__(self, name: str, days_until_expiration: int, efficiency_percentage: int) -> None:
        self.name: str = name
        self.days_until_expiration: int = days_until_expiration
        self.efficiency_percentage: int = efficiency_percentage

    @property
    def use_before(self) -> int:
        return self.days_until_expiration

    @use_before.setter
    def use_before(self, days_until_expiration: int) -> None:
                self.days_until_expiration = days_until_expiration

    @property
    def efficiency(self) -> int:
        return self.efficiency_percentage

    @efficiency.setter
    def efficiency(self, efficiency_percentage: int) -> None:
        self.efficiency_percentage = efficiency_percentage

    def __repr__(self):
        return f"{self.name}, {self.days_until_expiration}, {self.efficiency_percentage}"

    def _degrade_efficiency_unexpired(self):
        """
        Degrades the efficiency_percentage corresponding to a day when the drug is unexpired
        """
        self.efficiency_percentage -= 1


    def _update_expiration(self) -> None:
        """
        Updates the number of days until the expiration date
        """
        self.days_until_expiration -= 1

    def update_efficiency_percentage(self) -> None:
        """
        Updates the efficiency_percentage of a self after one more more.
        """
        self._update_expiration()
        self._degrade_efficiency_unexpired()
        if self.days_until_expiration < 0:
            self._degrade_efficiency_unexpired()


