import unittest

from src.bfs.maze_escape import maze_escape
from src.bfs.word_conversion import word_conversion
from src.bfs.shortest import shortest

class TestBFS(unittest.TestCase):

    def test_ice(self):
        self.assertEqual(maze_escape(0,0,[[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]), 10)

    def test_word_conversion(self):
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
        self.assertEqual(word_conversion("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
    
    def test_short(self):
        self.assertEqual(shortest(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),3)
    