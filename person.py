class Person:
    # setting default values so that if someone creates a Person object without providing arguments (grades, loan, balance)
    # the constructor doesn't fail, it just assigns 0 to each.
    def __init__(
        self, name, age, gender, city, appearance, grades=0, loan=0, balance=0
    ):
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city
        self.appearance = appearance
        self.grades = grades
        self.loan = loan
        self.balance = balance

    def create_your_character(self):
        name = input("Please enter your name: ").capitalize()

        while True:
            try:
                age = int(input("Please enter your age: "))

                if isinstance(age, int):
                    break
            except ValueError:
                print("Please enter a number.")

        # TODO: These two are redundant; make DRY
        while True:
            gender = input("Please enter your gender: ").capitalize()

            # Error handling to check if gender is an alphabetical value
            if gender.isalpha():
                break
            else:
                print("Please enter a alphabetical value.")

        while True:
            city = input("Please enter a city: ").title()

            if city.isalpha():
                break
            else:
                print("Please enter a alphabetical value.")

        # Display the avatars before the user chooses
        self.choose_your_avatar()

        while True:
            try:

                appearance_choice = int(
                    input("Choose your character's appearance (1-4): ")
                )

                # Get the avatar based on the chosen number
                appearance = self.choose_your_avatar(appearance_choice)

                # return the new instance of the Person class
                return Person(name, age, gender, city, appearance)
            except ValueError:
                print("Please enter a number between 1-4.")

    # Set appearance_choice parameter to none to display the avatars before a user chooses a number
    def choose_your_avatar(self, appearance_choice=None):
        avatars = {
            1: """
              .-""-.
             /-.{}  \\
             | _\\__.|
             \\/^)^ \\/
              \\ =  /
         .---./`--`\\.--._
        /     `;--'`     \\
       ;        /`       ;
       |       |*        |
      /   |   |     |    \\
      |    \\  |*    /    |
      \\_   |\\_|____/|  __/
                              
                              
                              
                              
    """,
            2: """
             ////^\\\\
            | ^   ^ |
           @ (o) (o) @
            |   <   |
            |  ___  |
             \\_____/
           ____|  |____
          /    \\__/    \\
         /              \\
        /\\_/|        |\\_/\\
       / /  |        |  \\ \\
      ( <   |        |   > )
                              
                              
                              
    """,
            3: """
                 _.._           
               .'  ..=`_         
              / _ ='. )`,        
             | .--:'./`\\ \\     
            .'    .-'   | )      
           / /:';' _   _( |      
          /.' | |  " | "| |      
         (  .|  |   __  ' /      
         |  |/ / \\  `- /( |     
         )_.:./)   `--'._\\ 
                              
                              
                              
                              
                              
    """,
            4: """
            .------.                                     
          .'  .-.    `.                                   
        .'  .'  ; `.   \\                                  
       /   /    :   \\   \\                                 
      /   /-.___;\\   ;   ;                                
     /   :;--.  .-^-.:   :                                
    :    ;:`   :   :                                    
    ;   : ;  O   O   ;   ;                                
    :   ; :    +     /  .'                                 
     \\  ;  \\  --' .:s-"                                   
      "-:.-"`.__.-";                                      
             :     :                                      
             ;     :                                      
      _..+-""._    _"t-.._                                
   .-"    \\    "  '  :    `.                              
  /        `-.______.'      \\  
                              
    """,
        }

        # If user chooses an appearance return the avatar
        if appearance_choice is not None:
            avatar = avatars.get(appearance_choice, "Invalid choice!")
            print(avatar)
            return avatar

        for key, avatar in avatars.items():
            print(f"{key}. {avatar}")


def create_player():
    # Initialize a "blank" person to call create_your_character on
    person = Person(
        "",
        0,
        "",
        "",
        "",
    )

    # Create the character
    return person.create_your_character()
