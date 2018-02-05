"""
This module contains different plot utilities
"""
import matplotlib.pyplot as plt

import numpy as np

class Plot:
    """
    Plot Utilities
    """
    @staticmethod
    def get_random_colors(count):
        """Generates a list of random colors for the plot
        Args:
            count   - color count to generate
        Raises:
            None
        """
        np.random.seed(0)
        colors = np.random.rand(count, 3)
        return colors

    @staticmethod
    def hist_unique(data_list,
                    x_label,
                    y_label,
                    title,
                    save_file_path,
                    should_show=True,
                    bar_width=0.35,
                    alpha=0.4,
                    color='b',
                    logger=None):
        """Generates a histogram for all unique values in the data_list
        Args:
            data_list   - input data_list
            x_label     - x axis label for the plot
            y_label     - y axis label for the plot
            title       - title for the plot
            should_show - should show the plot 
            bar_width   - width of the bar
            alpha       - opacity of the bar
            color       - color of the bar
            logger      - shared logger object
        Raises:
            None
        Note:
            TODO - bar_width becomes large if the bar count becomes low (need to fix)
        """
        # get unique elements and its counts
        unique, counts = np.unique(data_list, return_counts=True)

        # get the indexes
        index = np.arange(len(unique))

        # draw a bar chart with counts and indexes
        plt.bar(index, 
                counts,
                bar_width,
                alpha=alpha,
                color=color)

        # set x and y labels
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # set title and plot
        plt.title(title)
        plt.xticks(index + bar_width/2, unique)

        if save_file_path is not None:
            plt.savefig(save_file_path)
            plt.close()

        # show plot if needed
        if should_show == True:
            plt.show()

    @staticmethod
    def bar(data_list1,
            data_list2,
            x_label,
            y_label,
            title,
            save_file_path,
            should_show=True,
            bar_width=0.35,
            alpha=0.4,
            color='b',
            logger=None):
        """Generates a bar chart with values in the data_list1 (on x-axis) and data_list2 (on y-axis)
        Args:
            data_list1  - input data_list1
            data_list2  - input data_list2
            x_label     - x axis label for the plot
            y_label     - y axis label for the plot
            title       - title for the plot
            should_show - should show the plot 
            bar_width   - width of the bar
            alpha       - opacity of the bar
            color       - color of the bar
            logger      - shared logger object
        Raises:
            None
        """

        # get the indexes
        index = np.arange(len(data_list1))

        # draw a bar chart with counts and indexes
        plt.bar(data_list1, 
                data_list2,
                bar_width,
                alpha=alpha,
                color=color)

        # set x and y labels
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # set title and plot
        plt.title(title)
        plt.xticks(index + bar_width/2, data_list1)

        if save_file_path is not None:
            plt.savefig(save_file_path)
            plt.close()

        # show plot if needed
        if should_show == True:
            plt.show()


    @staticmethod
    def bar_stacked(data_list1,
                    data_list2,
                    x_label,
                    y_label,
                    title,
                    save_file_path,
                    should_show=True,
                    top_items_count = -1,
                    horizontal=False,
                    plot_width=None,
                    plot_height=None,
                    bar_width=0.35,
                    alpha=1,
                    logger=None):
        """Generates a stacked bar chart with for unique labels in data_list1 and stacked by types in data_list2
        Args:
            data_list1          - input data_list1 (main data)
            data_list2          - input data_list2 (sub-data for stacking)
            x_label             - x axis label for the plot
            y_label             - y axis label for the plot
            title               - title for the plot
            should_show         - should show the plot 
            top_items_count     - top items to use from data_list1
            plot_width          - width of the plot
            plot_height         - height of the plot
            bar_width           - width of the bar
            alpha               - opacity of the bar
            color               - color of the bar
            logger              - shared logger object
        Raises:
            None
        """
        # get top elements by count in data_list1
        unique1, counts1    = np.unique(data_list1, return_counts=True)
        sorted_indexes      = sorted(range(len(counts1)), key=lambda k: counts1[k], reverse=True)

        top_data_list1      = unique1.tolist()
        if top_items_count != -1:
            top_data_list1  = [unique1[x] for x in sorted_indexes[0:top_items_count-1]]

        index               = np.arange(len(top_data_list1))

        # get unique elements in the second list and its counts
        unique2, counts2 = np.unique(data_list2, return_counts=True)

        temp_data_list1 = []
        temp_data_list2 = []
        for i in top_data_list1:
            temp_indexes     = [j for j, x in enumerate(data_list1) if x == i]
            temp_data_list1  = temp_data_list1 + [data_list1[x] for x in temp_indexes]
            temp_data_list2  = temp_data_list2 + [data_list2[x] for x in temp_indexes]

        colors = Plot.get_random_colors(len(unique2))

        if plot_height is not None and plot_width is not None:
            fig = plt.figure(figsize=(plot_width, plot_height))

        # draw a bar chart with counts and indexes
        prev_plot_counts = [0]*(len(top_data_list1))
        color_index = 0
        for field_name in unique2:
            field_indexes                   = [j for j, x in enumerate(temp_data_list2) if x == field_name]
            data_list                       = [temp_data_list1[x] for x in field_indexes]
            data_unique, data_counts        = np.unique(data_list, return_counts=True)

            plot_counts = [0]*(len(top_data_list1))

            for i in range(len(data_unique)):
                idx = top_data_list1.index(data_unique[i])
                plot_counts[idx] =  data_counts[i]
            color = colors[color_index]
            if horizontal:
                plt.barh(index, 
                         plot_counts,
                         bar_width,
                         alpha=alpha,
                         color=color,
                         left=prev_plot_counts)
            else:
                plt.bar(index, 
                        plot_counts,
                        bar_width,
                        alpha=alpha,
                        color=color,
                        bottom=prev_plot_counts)
            color_index = color_index + 1
            prev_plot_counts = [x + y for x, y in zip(plot_counts, prev_plot_counts)]

        # set x and y labels
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # set title and plot
        plt.title(title)
        if horizontal:
            plt.yticks(index + bar_width/2, top_data_list1)
        else:
            plt.xticks(index + bar_width/2, top_data_list1)

        plt.legend(unique2, loc='best')

        if save_file_path is not None:
            plt.savefig(save_file_path)
            plt.close()

        # show plot if needed
        if should_show == True:
            plt.show()
