from src.custom_stack_class import CustomStack


class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if stack.is_empty():
            return []

        elements = []
        while not stack.is_empty():
            elements.append(stack.pop())

        return sorted(elements)
