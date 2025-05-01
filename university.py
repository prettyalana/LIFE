import random


class University:
    def __init__(self, name):
        self.name = name
        # TODO: Add Additional majors and occupations
        self.university_data = {
            "computer science": {
                "occupations": [
                    "Software Engineer",
                    "QA Tester",
                    "Cloud Engineer",
                    "Cyber Security",
                ]
            },
            "business administration": {
                "occupations": [
                    "Business Analyst",
                    "Entrepreneur",
                    "Project Manager",
                    "Account Manager",
                ]
            },
        }

    def generate_random_university(self):
        university = random.choice(universities)
        return university

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
        # The player gets an acceptance letter to a random college and they can choose to accept or reject.
        # If they reject the first univeristy, they will receive another letter from a random university.
        # If they reject the second university, there's a 50% chance the user will receive another offer and a 50% chance the user will not get another offer.
        # Should the user not receive another offer they will be prompted again to choose what they want to do.
        # With each offer there's a 20% chance they will receive a full-ride scholarship

        while True:
            self.full_ride_scholarship(person)
            offer_letter = input(
                "Congratulations {person.name}! You have been accepted into {university}! Would you like to accept this offer (y/n)? "
            ).lower()

            scholarship = self.full_ride_scholarship(person)

            if offer_letter == "y":
                if not scholarship:
                    person.loan += 20000
                print(
                    f"You are now attending {offer_letter.university}. Your loan is {person.loan}."
                )
            else:
                if random.random() < 0.5:
                    offer_letter
                else:
                    pass
                    # TODO: To prevent recursion consider moving this logic to main
                    # Removed the import so this won't work
                    # what_to_do_with_life(person)

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

    # TODO: Allow user to change majors
    # def change_majors(self):
    #     pass


universities = ["MIT", "IIT", "UIC", "Berkley", "Stanford"]
