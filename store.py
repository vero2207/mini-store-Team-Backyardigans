"""Mini Store starter code for the Git/GitHub workflow exercise."""


def shipping_cost(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must be >= 0")
    return 99.0


def apply_discount(subtotal, percent):
    if percent < 0:
        raise ValueError("percent must be >= 0")
    if percent > 100:
        raise ValueError("percent must be <= 100")
    return round(subtotal * (1 - percent / 100), 2)

        #Me gusto, siento que aporta bastante a los requerimientos de la practica. Solo que yo cambiaria el texto a algo mas claro y con mayusculas al principio. Como "Percent must be...". Atte. Vero :)


def can_checkout(item_count):
    return 1 <= item_count <= 50


def loyalty_discount(points):
    if points < 0:
        raise ValueError("points must be >= 0")
    return 0

