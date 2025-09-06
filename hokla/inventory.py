class Inventory(object):

    def __init__(self, drugs):
        self.drugs = drugs

    def update_efficiency(self):
        """
        Updates the efficiency of every drug in the inventory
        """
        for drug in self.drugs:
            drug.update_efficiency()
