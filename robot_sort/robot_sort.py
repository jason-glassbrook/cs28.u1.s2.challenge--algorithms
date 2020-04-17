class SortingRobot:

    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l  # The list the robot is tasked with sorting
        self._item = None  # The item the robot is holding
        self._position = 0  # The list position the robot is at
        self._light = "OFF"  # The state of the robot's light
        self._time = 0  # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def light_is_off(self):
        return not self.light_is_on()

    def put_down_to_left(self):
        """
        from:
            ...] [ ] [a] [...
                    {[b]}
        to:
            ...] [b] [a] [...
                {[ ]}
        """
        self.move_left()
        self.swap_item()

    def put_down_to_right(self):
        """
        from:
            ...] [a] [ ] [...
                {[b]}
        to:
            ...] [a] [b] [...
                    {[ ]}
        """
        self.move_right()
        self.swap_item()

    def swap_to_left(self):
        """
        from:
            ...] [ ] [a] [...
                    {[b]}
        to:
            ...] [a] [b] [...
                {[ ]}
        """
        self.swap_item()
        self.put_down_to_left()

    def swap_to_right(self):
        """
        from:
            ...] [a] [ ] [...
                {[b]}
        to:
            ...] [b] [a] [...
                    {[ ]}
        """
        self.swap_item()
        self.put_down_to_right()

    def is_sorted(self):
        return self.light_is_on()

    def is_not_sorted(self):
        return not self.is_sorted()

    def record_not_reordering(self, force=False):
        if force:
            self.set_light_on()
        else:
            # don't change state of light
            pass

    def record_reordering(self):
        self.set_light_off()

    def sort_moving_left_to_right(self):
        # pick up an item
        self.swap_item()

        # compare current item to the right
        self.move_right()

        if self.compare_item() > 0:
            # item in hand was more
            self.record_reordering()
            self.swap_to_left()

        else:
            # item in hand was less or equal
            self.record_not_reordering()
            self.put_down_to_left()

        # we're now back where we started
        self.move_right()

    def sort(self):
        """
        Sort the robot's list.
        """

        # get this thing started
        self.record_reordering()

        while self.is_not_sorted():

            # this is tentative
            self.record_not_reordering(True)

            # check from left to right
            while self.can_move_right():
                self.sort_moving_left_to_right()

            # reset position
            while self.can_move_left():

                self.move_left()

            # THIS SORTS, BUT... INFINITE LOOP
            # # this is tentative
            # self.record_not_reordering(True)
            #
            # # check from right to left
            # while self.can_move_left():
            #     self.sort_moving_right_to_left()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    import random

    numbers = [random.randint(0, 10) for __ in range(10)]

    robot = SortingRobot(numbers)

    robot.sort()
    print(robot._list)
