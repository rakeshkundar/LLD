class ProductCategory:
    name: str
    description: str

    def __init__(self, name: str, desc: str) -> None:
        self.name = name
        self.description = desc

    def get_product_category_name(self):
        return self.name

    def get_product_category_desc(self):
        return self.description