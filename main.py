from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_a_card(hand):
    return hand.append(random.choice(cards))

def calc_score(hand):
    score = sum(hand)
    num_of_A = hand.count(11)
    while score > 21 and num_of_A > 0:
        score -= 10
        num_of_A -= 1
    return score

def black_jack():
    print(logo)
    player_hand = []
    computer_hand = []

    for _ in range(2):
        draw_a_card(player_hand)
        draw_a_card(computer_hand)

    player_score = calc_score(player_hand)
    computer_score = calc_score(computer_hand)

    print(f"Your hand is: \n"
          f"{player_hand} ({player_score})")

    if player_score == 21:
        if computer_score == 21:
            print(f"Dealer's hand is:\n"
                  f"{computer_hand}"
                  f"It's a stand off!")
            return
        else:
            print("Black Jack! You win!")
            return
    else:
        if computer_score == 21:
            print(f"Dealer's hand is:\n"
                  f"{computer_hand}"
                  "Dealer Black Jack! You lose!")
            return

    print(f"Dealer's hand is:\n"
          f"[{computer_hand[0]}, ?]")

    hit = True
    decision = input("Do you want to draw a card? (y/n): ")

    if decision == 'n':
        hit = False

    while hit:
        draw_a_card(player_hand)
        player_score = calc_score(player_hand)
        if player_score > 21:
            print(f"Your hand is {player_hand} ({player_score}). You bust!")
            return
        decision = input(f"Your hand is:\n"
                         f"{player_hand} ({player_score})\n"
                         f"Do you want to draw a card? (y/n): ")
        if decision == 'n':
            hit = False

    while computer_score <= 16:
        draw_a_card(computer_hand)
        computer_score = calc_score(computer_hand)

    if computer_score > 21:
        print(f"Dealer hand is {computer_hand} ({computer_score}). "
              f"Dealer goes bust! You win!")
        return
    elif player_score > computer_score:
        print(f"{player_hand} ({player_score}) vs "
              f"{computer_hand} ({computer_score}). You win!")
        return
    elif player_score < computer_score:
        print(f"{player_hand} ({player_score}) vs "
              f"{computer_hand} ({computer_score}). You lose!")
        return
    else:
        print(f"{player_hand} ({player_score}) vs "
              f"{computer_hand} ({computer_score}). It's a draw!")
        return

keep_playing = True
while keep_playing:
    print("\n"*5)
    black_jack()
    continue_decision = input("Do you want to play another round? (y/n):")
    if continue_decision == 'n':
        keep_playing = False




