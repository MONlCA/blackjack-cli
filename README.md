# Terminal Blackjack

A simple command-line Blackjack game written in Python.

## Features

- Standard 52-card deck
- Hit / stand gameplay
- Dealer automatically hits below 17
- Correct Ace handling as 1 or 11
- Blackjack, busts, pushes, wins, and losses
- 100-chip starting bankroll with validated bets
- Standard 3:2 payout for a natural blackjack
- Session win/loss/push record
- No external dependencies

## Run it

```bash
python3 blackjack.py
```

## Example

```text
Welcome to Terminal Blackjack!
Dealer stands on 17. Blackjack pays 3:2.

You have 100 chips. Bet: 10

==========================================
BLACKJACK  •  BET 10
==========================================
Dealer: ??  7♣
You   : A♠  9♦  (20)

[H]it or [S]tand? s
```

Winning a normal hand adds the amount of your bet to your bankroll. A natural blackjack pays 3:2, a push returns your bet, and a loss subtracts the wager.

## Ideas for future updates

- Double down
- Split hands
- Persistent player stats
- Multiple-deck shoe
- ASCII card art
- Unit tests for scoring and payouts

## License

MIT
