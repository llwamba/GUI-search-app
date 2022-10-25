# Header
'''\
By LIONEL LWAMBA
10/16/2022
'''

from tkinter import *


count_binary_search = 0


def main():
    """
    Main function

    The Big O Notation of the binary search is O(log N)
    The Big O Notation of the Merge Sort is n log n

    """
    # Get value from user
    # user to enter a comma separated list of integers
    valuesList = list_input.get()
    array1 = valuesList.split(",")
    array = list(map(int, array1))

    # Get value from user
    # user to enter an integer to search for
    valueSearchStr = searchFor_input.get()
    valueSearch = int(valueSearchStr)

    # Sort the array
    sorted_array = merge_sort(array, ascend)
    sortedArray_output.config(text=f"{sorted_array}")

    # Search for value in the array entered by the user
    binary_search(sorted_array, valueSearch)


def merge_sort(array, sorter):
    """
    Merge Sort
    """
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle], sorter)
        right = merge_sort(array[middle:], sorter)
        return merge(left, right, sorter)


def merge(left, right, sorter):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if sorter(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def ascend(x, y):
    """
    Function for ascending order
    """
    return x < y


def binary_search(array, value):
    """
    Binary search
    """

    # Define the bottom limit
    lower_bound = 0
    # Define the top limit
    upper_bound = len(array) - 1
    # Iterate through the array
    while lower_bound <= upper_bound:
        global count_binary_search
        count_binary_search += 1
        # Set the middle index
        middle_index = (lower_bound + upper_bound) // 2
        # Set the middle value
        middle_value = array[middle_index]

        # Check if the value is found
        if middle_value == value:
            # Return the value
            messageDisplay_label.config(
                text=f"Found {value} at index {middle_index} in the sorted list \nThe number of iterations for binary search is approximately {count_binary_search} iterations.")
            return value

        # Verify if the
        elif value < middle_value:
            # Set the upper bound
            upper_bound = middle_index - 1

        # Verify if the value is greater than the middle value
        elif value > middle_value:
            # Set the lower bound
            lower_bound = middle_index + 1

    # if value not found
    messageDisplay_label.config(text=f"{value} not found")


"""
Following code for GUI

"""
Window = Tk()
Window.title("Search Program")
Window.config(padx=20, pady=20)

list_label = Label(text="Please enter a comma separated list of integers:")
list_label.grid(column=1, row=0)
list_input = Entry()
list_input.grid(column=1, row=1)
list_label.config(pady=7)

searchFor_label = Label(text="Please enter a number to search for:")
searchFor_label.grid(column=1, row=2)
searchFor_input = Entry(width=5)
searchFor_input.grid(column=1, row=3)
searchFor_label.config(pady=7)


sortedArray_label = Label(Window, text="Sorted List: ", font=(
    "Calibri", 12, "bold"))
sortedArray_label.grid(column=1, row=4)
sortedArray_output = Label(text="0")
sortedArray_output.grid(column=2, row=4)
sortedArray_label.config(pady=15)


messageDisplay_label = Label(Window, text="", font=(
    "Calibri", 12, "bold", "italic"))
messageDisplay_label.grid(column=1, row=5)
messageDisplay_label.config(pady=10)

search_button = Button(text="Search", command=main)
search_button.grid(column=0, row=6)

quit_button = Button(text="Quit", command=Window.quit)
quit_button.grid(column=3, row=6)

Window.mainloop()
