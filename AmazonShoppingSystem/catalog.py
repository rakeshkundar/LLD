from __future__ import annotations


class Search:
    def search_product_by_name(self, name):
        pass

    def search_product_by_category(self, category):
        pass


class Catalog(Search):

    def __init__(self):
        self.product_names = {}
        self.product_categories = {}
    
    def search_products_by_name(self, name):
        return self.product_names.get(name)
    
    def search_products_by_category(self, category):
        return self.product_categories.get(category)
