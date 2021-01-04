class Cell(object):
    def __init__(self, value):
        self.value = value
        self.next_cell = None


class LinkedList(object):
    def __init__(self):
        self.first_cell = None

    def add(self, value):
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
        # Go to cell with index = cell_index
        last_cell = self.first_cell

        temp_index = 0

        while temp_index != cell_index:
            # Go to next cell
            last_cell = last_cell.next_cell
            temp_index += 1

        if temp_index == cell_index:
            return last_cell.value


linked_list = LinkedList()

linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

print(linked_list.get(0))
print(linked_list.get(1))
print(linked_list.get(2))
