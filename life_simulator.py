class Person:
    def __init__(self, name, age, gender, appearance):
        self.name = name
        self.age = age
        self.gender = gender
        self.appearance = appearance

    def create_your_character(self):
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        gender = input("Please enter your gender: ")

        # Display the avatars before the users choose
        self.choose_your_avatar()

        appearance_choice = int(input("Choose your character's appearance (1-4): "))

        # Get the avatar based on the chosen number
        appearance = self.choose_your_avatar(appearance_choice)

        # create a new instance of the Person class
        # return Person(name, age, gender, appearance)

    def choose_your_avatar(self):
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
||               .'  ..=`_         ||
||              / _ ='. )`,        ||
||             | .--:'./`\\ \\     ||
||            .'    .-'   | )      ||
||           / /:';' _   _( |      ||
||          /.' | |  " | "| |      ||
||         (  .|  |   __  ' /      ||
||         |  |/ / \\  `- /( |     ||
||         )_.:./)   `--'._\\ 
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


# class Home:
#     def __init__(self):
#         pass

# class Store:
#     def __init__(self):
#         pass

    