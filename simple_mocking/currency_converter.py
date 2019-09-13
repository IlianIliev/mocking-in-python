"""
WARNING - this is an educational example and should not be used in production.
Always use Decimal when working with currencies

"""

RATES = {
    ('EUR', 'USD'): 1.11,
    ('USD', 'EUR'): 0.90,
    ('EUR', 'SEK'): 10.67
}


def get_conversion_rate(currency_from, currency_to):

    return RATES[(currency_from, currency_to)]


def currency_converter(amount, currency_from, currency_to):
    conversion_rate = get_conversion_rate(currency_from, currency_to)
    return amount * conversion_rate
