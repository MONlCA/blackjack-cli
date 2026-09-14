import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {str(n): n for n in range(2, 11)}
VALUES.update({"J": 10, "Q": 10, "K": 10, "A": 11})


def make_deck():
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def card_text(card):
    rank, suit = card
    return f"{rank}{suit}"


def hand_value(hand):
    total = sum(VALUES[rank] for rank, _ in hand)
    aces = sum(1 for rank, _ in hand if rank == "A")

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def show_hand(label, hand, hide_first=False):
    if hide_first:
        cards = ["??"] + [card_text(card) for card in hand[1:]]
        print(f"{label}: {'  '.join(cards)}")
    else:
        print(f"{label}: {'  '.join(card_text(card) for card in hand)}  ({hand_value(hand)})")


def play_round(stats):
    deck = make_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    print("\n" + "=" * 42)
    print("BLACKJACK")
    print("=" * 42)

    show_hand("Dealer", dealer, hide_first=True)
    show_hand("You   ", player)

    player_blackjack = hand_value(player) == 21
    dealer_blackjack = hand_value(dealer) == 21

    if player_blackjack or dealer_blackjack:
        show_hand("Dealer", dealer)
        if player_blackjack and dealer_blackjack:
            print("\nPush. Both have blackjack.")
            stats["pushes"] += 1
        elif player_blackjack:
            print("\nBlackjack! You win.")
            stats["wins"] += 1
        else:
            print("\nDealer has blackjack. You lose.")
            stats["losses"] += 1
        return

    while True:
        choice = input("\n[H]it or [S]tand? ").strip().lower()

        if choice in {"h", "hit"}:
            player.append(deck.pop())
            show_hand("You   ", player)

            if hand_value(player) > 21:
                print("\nBust. Dealer wins.")
                stats["losses"] += 1
                return

            if hand_value(player) == 21:
                print("\n21. You stand automatically.")
                break

        elif choice in {"s", "stand"}:
            break
        else:
            print("Please type H or S.")

    print("\nDealer reveals:")
    show_hand("Dealer", dealer)

    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
        print(f"Dealer hits: {card_text(dealer[-1])}")
        show_hand("Dealer", dealer)

    player_total = hand_value(player)
    dealer_total = hand_value(dealer)

    if dealer_total > 21:
        print("\nDealer busts. You win!")
        stats["wins"] += 1
    elif player_total > dealer_total:
        print(f"\nYou win, {player_total} to {dealer_total}!")
        stats["wins"] += 1
    elif player_total < dealer_total:
        print(f"\nDealer wins, {dealer_total} to {player_total}.")
        stats["losses"] += 1
    else:
        print(f"\nPush at {player_total}.")
        stats["pushes"] += 1


def main():
    stats = {"wins": 0, "losses": 0, "pushes": 0}

    print("Welcome to Terminal Blackjack!")
    print("Dealer stands on 17. Blackjack pays bragging rights only.\n")

    while True:
        play_round(stats)
        print(
            f"\nRecord: {stats['wins']}W  {stats['losses']}L  {stats['pushes']}P"
        )

        again = input("\nPlay again? [Y/n] ").strip().lower()
        if again in {"n", "no"}:
            print("\nThanks for playing.")
            break


if __name__ == "__main__":
    main()
