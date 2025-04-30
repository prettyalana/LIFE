from person import create_player
import university
import job
import home


def greeting(player):
    print(f"Welcome {player.name} to the game of LIFE")
    instruction_prompt = input("Would you like to see the instructions (y/n)? ").lower()

    if instruction_prompt == "y":
        instructions()


def instructions():
    # TODO: Add game instructions
    print("To play the game of life: ")


def what_to_do_with_life():
    return input("What do you want to do with your life (1-5)? ")


def life_choices():
    choices = {
        1: "Go to university.",
        2: "Become a streamer",
        3: "Take a gap year",
        4: "Work at your local cafe",
        5: "Invest in stocks and web3",
    }

    for key, choice in choices.items():
        print(f"{key}. {choice}")


def make_life_decision():
    life_choices()
    decision = int(what_to_do_with_life())
    return decision


def life_choice_outcome(decision):
    if decision == 1:
        university()
    elif decision == 2:
        job()
    elif decision == 3:
        home()
    elif decision == 4:
        job()
    elif decision == 5:
        job()


def story(player):
    print(
        f"Hi {player.name}! Your journey begins in the city of {player.city}. Let's start a new LIFE!"
    )
    if player.age > 18:
        time_travel = input(
            f"You are currently {player.age} years old. Would you like to time travel back to 18 years old (y/n)? "
        ).lower()
        if time_travel == "y":
            player.age = 18
            print(
                f"You have traveled back in time. You are now {player.age} years old."
            )
    else:
        pass


def main():
    player = create_player()
    greeting(player)
    story(player)

    if player.age == 18:
        decision = make_life_decision()
        life_choice_outcome(decision)


if __name__ == "__main__":
    main()
