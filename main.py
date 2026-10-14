def greet(name: str = "") -> str:
    """Gibt eine Begruessung zurueck."""
    if name:
        return f"Hello {name}"
    return "Hello"


def add(a: int, b: int) -> int:
    """Addiert zwei Zahlen."""
    return a + b


if __name__ == "__main__":
    print(greet())
