import unittest

from walker import Direction, move

class TestCalculator(unittest.TestCase):

  def test_moveDown(self):
    x, y = move(Direction.DOWN, 0, 0)
    self.assertEqual(x, 0)
    self.assertEqual(y, -1)

  def test_moveUp(self):
    x, y = move(Direction.UP, 0, 0)
    self.assertEqual(x, 0)
    self.assertEqual(y, 1)

  def test_moveLeft(self):
    x, y = move(Direction.LEFT, 0, 0)
    self.assertEqual(x, -1)
    self.assertEqual(y, 0)

  def test_moveRight(self):
    x, y = move(Direction.RIGHT, 0, 0)
    self.assertEqual(x, 1)
    self.assertEqual(y, 0)

  def test_testException(self):
    with self.assertRaises(Exception):
      move("fake", 0, 0)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()