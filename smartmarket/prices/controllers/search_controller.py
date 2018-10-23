from prices.models import Price


class SearchController:
    def __init__(self, word):
        self.word = word

    def search_in_shops(self):
        price = Price.objects.filter(store__brand_shop__brand_shop=self.word)
        print(price)
        return price.last().product
