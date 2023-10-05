# Function to execute each story element
def handle_story_element(story_element, question, choice_a, choice_b):
    answer = ""
    print(story_element)
    while answer not in (choice_a, choice_b):
        print(question)
        print("Options:")
        print(f" * {choice_a}")
        print(f" * {choice_b}")
        answer = input("Enter your choice (or QUIT to exit): ").strip().upper()
        if answer == "QUIT":
            exit()
    return answer

# Main/driver function
def main():

    # Sample inputs
    description = "You're walking on campus looking for your intro to CS class."

    # Story Block 1
    story_element1 = (
        "As you walk into class, you notice you're in the wrong building!\n"
        "You exit and see the quad splits, revealing two science buildings.\n"
        "The building on the RIGHT has more people entering.\n"
        "The building on the LEFT is where most computer labs are located."
    )
    question1 = "Do you choose to go RIGHT or LEFT?"
    choice1A = "RIGHT"
    choice1B = "LEFT"

    # Story Block 2A
    story_element2A = "You turned RIGHT. You look for women from your GWC College Loop.\n"
    question2A = "What do you do next?"
    choice2A = "I'll pick the first choice!"
    choice2B = "I'll pick the second choice!"

    # Story Block 2B
    story_element2B = "You turned LEFT. You start to power walk into the building. You break into a run when you catch a glimpse of a friend in the computer lab.\n"
    question2B = "What do you do next?"
    choice2C = "I'll pick the first choice!"
    choice2D = "I'll pick the second choice!"

    print(description)
    current_answer = handle_story_element(
        story_element1,
        question1,
        choice1A,
        choice1B)

    if current_answer == choice1A: # if you chose RIGHT
        current_answer = handle_story_element(
            story_element2A,
            question2A,
            choice2A,
            choice2B
        )
    elif current_answer == choice1B: # else if you chose LEFT
        current_answer = handle_story_element(
            story_element2B,
            question2B,
            choice2C,
            choice2D
        )

# Execute if running this script directly
if __name__ == "__main__":
    main()
