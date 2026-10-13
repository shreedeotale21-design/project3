
import unittest
import matplotlib
matplotlib.use("Agg")

from time_series_visualizer import (
    draw_line_plot,
    draw_bar_plot,
    draw_box_plot
)


class TestPlots(unittest.TestCase):

    def test_line_plot(self):
        fig = draw_line_plot()
        ax = fig.axes[0]

        self.assertEqual(
            ax.get_title(),
            "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        )
        self.assertEqual(ax.get_xlabel(), "Date")
        self.assertEqual(ax.get_ylabel(), "Page Views")

    def test_bar_plot(self):
        fig = draw_bar_plot()
        ax = fig.axes[0]

        self.assertEqual(ax.get_xlabel(), "Years")
        self.assertEqual(ax.get_ylabel(), "Average Page Views")
        self.assertEqual(ax.get_legend().get_title().get_text(), "Months")

    def test_box_plot(self):
        fig = draw_box_plot()

        self.assertEqual(len(fig.axes), 2)
        self.assertEqual(
            fig.axes[0].get_title(),
            "Year-wise Box Plot (Trend)"
        )
        self.assertEqual(
            fig.axes[1].get_title(),
            "Month-wise Box Plot (Seasonality)"
        )


if __name__ == "__main__":
    unittest.main()
