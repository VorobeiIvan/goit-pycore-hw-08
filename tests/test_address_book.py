import unittest
from datetime import datetime, timedelta

# Імпортуємо класи з основного файлу
from src.classes import AddressBook, Record, Birthday, Phone

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()

        # Додаємо тестові дані
        self.record1 = Record("John Doe")
        self.record1.add_phone("1234567890")
        self.record1.add_birthday(Birthday("25.12.1990"))

        self.record2 = Record("Jane Smith")
        self.record2.add_phone("0987654321")
        self.record2.add_birthday(Birthday("01.01.1995"))

        self.address_book.add_record(self.record1)
        self.address_book.add_record(self.record2)

    def test_add_record(self):
        record3 = Record("Bob Johnson")
        record3.add_phone("1112223333")
        self.address_book.add_record(record3)
        self.assertIn("Bob Johnson", self.address_book.data)

    def test_find_record(self):
        result = self.address_book.find("John Doe")
        self.assertEqual(result, self.record1)

    def test_delete_record(self):
        self.address_book.delete("Jane Smith")
        self.assertNotIn("Jane Smith", self.address_book.data)

    def test_add_phone(self):
        self.record1.add_phone("2223334444")
        self.assertEqual(len(self.record1.phones), 2)
        self.assertEqual(self.record1.phones[1].value, "2223334444")

    def test_remove_phone(self):
        self.record1.remove_phone("1234567890")
        self.assertEqual(len(self.record1.phones), 0)

    def test_edit_phone(self):
        self.record1.edit_phone("1234567890", "5556667777")
        self.assertEqual(self.record1.phones[0].value, "5556667777")

    def test_find_phone(self):
        phone = self.record1.find_phone("1234567890")
        self.assertIsNotNone(phone)
        self.assertEqual(phone.value, "1234567890")

    def test_get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)

        # Додаємо запис з днем народження протягом наступного тижня
        record3 = Record("Alice Wonderland")
        birthday_date = (today + timedelta(days=3)).strftime("%d.%m.%Y")
        record3.add_birthday(Birthday(birthday_date))
        self.address_book.add_record(record3)

        upcoming = self.address_book.get_upcoming_birthdays()
        self.assertIn(record3, upcoming)
        self.assertNotIn(self.record1, upcoming)  # День народження не в наступному тижні

if __name__ == "__main__":
    unittest.main()
