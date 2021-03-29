class my_hashmap():
    n_b = None
    d_b = None

    def __init__(self, n_b=8):
        self.n_b = n_b
        self.init_hashmap()

    def init_hashmap(self):
        self.data = [0 for i in range(self.n_b)]

    def hash(self, i1, i2):
        return (i1 + i2) % self.n_b

    def get_from_hash(self, i1, i2):
        if not self.data:
            self.init_hashmap()

        p = self.hash(i1, i2)
        return self.data[p]

    def get_from_bitmap(self, i1, i2):
        if not self.d_b:
            print("ERROR")
            return -1

        p = self.hash(i1, i2)
        return self.d_b[p]

    def increment_count(self, i1, i2):
        if not self.data:
            self.init_hashmap()

        p = self.hash(i1, i2)
        self.data[p] += 1

    def convert_to_bitmap(self, m_n_o_b, c_h=True):
        if not self.data:
            self.init_hashmap()

        self.d_b = []

        for i in self.data:
            self.d_b.append(i > m_n_o_b)

        if c_h:
            self.data = None