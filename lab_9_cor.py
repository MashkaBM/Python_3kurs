
import numpy as np

def my_coroutine():
    lst = []
    while True:
        current_input = yield
        try:
            lst.append(float(current_input))
            
        except ValueError:
            if current_input == 'mean':
                average = mean(lst)
                print(average)
            elif current_input == 'var':
                variance = var(lst)
                print(variance)
            elif current_input == 'exit':
                exit()

            else:
                raise ValueError("Incorrect input")


if __name__ == '__main__':
    corout = my_coroutine()
    next(corout)
    while True:
        corout.send(input())
