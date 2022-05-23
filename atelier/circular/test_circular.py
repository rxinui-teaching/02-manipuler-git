"""Test Circular datastructure"""
from circular import Circular


class TestCircular:
    def setup_method(self):
        self.c = Circular(3)

    def teardown_method(self):
        self.c = None

    def test_is_empty(self):
        print("- expected to be empty")
        assert self.c.is_empty()
        print("- expected to NOT be empty")
        self.c.structure[0], self.c.nb_element = 1, 1
        assert not self.c.is_empty()

    def test_is_full(self):
        print("- expected to be full")
        self.c.structure[0], self.c.nb_element = 0, 1
        self.c.structure[1], self.c.nb_element = 0, 2
        assert not self.c.is_full()
        self.c.structure[2], self.c.nb_element = 0, 3
        assert self.c.is_full()

    def test_add(self):
        print("- add when empty")
        self.c.add(0)
        assert (
            self.c.nb_element == 1
            and self.c.structure[0] == 0
            and self.c.structure[1] is None
            and self.c.structure[2] is None
        )
        print("- add until full")
        self.c.add(3.14)
        assert (
            self.c.nb_element == 2
            and self.c.structure[0] == 0
            and self.c.structure[1] == 3.14
            and self.c.structure[2] is None
        )
        print("- add when full")
        self.c.add("bitcoin")
        assert self.c.is_full() and self.c.structure[2] == "bitcoin"
        self.c.add("ethereum")
        assert self.c.is_full() and "ethereum" not in self.c

    def test_clean(self):
        print("- clean when empty")
        self.c.clean()
        assert self.c.is_empty()
        print("- clean when has elements")
        self.c.structure[0], self.c.nb_element = 0, 1
        self.c.clean()
        assert self.c.is_empty()
        print("- clean when full")
        self.c.structure[1], self.c.nb_element = 0, 2
        self.c.structure[2], self.c.nb_element = 0, 3
        self.c.clean()
        assert self.c.is_empty()

    def test_shift_left(self):
        print("- shift left when empty")
        self.c.shift_left()
        assert self.c.is_empty()
        print("- shift left some elements")
        self.c.structure[0], self.c.nb_element = 28, 1
        self.c.structure[1], self.c.nb_element = "ok", 2
        self.c.shift_left()
        assert self.c.structure[0] == "ok" and self.c.structure[1] is None and self.c.structure[2] == 28

    def test_pop(self):
        print("- pop when full")
        self.c.structure[0], self.c.nb_element = 28, 1
        self.c.structure[1], self.c.nb_element = "ok", 2
        self.c.structure[2], self.c.nb_element = False, 3
        self.c.pop()
        assert self.c.nb_element == 2 and self.c.structure[0] == "ok" and self.c.structure[1] == False and self.c.structure[2] is None
        print("- pop until empty")
        self.c.pop()
        assert self.c.nb_element == 1 and self.c.structure[0] == False and self.c.structure[1] is None and self.c.structure[2] is None
        print("- pop when empty")
        self.c.pop()
        assert self.c.is_empty()
