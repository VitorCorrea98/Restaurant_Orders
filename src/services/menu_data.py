# Req 3
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path, mode="r") as file:
            reader = csv.reader(file)
            content = list(reader)
            content.pop(0)
            for name, price, ingredient, quantity in content:
                print(name, price, ingredient, quantity)
