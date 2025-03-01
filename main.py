from basic_spaceship import BasicSpaceship
from shield_decorator import ShieldDecorator
from weapon_decorator import WeaponDecorator


def main():
    # 1. Create a basic spaceship
    base_ship = BasicSpaceship()
    print("--- Basic Spaceship ---")
    print("Attack:", base_ship.get_attack())
    print("Defense:", base_ship.get_defense())
    print("Weight:", base_ship.get_weight())
    print("Details:", base_ship.get_details())
    print()

    # 2. Add a standard shield
    shielded_ship = ShieldDecorator(base_ship)
    print("--- After Adding Shield ---")
    print("Attack:", shielded_ship.get_attack())
    print("Defense:", shielded_ship.get_defense())  # base + 10
    print("Weight:", shielded_ship.get_weight())  # base + 20
    print("Details:", shielded_ship.get_details())
    print()

    # 3. Add a laser weapon
    armed_ship = WeaponDecorator(shielded_ship)
    print("--- After Adding Weapon ---")
    print("Attack:", armed_ship.get_attack())  # base + 15
    print("Defense:", armed_ship.get_defense())  # base + 10
    print("Weight:", armed_ship.get_weight())  # base + 20 + 15
    print("Details:", armed_ship.get_details())
    print()

    # 4. Add a custom second shield with bigger defense
    big_shield_ship = ShieldDecorator(armed_ship, shield_name="Heavy Shield", extra_defense=20, extra_weight=35)
    print("--- After Adding a Second Shield ---")
    print("Attack:", big_shield_ship.get_attack())  # base + 15
    print("Defense:", big_shield_ship.get_defense())  # base + 10 + 20
    print("Weight:", big_shield_ship.get_weight())  # base + 20 (1st shield) + 15 (weapon) + 35 (2nd shield)
    print("Details:", big_shield_ship.get_details())
    print()


if __name__ == "__main__":
    main()
