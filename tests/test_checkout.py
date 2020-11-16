from novicap_checkout.checkout import Checkout


def test_checkout():
    checkout = Checkout('products.json')
    assert checkout.scan('VOUCHER', 'TSHIRT', 'MUG') == 32.5
    assert checkout.scan('VOUCHER', 'TSHIRT', 'VOUCHER') == 25.0
    assert checkout.scan('TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT') == 81.0
    assert checkout.scan('VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'MUG', 'TSHIRT', 'TSHIRT') == 74.5
