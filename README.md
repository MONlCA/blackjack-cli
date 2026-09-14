# Terminal Blackjack

A simple command-line Blackjack game written in Python.

## Features

- Standard 52-card deck
- Hit / stand gameplay
- Dealer automatically hits below 17
- Correct Ace handling as 1 or 11
- Blackjack, busts, pushes, wins, and losses
- Session win/loss/push record
- No external dependencies

## Run it

```bash
python3 blackjack.py
```

## Example

```text
Dealer: ??  7♣
You   : A♠  9♦  (20)

[H]it or [S]tand? s

Dealer reveals:
Dealer: 10♥  7♣  (17)

You win, 20 to 17!
```

## Ideas for future updates

- Betting and chip balance
- Double down
- Split hands
- Persistent player stats
- Multiple-deck shoe
- ASCII card art

## License

MIT
