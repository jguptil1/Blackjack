def main(): #controller of a hand of poker
    
    deck_instance = Deck() #creates a deck
    deck_instance.shuffle_deck() #shuffles the deck
    player_instance = Player(name='Player')
    dealer_instance = Player(name='Dealer')


    # creating the first hand for the player and dealer
    for i in range(2):
        dealt_card = deck_instance.deal_card()
        player_instance.add_card(dealt_card)
        dealt_card = deck_instance.deal_card()
        dealer_instance.add_card(dealt_card)

    #Showing the dealers intial face up card
    dealer_hand = dealer_instance.hand
    dealer_value =dealer_instance.calc_hand_value()
    dealer_screen = Screen(name='Dealer', value=dealer_value, hand=dealer_hand)
    dealer_screen.print_screen(show_full_hand=False, show_total=False)

    #Showing the players initial hand
    initial_hand_value = player_instance.calc_hand_value()
    player_hand = player_instance.hand
    player_screen = Screen(name='Player', value= initial_hand_value, hand=player_hand)
    player_screen.print_screen(show_full_hand=True, show_total=True)
    
    #Checking to see if player gets blackjack off of the intial hand

    player_blackjack = False #should stay false unless they get 21 off the rip. 
    if initial_hand_value == 21:
        print('You have blackjack! You win!')
        player_blackjack = True
    else: 
        print(f'Your Initial Hand Value: {initial_hand_value}')


    ### Bulk game logic ###

    ## Player Logic First as they have first move

    ## if hit, add a card and ask again until they bust or stand
    continue_hand = True
    while continue_hand and not(player_blackjack): #will continue the hand as long as it is true and the player hasn't already got blackjack. 
        player_decision = player_instance.hit_or_stand()
        if player_decision.lower() == 'hit':
            # Need to add a card to the hand. 
            print('-'*20)
            print('You have decided to hit')
            player_instance.add_card(deck_instance.deal_card()) #adding new card to player instance
            
            ##The display below needs to be updated
            #display the updated hand.
            print()
            #dealer_instance.show_dealer_card() #old method
            dealer_screen.print_screen(show_full_hand=False, show_total=False)
            
            #need a new screen instance to show the updated hand for the player
            new_hand_value = player_instance.calc_hand_value()
            new_player_hand = player_instance.hand
            player_screen = Screen(name='Player', value= new_hand_value, hand=new_player_hand)
            player_screen.print_screen(show_full_hand=True, show_total=True)

            #if they bust:
            if int(new_hand_value) > 21:
                print('You have busted. End of Hand')
                continue_hand = False
            else: 
                continue
             
        elif player_decision.lower() == 'stand': 
            print()
            print('You have decided to stand')
            print()
            print('Dealers turn...')

        
            print('Revealing the Dealers Full Hand: ')
            dealer_screen.print_screen(show_full_hand=True, show_total=True)

            #I dont think the code below is necessary (will keep commented out for now): 
            # pre_hit_or_stand_deal_val = dealer_instance.calc_hand_value()
            # print(f"Dealer's hand value: {pre_hit_or_stand_deal_val}")

            continue_dealer_hand = True
            while continue_dealer_hand: #Dealer's Turn Logic
                dealer_decision = dealer_instance.hit_or_stand()
                
                if dealer_decision == 'hit':
                    print(f'Dealer has to: {dealer_decision}')
                    
                    #need to add a card to dealer hand
                    new_card = deck_instance.deal_card()
                    dealer_instance.add_card(new_card)

                    #show dealers new hand
                    dealer_hand = dealer_instance.hand
                    dealer_value =dealer_instance.calc_hand_value()
                    dealer_screen = Screen(name='Dealer', value=dealer_value, hand=dealer_hand)
                    dealer_screen.print_screen(show_full_hand=True, show_total=True)

                    deal_hand_val = dealer_instance.calc_hand_value()
                    print(f'Dealer New Hand Value: {deal_hand_val}')
                    print(f'Your Hand Value: {player_instance.calc_hand_value()}')
                    
                    if deal_hand_val == 21:
                        print('Dealer has won.')
                        continue_hand = False
                        break
                    elif deal_hand_val > 21:
                        print('Dealer has busted. You win.')
                        continue_hand = False
                        continue_dealer_hand = False
                else:
                    #dealer has reached at least 17 and we need to determine who won
                    #dealer_hand_val = dealer_instance.calc_hand_value()
                    #print(dealer_hand_val)

                    ## Determine winner by comparison
                    if player_instance.calc_hand_value() > dealer_instance.calc_hand_value():
                        print('You have a better hand.')
                        print('You win!')
                    elif player_instance.calc_hand_value() < dealer_instance.calc_hand_value():
                        print('Dealer has a better hand.')
                        print('Dealer wins.')
                    else:
                        print('Push')

                    continue_hand = False
                    continue_dealer_hand = False
            

main()