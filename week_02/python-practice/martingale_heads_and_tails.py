import random


HEADS = "heads"
TAILS = "tails"
COIN_VALUES = [HEADS, TAILS]


def flip_coin() -> str:
    return random.choice(COIN_VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int:
    if starting_funds <= 0:
        raise ValueError("starting_funds must be > 0")
    if min_bet <= 0:
        raise ValueError("min_bet must be > 0")
    if max_bet < min_bet:
        raise ValueError("max_bet must be >= min_bet")

    steps_to_lose = 0
    current_funds = starting_funds
    current_bet = min(min_bet, current_funds)

    while current_funds > 0:
        steps_to_lose += 1

        # нельзя поставить больше, чем есть
        current_bet = min(current_bet, current_funds)
        current_funds -= current_bet

        flipped_coin_value = flip_coin()

        if flipped_coin_value == HEADS:
            current_funds += current_bet * 2
            current_bet = min_bet
        else:
            next_bet = current_bet * 2

            if next_bet > max_bet:
                next_bet = min_bet

            current_bet = min(next_bet, current_funds)

    return steps_to_lose


def simulate_martingale_runs(
    *,
    starting_funds: int,
    min_bet: int,
    max_bet: int,
    n_games: int,
) -> float:
    if n_games <= 0:
        raise ValueError("n_games must be > 0")

    total_steps_to_lose = 0

    for _ in range(n_games):
        steps_to_lose = play_martingale(
            starting_funds=starting_funds,
            min_bet=min_bet,
            max_bet=max_bet,
        )
        total_steps_to_lose += steps_to_lose

    return total_steps_to_lose / n_games


print(simulate_martingale_runs(
    starting_funds=1000,
    min_bet=1,
    max_bet=100,
    n_games=10,
))