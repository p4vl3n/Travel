class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product):
        Catalogue.products.append(product)

    def get_by_letter(self, first_letter):
        requested_products = [prd for prd in Catalogue.products if prd[0] == first_letter]
        return requested_products

    def __repr__(self):
        Catalogue.products.sort()
        result = f"Items in the {self.name} catalogue:\n"
        result += f'\n'.join(sorted(Catalogue.products))
        return result

        # return f"Items in the {self.name} catalogue:\n"+'\n'.join(sorted(Catalogue.products))


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
