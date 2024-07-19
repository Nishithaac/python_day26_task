"""
HomepageLocators.py
Program: File containing Locators for IMDB search
"""


class Locators:
    # Locator for the 'Name' option in the search accordion
    name_option="//label[@for='accordion-item-nameTextAccordion']"

    # Locator for the input field under the 'Name' option
    name_input="//input[@data-testid='test-nametext']"

    # Locator for the 'Birth Date' option in the search accordion
    birth_option="//label[@for='accordion-item-birthDateAccordion']"

    # Locator for the start year input field under the 'Birth Date' option
    birth_input1="//input[@data-testid='birthYearMonth-start']"

    # Locator for the end year input field under the 'Birth Date' option
    birth_input2="//input[@data-testid='birthYearMonth-end']"


    # Locator for the 'Birthday' option in the search accordion
    birthday="//label[@for='accordion-item-birthdayAccordion']"

    # Locator for the birthday input field under the 'Birthday' option
    birthday_input="//input[@data-testid='birthday-input-test-id']"

    # Locator for the 'Awards' option in the search accordion
    awards_option="//label[@for='accordion-item-awardsAccordion']"

    # Locator for the button to select the 'Oscar Best Actress Winners' award group
    awards_input="//button[@data-testid='test-chip-id-oscar_best_actress_winners']"

    # Locator for the button to initiate the search
    search_box="//button[@data-testid='adv-search-get-results']"

    # Locator for the search results section
    search_results="//div[@class='sc-77f37b3d-0 fsyPsS dli-parent']"