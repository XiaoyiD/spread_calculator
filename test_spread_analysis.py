"""
Property testing for functions in spread_analysis.py.
"""

import unittest
import spread_analysis as sp_ana
import pandas as pd


class TestChallenge1(unittest.TestCase):
    """Property tests for Challenge1 related functions"""

    def test_find_best_benchmark(self):
        """Test Case for current corporate bond with both shorter term and
         longer term government bonds"""

        corporate_term = 10.3
        corporate_yield = 5.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.4, 12],
            'yield': [3.7, 4.8]
        })
        c1, sp = sp_ana.find_best_benchmark(corporate_term, corporate_yield, government_bonds)
        self.assertEqual((c1,sp),('G1', '1.60'))

    def test_find_best_benchmark_shorter_only(self):
        """Test Case for current corporate bond with
         only shorter term government bonds"""

        corporate_term = 10.3
        corporate_yield = 5.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.4, 10.1],
            'yield': [3.7, 4.8]
        })
        c1, sp = sp_ana.find_best_benchmark(corporate_term, corporate_yield, government_bonds)
        self.assertEqual((c1,sp),('G2', '0.50'))

    def test_find_best_benchmark_shorter_only(self):
        """Test Case for current corporate bond with
         only shorter term government bonds"""

        corporate_term = 10.3
        corporate_yield = 5.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.4, 10.1],
            'yield': [3.7, 4.8]
        })
        c1, sp = sp_ana.find_best_benchmark(corporate_term, corporate_yield,
                                            government_bonds)
        self.assertEqual((c1, sp), ('G2', '0.50'))

    def test_find_best_benchmark_longer_only(self):
        """Test Case for current corporate bond with
         only longer term government bonds"""

        corporate_term = 8.3
        corporate_yield = 5.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.4, 10.1],
            'yield': [3.7, 4.8]
        })
        c1, sp = sp_ana.find_best_benchmark(corporate_term, corporate_yield,
                                            government_bonds)
        self.assertEqual((c1, sp), ('G1', '1.60'))

    def test_find_best_benchmark_same_term(self):
        """Test Case for current corporate bond with
         same length term government bonds"""

        corporate_term = 9.9
        corporate_yield = 5.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.6, 10.2],
            'yield': [3.7, 4.8]
        })
        c1, sp = sp_ana.find_best_benchmark(corporate_term, corporate_yield,
                                            government_bonds)
        self.assertEqual((c1, sp), ('G2', '0.50'))


class TestChallenge2(unittest.TestCase):
    """Property tests for Challenge2 related functions"""

    def test_nochoice_closest_to_corp(self):
        """Test Case for current corporate bond with both shorter term and
         longer term government bonds, no other choice of greater or lower"""

        corporate_term = 10.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2'],
            'type': ['government', 'government'],
            'term': [9.4, 12],
            'yield': [3.7, 4.8]
        })
        g1_term, g1_yield, g2_term, g2_yield =\
            sp_ana.closest_to_corp(corporate_term, government_bonds)
        self.assertEqual((g1_term, g1_yield, g2_term, g2_yield),
                         (12.0, 4.8, 9.4, 3.7))

    def test_multi_greater_choice_closest_to_corp(self):
        """Test Case for current corporate bond with one shorter term and
         multi longer term government bonds"""

        corporate_term = 10.3
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2', 'G3', 'G4'],
            'type': ['government', 'government', 'government', 'government'],
            'term': [9.4, 10.5, 12, 19],
            'yield': [3.7, 4.8, 5.6, 9.0]
        })
        g1_term, g1_yield, g2_term, g2_yield =\
            sp_ana.closest_to_corp(corporate_term, government_bonds)
        self.assertEqual((g1_term, g1_yield, g2_term, g2_yield),
                         (10.5, 4.8, 9.4, 3.7))

    def test_multi_lower_choice_closest_to_corp(self):
        """Test Case for current corporate bond with multi shorter term and
         one longer term government bonds"""

        corporate_term = 12.5
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2', 'G3', 'G4'],
            'type': ['government', 'government', 'government', 'government'],
            'term': [9.4, 10.5, 12, 19],
            'yield': [3.7, 4.8, 5.6, 9.0]
        })
        g1_term, g1_yield, g2_term, g2_yield =\
            sp_ana.closest_to_corp(corporate_term, government_bonds)
        self.assertEqual((g1_term, g1_yield, g2_term, g2_yield),
                         (19.0, 9.0, 12.0, 5.6))

    def test_multi_mix_choice_closest_to_corp(self):
        """Test Case for current corporate bond with both shorter term and
         longer term government bonds"""

        corporate_term = 10.8
        government_bonds = pd.DataFrame.from_dict({
            'bond': ['G1', 'G2', 'G3', 'G4'],
            'type': ['government', 'government', 'government', 'government'],
            'term': [9.4, 10.5, 12, 19],
            'yield': [3.7, 4.8, 5.6, 9.0]
        })
        g1_term, g1_yield, g2_term, g2_yield =\
            sp_ana.closest_to_corp(corporate_term, government_bonds)
        self.assertEqual((g1_term, g1_yield, g2_term, g2_yield),
                         (12.0, 5.6, 10.5, 4.8))

if __name__ == "__main__":
    unittest.main()