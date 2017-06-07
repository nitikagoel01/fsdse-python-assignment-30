from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        d1 = {'a': 100, 'b': 200, 'c': 300}
        d2 = {'a': 300, 'b': 200, 'd': 400}
        result = solution(d1, d2)
        self.assertEqual(result['a'], 400)
        self.assertEqual(result['b'], 400)
        self.assertEqual(result['c'], 300)
        self.assertEqual(result['d'], 400)


