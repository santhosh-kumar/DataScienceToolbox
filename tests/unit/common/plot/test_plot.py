"""
Unit Test for plot
"""
import os

from unittest import TestCase

from plot.plot import Plot
from exceptions.exceptions import PreconditionException


class TestPlot(TestCase):
    """
    Unit test for plot
    """
    TEST_PLOT_FILE_PATH = 'test_plot.png'
    TEST_SHOULD_SHOW_PLOT = False

    def setUp(self):
        """setUp

        Args:
            self: TestPlot

        Returns:
            None

        Raises:
            None
        """
        pass

    def tearDown(self):
        """tearDown

        Args:
            self: TestPlot

        Returns:
            None

        Raises:
            None
        """
        if os.path.exists(self.TEST_PLOT_FILE_PATH):
            os.remove(self.TEST_PLOT_FILE_PATH)

    def test_hist_unique(self):
        """Test hist_unique

        Args:
            self: TestPlot

        Returns:
            None

        Raises:
            None
        """
        Plot.hist_unique([1, 2, 3, 4, 5, 1, 2],
                         'numbers',
                         'count',
                         'numbers-count',
                         self.TEST_PLOT_FILE_PATH,
                         self.TEST_SHOULD_SHOW_PLOT)
        if not os.path.exists(self.TEST_PLOT_FILE_PATH):
            self.assertTrue(False, 'Plot file not found')

        # Invalid data_list
        with self.assertRaises(PreconditionException) as context:
            Plot.hist_unique(None,
                             'numbers',
                             'count',
                             'numbers-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid data_list' in str(context.exception))

        # Invalid x_label
        with self.assertRaises(PreconditionException) as context:
            Plot.hist_unique([1, 2, 3, 4, 5, 1, 2],
                             None,
                             'count',
                             'numbers-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid x_label' in str(context.exception))

        # Invalid y_label
        with self.assertRaises(PreconditionException) as context:
            Plot.hist_unique([1, 2, 3, 4, 5, 1, 2],
                             'numbers',
                             None,
                             'numbers-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid y_label' in str(context.exception))

        # Invalid title
        with self.assertRaises(PreconditionException) as context:
            Plot.hist_unique([1, 2, 3, 4, 5, 1, 2],
                             'numbers',
                             'count',
                             None,
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid title' in str(context.exception))

    def test_bar(self):
        """Test bar

        Args:
            self: TestPlot

        Returns:
            None

        Raises:
            None
        """
        Plot.bar(['a', 'e', 'i', 'o', 'u'],
                 [1, 2, 3, 4, 5],
                 'vowels',
                 'counts',
                 'vowels-count',
                 self.TEST_PLOT_FILE_PATH,
                 self.TEST_SHOULD_SHOW_PLOT)
        if not os.path.exists(self.TEST_PLOT_FILE_PATH):
            self.assertTrue(False, 'Plot file not found')

        # Invalid data_list1
        with self.assertRaises(PreconditionException) as context:
            Plot.bar(None,
                     [1, 2, 3, 4, 5],
                     'alphabets',
                     'counts',
                     'alphabets-count',
                     self.TEST_PLOT_FILE_PATH,
                     self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid data_list1' in str(context.exception))

        # Invalid data_list2
        with self.assertRaises(PreconditionException) as context:
            Plot.bar(['a', 'e', 'i', 'o', 'u'],
                     None,
                     'alphabets',
                     'counts',
                     'alphabets-count',
                     self.TEST_PLOT_FILE_PATH,
                     self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid data_list2' in str(context.exception))

        # Invalid x_label
        with self.assertRaises(PreconditionException) as context:
            Plot.bar(['a', 'e', 'i', 'o', 'u'],
                     [1, 2, 3, 4, 5],
                     None,
                     'counts',
                     'alphabets-count',
                     self.TEST_PLOT_FILE_PATH,
                     self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid x_label' in str(context.exception))

        # Invalid y_label
        with self.assertRaises(PreconditionException) as context:
            Plot.bar(['a', 'e', 'i', 'o', 'u'],
                     [1, 2, 3, 4, 5],
                     'alphabets',
                     None,
                     'alphabets-count',
                     self.TEST_PLOT_FILE_PATH,
                     self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid y_label' in str(context.exception))

        # Invalid title
        with self.assertRaises(PreconditionException) as context:
            Plot.bar(['a', 'e', 'i', 'o', 'u'],
                     [1, 2, 3, 4, 5],
                     'alphabets',
                     'counts',
                     None,
                     self.TEST_PLOT_FILE_PATH,
                     self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid title' in str(context.exception))

    def test_bar_stacked(self):
        """Test test_bar_stacked

        Args:
            self: TestPlot

        Returns:
            None

        Raises:
            None
        """
        Plot.bar_stacked(['a', 'e', 'i', 'o', 'u'],
                         [1, 2, 3, 4, 5],
                         'vowels',
                         'counts',
                         'vowels-count',
                         self.TEST_PLOT_FILE_PATH,
                         self.TEST_SHOULD_SHOW_PLOT)
        if not os.path.exists(self.TEST_PLOT_FILE_PATH):
            self.assertTrue(False, 'Plot file not found')

        # Invalid data_list1
        with self.assertRaises(PreconditionException) as context:
            Plot.bar_stacked(None,
                             [1, 2, 3, 4, 5],
                             'alphabets',
                             'counts',
                             'alphabets-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid data_list1' in str(context.exception))

        # Invalid data_list2
        with self.assertRaises(PreconditionException) as context:
            Plot.bar_stacked(['a', 'e', 'i', 'o', 'u'],
                             None,
                             'alphabets',
                             'counts',
                             'alphabets-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid data_list2' in str(context.exception))

        # Invalid x_label
        with self.assertRaises(PreconditionException) as context:
            Plot.bar_stacked(['a', 'e', 'i', 'o', 'u'],
                             [1, 2, 3, 4, 5],
                             None,
                             'counts',
                             'alphabets-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid x_label' in str(context.exception))

        # Invalid y_label
        with self.assertRaises(PreconditionException) as context:
            Plot.bar_stacked(['a', 'e', 'i', 'o', 'u'],
                             [1, 2, 3, 4, 5],
                             'alphabets',
                             None,
                             'alphabets-count',
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid y_label' in str(context.exception))

        # Invalid title
        with self.assertRaises(PreconditionException) as context:
            Plot.bar_stacked(['a', 'e', 'i', 'o', 'u'],
                             [1, 2, 3, 4, 5],
                             'alphabets',
                             'counts',
                             None,
                             self.TEST_PLOT_FILE_PATH,
                             self.TEST_SHOULD_SHOW_PLOT)

        self.assertTrue('Invalid title' in str(context.exception))
