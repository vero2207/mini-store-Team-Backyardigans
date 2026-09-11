"""Mini Store starter code for the Git/GitHub workflow exercise."""

def shipping_cost(subtotal):
    if subtotal < 0:
        raise ValueError("subtotal must be >= 0")

    if subtotal >= 1000:
        return 0.0

    return 99.0

#Buena función, solo agregaria una prueba para comprobar que exactamente 1000 recibe envio gratis tambien.



def apply_discount(subtotal, percent):
    if subtotal < 0:
        raise ValueError("subtotal must be >= 0")
    return round(subtotal * (1 - percent / 100), 2)


def can_checkout(item_count):
    return item_count > 0


def loyalty_discount(points):
    if points < 0:
        raise ValueError("points must be >= 0")
    return 0
