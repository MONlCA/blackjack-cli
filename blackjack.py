import random

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
VALUES = {str(n): n for n in range(2, 11)}
VALUES.update({"J": 10, "Q": 10, "K": 10, "A": 11})
STARTING_CHIPS = 100


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


def get_bet(chips):
    while True:
        value = input(f"\nYou have {chips:g} chips. Bet: ").strip()
        try:
            bet = int(value)
        except ValueError:
            print("Enter a whole number.")
            continue
        if bet < 1:
            print("Bet at least 1 chip.")
        elif bet > chips:
            print("You don't have that many chips.")
        else:
            return bet


def play_round(stats, chips):
    bet = get_bet(chips)
    deck = make_deck()
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]

    print("\n" + "=" * 42)
    print(f"BLACKJACK  •  BET {bet}")
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
            return chips
        if player_blackjack:
            winnings = bet * 1.5
            print(f"\nBlackjack! You win {winnings:g} chips.")
            stats["wins"] += 1
            return chips + winnings
        print(f"\nDealer has blackjack. You lose {bet} chips.")
        stats["losses"] += 1
        return chips - bet

    while True:
        choice = input("\n[H]it or [S]tand? ").strip().lower()
        if choice in {"h", "hit"}:
            player.append(deck.pop())
            show_hand("You   ", player)
            if hand_value(player) > 21:
                print(f"\nBust. You lose {bet} chips.")
                stats["losses"] += 1
                return chips - bet
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
    if dealer_total > 21 or player_total > dealer_total:
        print(f"\nYou win {bet} chips!")
        stats["wins"] += 1
        return chips + bet
    if player_total < dealer_total:
        print(f"\nDealer wins. You lose {bet} chips.")
        stats["losses"] += 1
        return chips - bet

    print(f"\nPush at {player_total}. Your bet is returned.")
    stats["pushes"] += 1
    return chips


def main():
    stats = {"wins": 0, "losses": 0, "pushes": 0}
    chips = STARTING_CHIPS

    print("Welcome to Terminal Blackjack!")
    print("Dealer stands on 17. Blackjack pays 3:2.")

    while chips > 0:
        chips = play_round(stats, chips)
        print(f"\nBankroll: {chips:g} chips")
        print(f"Record: {stats['wins']}W  {stats['losses']}L  {stats['pushes']}P")
        if chips <= 0:
            print("\nYou're out of chips. Game over.")
            break
        again = input("\nPlay again? [Y/n] ").strip().lower()
        if again in {"n", "no"}:
            print(f"\nYou leave the table with {chips:g} chips. Thanks for playing.")
            break


if __name__ == "__main__":
    main()
