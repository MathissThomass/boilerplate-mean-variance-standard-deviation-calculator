import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    numbers = np.reshape(np.array(list), (3, 3))

    calculations = {'mean': [np.mean(numbers, axis=0).tolist(), np.mean(numbers, axis=1).tolist(),
                             np.mean(numbers.flatten()).tolist()],
                    'variance': [np.var(numbers, axis=0).tolist(), np.var(numbers, axis=1).tolist(),
                                 np.var(numbers.flatten()).tolist()],
                    'standard deviation': [np.std(numbers, axis=0).tolist(), np.std(numbers, axis=1).tolist(),
                                           np.std(numbers.flatten()).tolist()],
                    'max': [np.max(numbers, axis=0).tolist(), np.max(numbers, axis=1).tolist(),
                            np.max(numbers.flatten()).tolist()],
                    'min': [np.min(numbers, axis=0).tolist(), np.min(numbers, axis=1).tolist(),
                            np.min(numbers.flatten()).tolist()],
                    'sum': [np.sum(numbers, axis=0).tolist(), np.sum(numbers, axis=1).tolist(),
                            np.sum(numbers.flatten()).tolist()]}

    return calculations
