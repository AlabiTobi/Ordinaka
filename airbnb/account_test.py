import unittest

from airbnb import account


class AccountTest(unittest.TestCase):
    def test_add(self):
        result = account.add(2, 5)
        self.assertEqual(7, result)

    def test_sub_created(self):
        result = account.sub(7, 4)
        self.assertEqual(3, result)

    def test_that_account_can_be_created(self):
        account1 = account.Account("Eregbesola", 1234, "08160903419")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """
        GIVEN:
        WHEN:
        THEN:
        """
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        name = account1.name
        self.assertEqual("Eregbesola", name)

    def test_that_account_can_deposit(self):
        """
        GIVEN: An account
        WHEN: when a deposit is mode
        THEN: account balance should be reflected
        """
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        account1.deposit(2000)

        self.assertEqual(2000, account1.balance)

    def test_negative_deposit_raises_error(self):
        account1 = account.Account("Stepen", 1234, "08160903419")
        account1.deposit(500)

        self.assertRaises(ValueError, account1.deposit, -1000)

        self.assertEqual(500, account1.balance)

    def test_that_deposit_can_be_created(self):
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        account1.withdraw(1000, 1234)
        self.assertEqual(1000, account1.balance)

    def test_that_deposit_negative_amount(self):
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        self.assertRaises(ValueError, account1.withdraw, -1000, 1234)
        self.assertEqual(2000, account1.balance)

    def test_tha__account_load_airtime(self):
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)
        account1.load_airtime(300, "08160903419")
        self.assertEqual(1700, account1.balance)

    def test_that_create_another_account(self):
        account1 = account.Account("Eregbesola", 1234, "08160903419")
        account2 = account.Account("Adunni", 9121, "07066474899")
        account1.add_to_account()


if __name__ == '__main__':
    unittest.main()
