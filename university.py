import random


class University:
    def __init__(self, name, grades):
        self.name = name
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

    def generate_random_university():
        university = random.choice(universities)

    def acceptance_letter():
        # The player gets an acceptance letter to a random college and they can choose to accept or reject.
        # If they reject the first univeristy, they will receive another letter from a random university.
        # If they reject the second university, there's a 50% chance the user will receive another offer and a 50% chance the user will not get another offer.
        # Should the user not receive another offer they will be prompted again to choose what they want to do.
        # With each offer there's a 20% chance they will receive a full-ride scholarship.
        print("Congratulations ")

    def study():
        pass


universities = ["MIT", "IIT", "UIC", "Berkley"]
