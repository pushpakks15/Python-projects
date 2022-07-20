enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies*2 + 1

enemies=increase_enemies()
print(f"enemies outside function: {enemies}")