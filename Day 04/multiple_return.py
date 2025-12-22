def ready_tea(cups):
    if cups == 0:
        return "No tea needed"
    return f"Preparing {cups} cup(s) of tea"
ready = ready_tea(3)
print(ready)
print(ready_tea(0))


def prepare_snack():
    return 10, 20;

snack, eats = prepare_snack()
print(f"Snack calories: {snack}, Eaten calories: {eats}")