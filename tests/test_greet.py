from greet import greet


def test_greet() -> None:
    assert greet("Monish") == "Hello, Monish!"
