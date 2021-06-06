import wikipedia
MENU_MESSAGE = "Welcome to the Wikipedia console!\nS)earch\nP)age\n>>> "
SEARCH_MESSAGE = "What would you like to search for?\n>>> "
PAGE_MESSAGE = "What page would you like to view? (I'm feelin' lucky)\n>>> "
INPUT_MESSAGE = "Invalid input"
PAGE_EXIST_MESSAGE = "That page does not exist"
DISAMBIGUATION_MESSAGE = "There are multiple results for that page, please be more specific"

def main():
    """
    Wikipedia Console Search Tool
    :return:
    """
    menu_selection = input(MENU_MESSAGE).lower()
    while menu_selection != '':
        if menu_selection == 's':
            search_term = input(SEARCH_MESSAGE)
            search_results = wikipedia.search(search_term)
            print("{} results (max 10) for {}".format(len(search_results), search_term))
            for i, results in enumerate(search_results):
                print("{}. {}".format(i+1, search_results[i]))
        elif menu_selection == 'p':
            try:
                page_selection = input(PAGE_MESSAGE)
                while not page_selection:
                    print(INPUT_MESSAGE)
                    page_selection = input(PAGE_MESSAGE)
                page = wikipedia.page(page_selection, auto_suggest=False)
                print(page.title)
                print(page.summary)
                print(page.url)
            except wikipedia.exceptions.PageError:
                print(PAGE_EXIST_MESSAGE)
            except wikipedia.exceptions.DisambiguationError:
                print(DISAMBIGUATION_MESSAGE)
        else:
            print(INPUT_MESSAGE)
        menu_selection = input(MENU_MESSAGE).lower()


main()
