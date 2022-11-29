from trello import TrelloClient
from trello.board import Board, List, Card
from Functions.SearchInList import search_with_name
from constants import *


class Trello():
    def __init__(self):
        self.client = TrelloClient(
            api_key,
            api_secret,
            token)

        self.boards = []
        self.board = None

        self.lists = []
        self.list = None

        self.card = None

        self.fetch_boards()

        self.get_board("ajanda")
        self.get_list(list_name="Halitcan - Kişisel")
        self.get_card("teklif form")

    def fetch_boards(self):
        print("Fetching boards...")
        self.boards = self.client.list_boards()

    def fetch_lists(self):
        if isinstance(self.board, Board):
            print("Fetching Lists")
            self.lists = self.board.list_lists()
        else:
            print("You should get board first with get_board() function.")

    def get_board(self, board_name=None):
        if isinstance(board_name, str):
            print("Getting board " + board_name + " ...")
            board = search_with_name(self.boards, board_name)
            if isinstance(board, Board):
                self.board = board
                self.fetch_lists()
            else:
                print("Cannot find board.")

    def get_list(self, list_name=None):
        if isinstance(list_name, str):
            if len(self.lists) > 0:
                print("Getting list " + list_name + " ...")
                self.list = search_with_name(self.lists, list_name).list_cards()
            else:
                print("You should get board first with get_board() function.")

    def get_card(self, card_name=None):
        if isinstance(card_name, str):
            print("Getting card " + card_name + " ...")
            self.card: Card = search_with_name(self.list, card_name)

trello = Trello()
