import unittest

from book import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Wiedźmin", "AS", 2000)

    def test_get_info(self):
            text_correct = "Książka: Wiedźmin Autor: AS Rok: 2000"
            text_result = self.book.get_info()
            self.assertEqual(text_result, text_correct)

    def test_change_title(self):
        self.book.change_title("Miecz Przeznaczenia")
        self.assertEqual("Miecz Przeznaczenia", self.book.title)

    def test_change_author(self):
        self.book.change_author("Brecht")
        self.assertEqual("Brecht", self.book.author)

    def test_change_year(self):
        self.book.change_year(2005)
        self.assertEqual(2005, self.book.year)



if __name__ == '__main__':
    unittest.main()
