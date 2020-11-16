import json


class Checkout:
    data = []

    def __init__(self, data_path):
        try:
            with open(data_path) as f:
                self.data = json.load(f)
        except FileNotFoundError or FileExistsError:
            print('Error importing JSON data file')
            return

    def scan(self, *product_codes):
        """
        Take in product codes as list of strings, and return total value of products in cart
        :param product_codes:
        :return:
        """
        total = 0
        product_count = {}

        if not self.data:
            print('No product(s) imported')
            return
        for product_code in product_codes:
            product = self._get_product(product_code)
            discount = product['discount']

            if not discount:
                # if no discount, add price and move on :)
                total += product['price']
            else:
                try:
                    product_count[product_code] += 1
                except KeyError:
                    # initialise the product code in the count object, default to 1
                    product_count[product_code] = 1
                count = product_count[product_code]

                if count < discount['min_count']:
                    total += product['price']
                else:
                    total += product['price']
                    discount_amount = Checkout._get_discount(product, product_count)
                    total -= discount_amount
        return total

    def _get_product(self, product_code):
        """
        Find product by using unique product code, else return None
        :param product_code:
        :return:
        """
        product = next((item for item in self.data if item["code"] == product_code), None)
        if not product:
            print('Product was not found')
            return
        return product

    @staticmethod
    def _get_discount(product, product_count):
        """
        Calculate the value of the product, by taking into account the number of time the product is in cart
        :param product:
        :param product_count:
        :return:
        """
        product_code = product['code']
        discount = product['discount']
        count = product_count[product_code]

        if discount['type'] == 'percent':
            # get the percentage decimal and multiple with all applicable products in cart so far
            # reset count to 0 after discount is used
            discount_amount = (discount['value'] / 100) * count * product['price']
            product_count[product_code] = 0
        elif discount['type'] == 'ppu':
            # get the discount value and and multiple with all applicable products in cart so far
            # reset local count to 1 if min threshold is passed to apply the discount to each applicable
            # product moving forward
            count = 1 if count > 3 else count
            discount_amount = discount['value'] * count
        else:
            discount_amount = 0
            pass

        return discount_amount
