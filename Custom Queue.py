class MyQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue has no items."""
        return len(self.items) == 0

    def add(self, element):
        """Add an element to the back of the queue."""
        self.items.append(element)

    def remove(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            print("Queue is empty! Cannot remove an element.")
            return None
        return self.items.pop(0)

    def front(self):
        """Get the front element without removing it."""
        if self.is_empty():
            print("Queue is empty! Cannot access the front element.")
            return None
        return self.items[0]

    def count(self):
        """Return the number of elements currently in the queue."""
        return len(self.items)

    def show(self):
        """Display all current elements in the queue."""
        if self.is_empty():
            print("Queue is currently empty.")
        else:
            print("Current queue elements:", self.items)


# Example
if __name__ == "__main__":
    queue = MyQueue()

    queue.add(5)
    queue.add(15)
    queue.add(25)
    queue.add(35)

    queue.show()
    print("Removed element:", queue.remove())
    print("Removed element:", queue.remove())

    queue.show()
    print("Front element:", queue.front())
    print("Number of elements in the queue:", queue.count())
