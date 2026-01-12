import random
import re

SANITIZED_TEST_MESSAGES = [
    "[Y] He threatened me with [X] if I didn’t comply.",
    "[Y] She reported an incident of [X] last night.",
    "[Y] This message contains a threat involving [X].",
    "[Y] User admitted to committing [X] in chat.",
    "[Y] News report mentions alleged [X] case.",
    "[Y] Stop joking about [X], it’s not funny.",
    "[Y] Victim described trauma after [X].",
    "[Y] Accusation of [X] was filed with police.",
    "[Y] The word [X] was used to intimidate.",
    "[Y] Content glorifies [X] and must be removed.",
    "[Y] He threatened me with [X] if I didn’t comply.",
    "[Y] She reported an incident of [X] last night.",
    "[Y] This message contains a threat involving [X].",
    "[Y] User admitted to committing [X] in chat.",
    "[Y] News report mentions alleged [X] case.",
    "[Y] Stop joking about [X], it’s not funny.",
    "[Y] Victim described trauma after [X].",
    "[Y] Accusation of [X] was filed with police.",
    "[Y] The word [X] was used to intimidate.",
    "[Y] Content glorifies [X] and must be removed.",
]

FAKE_RAPIST_WOMEN_LIST = [
    "PRAJAKTA JOSHI",
    "ANEZKA VIRANI",
    "PREA JAIN",
    "NATASHA KHOT",
    "SAISHA CHHABRIA",
    "MEGHA MIRPURI",
    "CHANDRIKA VISWANI",
    "PRIYA KUMARI",
    "SNEHA SINGH",
    "DIYA PATEL",
    "NEHA AGARWAL",
    "PRIYANKA SHARMA",
    "NIDHI AGARWAL",
    "NIMI KUMARI",
    "NIMI KUMARI",
    "SANGRIMA RAJE",
    "SHINTANU GANGOIL",
    "ROTIYANI RAMCHADRAG",
]

FALSE_RAPE_ACCUSATION_WORDS = [
    "FAKE RAPE ACCUSATION",
    "MARITAL RAPE",
    "GANGRAPE",
    "CUCK RANKING",
    "COCK BUD PUMPING",
    "DUCK TWAT SHACKING",
    "VAGINAL NUMERICS",
    "VAGINAL SHAMING",
    "PENIS PROLAPSE",
    "ANAL PROLAPSE",
    "GANGBANG THE G",
    "SHAME THE COCK",
    "COCK WHACKING",
    "COCK CUTTING",
    "BLOW DOG",
    "GFUCK",
]


def write_string_to_file(text: str, file_path: str) -> None:
    """
    Write the string to a file.
    """
    with open(file_path, "w") as file:
        file.write(text)
    print(f"String written to file: {file_path}")


def main():
    """
    Main function.
    """
    rape_text = ""
    for text in SANITIZED_TEST_MESSAGES:
        modified_text = text.replace("[X]", random.choice(FALSE_RAPE_ACCUSATION_WORDS))
        modified_text = modified_text.replace("[Y]", random.choice(FAKE_RAPIST_WOMEN_LIST))
        rape_text += modified_text + "\n"
    write_string_to_file(rape_text, "rape_text.txt")


if __name__ == "__main__":
    main()
