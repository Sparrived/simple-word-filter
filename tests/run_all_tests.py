import sys
from typing import Callable, Optional


ALL_TESTS : list[tuple[Callable, dict]] = []

def register_test(test_func: Callable, test_args: dict):
    ALL_TESTS.append((test_func, test_args))

def simple_test(
        test_func: Callable,
        word_list: list[str], 
        sample_words: list[str], 
        other_test_args: Optional[dict] = None
) -> Callable:
    def wrapper():
        test_func(
            word_list=word_list, 
            sample_words=sample_words, 
            **(other_test_args or {})
        )
    return wrapper

def run_all_tests():
    test_count = len(ALL_TESTS)
    print(f"Running {test_count} tests...")
    finished_tests = 0
    errored_tests = 0

    for test_func, test_args in ALL_TESTS:
        try:
            test_func(*test_args)
            finished_tests += 1
        except Exception as e:
            print(f"Test {test_func.__name__} failed: {e}")
            errored_tests += 1

    print(f"Finished {finished_tests} / {test_count} tests, {errored_tests} errors.")

if __name__ == "__main__":
    sys.exit(run_all_tests())