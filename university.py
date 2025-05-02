import random


class University:
    def __init__(self, name):
        self.name = name
        # TODO: Add Additional majors and occupations
        self.university_data = {
            1: {
                "computer science": {
                    "occupations": [
                        "Software Engineer",
                        "QA Tester",
                        "Cloud Engineer",
                        "Cyber Security",
                    ]
                }
            },
            2: {
                "business administration": {
                    "occupations": [
                        "Business Analyst",
                        "Entrepreneur",
                        "Project Manager",
                        "Account Manager",
                    ]
                }
            }
        }

    def generate_random_university(self):
        universities = ["MIT", "IIT", "UIC", "Berkley", "Stanford"]
        return random.choice(universities)

    def full_ride_scholarship(self, person):
        if random.random() < 0.2:
            scholarship = True
            print(
                f"Congratulations {person.name}! You have been awarded with a full ride scholarship!"
            )
            # loan gets wiped
            person.loan = 0
            return True
        return False

    def acceptance_letter(self, person):
        university_name = self.generate_random_university()

        scholarship = self.full_ride_scholarship(person)

        offer_letter = input(
            f"Congratulations {person.name}! You have been accepted into {university_name}! Would you like to accept this offer (y/n)? "
        ).lower()

        if offer_letter == "y":
            if not scholarship:
                person.loan += 20000
                person.money -= 20000
            print(
                f"""
                You are now attending {university_name}. 
                Your loan is: {person.loan}
                Your balance is: {person.money}."""
            )
            return person.loan and person.money
        else:
            if random.random() < 0.5:
                offer_letter
            else:
                # Prompt user again
                pass  # Fixed: added `pass` to handle incomplete block

    def choose_your_major(self, person):
        for key, major_data in self.university_data.items():
            for major in major_data:
                print(f"{key}. {major}")

        major_choice = int(input("Please choose a major: "))
        # .format fills out the curly braces {}
        print(
            "You are now majoring in {}.".format(
                # Convert into a list to get the key
                list(self.university_data[major_choice].keys())[0]
            )
        )
        return major_choice

    def study(self, person):
        print(
            r"""You are now studying for class.
              
     __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\ 
   //                 |                 \\ 
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ 
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                dwb `---`
                """
        )
        person.grades += 10

    def attend_lecture(self, person):
        print(
            r"""
            __ _____ ____ _____ ______ _______ _____ ______ ______ ______ ___
            __]_____]____]_____]______]_______]_____]______]______]______]___]
                        _                       _______  |||"||;;|.||##||=|||
            _                           _     |   *  3| |||-|| =|-||==||+|||
            ____________       _              |       | |||_||__|_||__||_|||
            |`.   --__     `.        _______    |       | ||================||
            |  `._____________`.  .'|.-----.|   _ ======| ||| | -|&|^^|!!|-|||
            |   | .-----------.| |  ||     ||  (o))   _ | ||| |**|=|+-|##|=|||
            |   | |  .-------.|| |  ||     ||  /||   / \`._|  .-.|_|__|__|_|||
            |   | |  |       |||_`..|'_____'| //||___\_/.'\| (( ))==========||
            |   | |`.|  ==== ||| | `---------(o)||         \  /-'-=|+|.-|-'|||
            |`. | |`.|_______|||/|______________||__.--._ (o)/|=|;:|-|&&|&&|||
            |  `|_|===========||_|                 (____)-.'(o)_|__|_|__|__|||
            |   | |  .-------.||                           `._\=============||
            |   | |  |       |||                             `.     |       ||
            |   | |`.|  ==== |||`._____________________________`.  o|o      ||
            |`. | |`.|_______||| |._.----------------.__.-------.|__|_______||
            |  `|_|===========|| || '----------------'  | .---. ||  __
            |   | |  .-------.|| ||               |     |_______||.'\.'.
            |   | |  |       ||| || ______________|     | .---. ||'.__.'
            |   | |`.|  ==== ||| ||                `.   |_______|||  _ |
            `. | |`.|_______||| ||                  `. | .---. |||_  ||
            `|_|========LGB||`||                    `|_______|||____|
                                `.                    `.
                                    `.____________________`."""
        )
        person.grades += 50

    def skip_lecture(self, person):
        self.grades -= 20

    # TODO: If the grade starts at 0 no grades should be available
    def grade_scale(self, person):
        if person.grades == 0:
            print("You just started classes.")
            letter_grade = "No grades available."
        elif person.grades >= 90:
            letter_grade = "A+"
        elif person.grades >= 80 and person.grades < 90:
            letter_grade = "B+"
        elif person.grades >= 70 and person.grades < 80:
            letter_grade = "C+"
        elif person.grades >= 60 and person.grades < 70:
            letter_grade = "D"
        elif person.grades < 60:
            letter_grade = "F"
            print(f"You are failing this course.")

        print(f"{letter_grade}")
        return letter_grade

    def university_next_steps(self, person):
        next_steps = {
            1: {"study"},
            2: {"attend lecture"},
            3: {"skip class"},
            4: {"go home"},
        }
        for key, option in next_steps.items():
            print(f"{key}. {", ".join(option)}")

    def attend_classes(self, person):
        count = 0

        while count < 10:
            next_steps_prompt = int(input("What do you want to do (1-4)? "))

            if next_steps_prompt == 1:
                self.study(person)
                self.grade_scale(person)
            elif next_steps_prompt == 2:
                self.attend_lecture(person)
                self.grade_scale(person)
            elif next_steps_prompt == 3:
                self.skip_lecture(person)
            elif next_steps_prompt == 4:
                # go home
                break
            count += 1

    # TODO: Allow user to change majors
    # def change_majors(self):
    #     pass

    def attend_university(self, person):
        self.acceptance_letter(person)
        self.choose_your_major(person)
        self.university_next_steps(person)
        self.attend_classes(person)
