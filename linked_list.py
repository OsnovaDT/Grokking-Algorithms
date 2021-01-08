'''Linked list for chapter 2'''


class Cell(object):
    '''Class for cell for linked list's elements'''

    def __init__(self, value):
        self.value = value
        self.next_cell = None


class LinkedList(object):
    '''Class for linked list'''

    def __init__(self):
        self.first_cell = None

    def add(self, value):
        '''Add elements to end of the linked list'''

        new_cell = Cell(value)

        if self.first_cell is None:
            self.first_cell = new_cell

            return

        # Go to last cell
        last_cell = self.first_cell
        while last_cell.next_cell:
            last_cell = last_cell.next_cell

        last_cell.next_cell = new_cell

    def get(self, cell_index):
        '''Get element from linked list by index'''

        # Go to cell with cell_index
        last_cell = self.first_cell

        temp_index = 0

        while temp_index != cell_index:
            # Go to next cell
            last_cell = last_cell.next_cell
            temp_index += 1

        if temp_index == cell_index:
            return last_cell.value


def main():
    '''Test how linked list works'''

    linked_list = LinkedList()

    linked_list.add(1)
    linked_list.add(2)
    linked_list.add(3)

    print(linked_list.get(0))
    print(linked_list.get(1))
    print(linked_list.get(2))


if __name__ == '__main__':
    main()
