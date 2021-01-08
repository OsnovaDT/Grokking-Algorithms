'''Code for stack class'''


class Stack(object):
    ''' Stack works by FIFO principle

    We can add an element to the end of the stack.
    We can get an element from the end of the stack.

    '''

    def __init__(self):
        self.__stack = []

    def add(self, element):
        '''Add an element to the end of the stack'''
        self.__stack.append(element)

    # Get from end of stack
    def get(self):
        '''Get an element from the end of the stack'''
        if self.__stack == []:
            return 'The stack is empty'
        return self.__stack.pop()


def main():
    '''Run methods for stack class'''

    stack = Stack()

    stack.add(1)
    stack.add(2)
    stack.add(3)

    print(stack.get())  # 3
    print(stack.get())  # 2
    print(stack.get())  # 1
    print(stack.get())  # The stack is empty


if __name__ == '__main__':
    main()
