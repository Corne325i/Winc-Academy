# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greet_template="Hello, <name>!"):
    greet_replace = greet_template.replace("<name>", name)

    return greet_replace


def force(
    mass,
    body="earth",
):
    gravity_factor = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }

    gravity_round = round(
        gravity_factor[body], 1
    )  # dit rond de getallen af tot 1 decimaal.
    gravity_force = mass * gravity_round

    return gravity_force


print(force(0.1))

def pull(m1, m2, d):
    G = 6.674 * 10**-11
    pull = G * ((m1 * m2) / d**2)
    return pull

print(pull(0.1, 5.972*10**24, 6.371*10**6))
