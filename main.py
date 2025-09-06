# -*- coding: utf-8 -*-

from hokla import Drug, Inventory


class InventoryTest:
    def test_foo(self):
        items = [
            Drug("Normal Drug", 10, 20),
            Drug("Old bottle of wine", 2, 0),
            Drug("Normal Drug 2", 5, 7),
            Drug("Granny recipe", 0, 150),
            Drug("Granny recipe", -1, 80),
            Drug("Insulin vial", 15, 20),
            Drug("Insulin vial", 10, 49),
            Drug("Insulin vial", 5, 49),
            Drug("ARN Vaccine", 3, 6),
        ]

        inventory = Inventory(items)
        inventory.update_efficiency()
        assert items[0].name == "Normal Drug"
        assert items[0].use_before == 9
        assert items[0].efficiency == 19

        assert items[1].name == "Old bottle of wine"
        assert items[1].use_before == 1
        assert items[1].efficiency ==1

        assert items[2].name == "Normal Drug 2"
        assert items[2].use_before == 4
        assert items[2].efficiency == 6

        assert items[3].name == "Granny recipe"
        assert items[3].use_before <= 0
        assert items[3].efficiency == 150

        assert items[4].name == "Granny recipe"
        assert items[4].use_before <= 0
        assert items[4].efficiency == 80

        assert items[5].name == "Insulin vial"
        assert items[5].use_before == 14
        assert items[5].efficiency == 18

        assert items[6].name == "Insulin vial"
        assert items[6].use_before == 9
        assert items[6].efficiency == 47

        assert items[7].name == "Insulin vial"
        assert items[7].use_before == 4
        assert items[7].efficiency == 46

        assert items[8].name == "ARN Vaccine"
        assert items[8].use_before == 2
        assert items[8].efficiency == 5


if __name__ == "__main__":
    test = InventoryTest()
    test.test_foo()
