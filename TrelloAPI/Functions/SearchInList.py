from trello.board import Board, List, Card


def search_with_name(search_list, name) -> Board or List or Card or bool:
    name = name.lower()
    for element in search_list:
        if element.name.lower() in name.lower() or name in element.name.lower():
            return element
    return False


