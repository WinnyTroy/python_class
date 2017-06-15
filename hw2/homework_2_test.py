import unittest

from homework_2 import player1_choice_rock

# class player1_choice_rock_test(unittest.TestCase):

#     def test(self):
#         self.assertTrue(True)

#     def player1_choice_rock():
#         self.assertEqual('r', 'You tie Bitch')

moves = ['r', 'p', 's']


class RPSRelationCase(unittest.TestCase):
    def runTest(self):
        """Test the relations between options."""

        self.assertEqual(player1_choice_rock, Paper,
                         "You win Sensei")
        # self.assertEqual(Rock.stronger_than, Scissors,
        #                  "Rock is not stronger than Scissors")
        # self.assertEqual(Paper.weaker_than, Scissors,
        #                  "Paper is not weaker than Scissors!")
        # self.assertEqual(Paper.stronger_than, Rock,
        #                  "Paper is not stronger than Rock")
        # self.assertEqual(Scissors.weaker_than, Rock,
        #                  "Scissors are not weaker than Rock")


# self.assertEqual(Scissors.stronger_than, Paper,
#                  "Scissors are not weaker than Paper")


if __name__ == '__main__':
    unittest.main()