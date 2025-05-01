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
            print(
                f"You are now attending {university_name}. Your loan is: {person.loan}."
            )
            return person.loan
        else:
            if random.random() < 0.5:
                offer_letter
            else:
                # Prompt user again
                pass  # Fixed: added `pass` to handle incomplete block

    def choose_your_major(self, player):
        for key, major_data in self.university_data.items():
            for major in major_data:
                print(f"{key}. {major}")

        major_choice = int(input("Please choose a major: "))
        # .format fills out the curly braces {} 
        print("You are now majoring in {}.".format(
            # Convert into a list to get the key 
            list(self.university_data[major_choice].keys())[0]))
        return major_choice

    def study(self):
        self.grades += 10

    def grade_scale(self, person):
        if person.grades >= 90:
            letter_grade = "A+"
        elif person.grades >= 80 and person.grades < 90:
            letter_grade = "B+"
        elif person.grades >= 70 and person.grades < 80:
            letter_grade = "C+"
        elif person.grades >= 60 and person.grades < 70:
            letter_grade = "D"
        else:
            letter_grade = "F"
            print(f"You have failed this course.")

        print(f"{letter_grade}")
        return letter_grade

    # TODO: Allow user to change majors
    # def change_majors(self):
    #     pass

    def attend_university(self, player):
        self.acceptance_letter(player)
        self.choose_your_major(player)
