import unittest

import numpy as np
from phonopy.interface.phonopy_yaml import read_cell_yaml
from phonopy.interface.abinit import read_abinit
import os

data_dir = os.path.dirname(os.path.abspath(__file__))


class TestAbinit(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read_abinit(self):
        cell = read_abinit(os.path.join(data_dir, "NaCl-abinit.in"))
        filename = os.path.join(data_dir, "NaCl-abinit-pwscf.yaml")
        cell_ref = read_cell_yaml(filename)
        self.assertTrue(
            (np.abs(cell.get_cell() - cell_ref.get_cell()) < 1e-5).all())
        diff_pos = (cell.get_scaled_positions()
                    - cell_ref.get_scaled_positions())
        diff_pos -= np.rint(diff_pos)
        self.assertTrue((np.abs(diff_pos) < 1e-5).all())
        for s, s_r in zip(cell.get_chemical_symbols(),
                          cell_ref.get_chemical_symbols()):
            self.assertTrue(s == s_r)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAbinit)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
