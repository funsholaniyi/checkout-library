Code         | Name         |  Price
----------------------------------------
VOUCHER      | Voucher      |   5.00€
TSHIRT       | T-shirt      |  20.00€
MUG          | Coffee mug   |   7.50€


Various departments have suggested some discounts to improve sales:

The marketing department wants a 2-for-1 special on VOUCHER items.

The CFO insists that the best way to increase sales is with (tiny) discounts on bulk purchases. If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.


The checkout process allows for items to be scanned in any order, and calculates the total price. The interface looks like this (in ruby):

checkout = Checkout.new(price_rules)

checkout.scan("VOUCHER")

checkout.scan("VOUCHER")

checkout.scan("TSHIRT")

price = checkout.total

Examples:

Items: VOUCHER, TSHIRT, MUG
Total: 32.50€

Items: VOUCHER, TSHIRT, VOUCHER
Total: 25.00€

Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT
Total: 81.00€

Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, MUG, TSHIRT, TSHIRT
Total: 74.50€


---------------------------------------

Example run,

from novicap_checkout.checkout import Checkout

checkout = Checkout('products.json')

print(checkout.scan('VOUCHER', 'TSHIRT', 'MUG'))