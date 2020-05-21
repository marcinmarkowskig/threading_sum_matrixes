from sumTwoMatrixes import sumTwoMatrixes
from showMatrix import showMatrix
import threading

def sumThreading(matrix_a, matrix_b, matrix_c, matrix_d, s):
    first_thread = threading.Thread(group=None, target=sumTwoMatrixes(matrix_a, matrix_b, s, "1"), name=None, args=(), kwargs={}, daemon=None)
    second_thread = threading.Thread(group=None, target=sumTwoMatrixes(matrix_c, matrix_d, s, "2"), name=None, args=(), kwargs={}, daemon=None)
    first_thread.start()
    second_thread.start()

    while first_thread.is_alive() or second_thread.is_alive():
        pass
