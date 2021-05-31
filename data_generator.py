import numpy as np



class RandomDataGenerator:
    def __init__(self) -> None:
        self.rng = np.random.default_rng()

    def gen_integers(self,
                     low: int = 1,
                     high: int = 9999999) -> np.ndarray:
        rand_size = self.get_random_size()
        random_ints = self.rng.integers(low, high, rand_size) # Integer Numbers
        print("Memory size of random_ints numpy array in Byte: ", random_ints.nbytes)

        return random_ints

    def gen_real_numbers(self,
                     low: int = 1,
                     high: int = 9999999)  -> np.ndarray:
        rand_size = self.get_random_size()
        random_reals = np.round(self.rng.uniform(low, high, rand_size), 3) # Real Numbers
        print("Memory size of random_reals numpy array in Byte: ", random_reals.nbytes)

        return random_reals

    def gen_alphanumeric(self,
                         length: int = 13) -> np.ndarray:
        rand_size = self.get_random_size()
        alpha_num = list('abcdefghijklmnopqrstuvwxyz0123456789')
        np_alpha_num = np.random.choice(alpha_num, size=[rand_size, length])
        random_alpha_num = np.array([''.join(i) for i in np_alpha_num])
        print("Memory size of random_alpha_num numpy array in Byte: ", random_alpha_num.nbytes)

        return random_alpha_num

    def gen_alphabetic(self,
                       length: int = 10) -> np.ndarray:
        rand_size = self.get_random_size()
        alpha = list('abcdefghijklmnopqrstuvwxyz')
        np_alpha = np.random.choice(alpha, size=[rand_size, length])
        random_alpha = np.array([''.join(i) for i in np_alpha])
        print("Memory size of random_alpha numpy array in Byte: ", random_alpha.nbytes)

        return random_alpha

    def combine_numpy_arrays(self, *args: list) -> np.ndarray:
        combined = np.array(args)
        combined_flat = combined.flatten()
        print("Memory size of combo numpy array in Byte: ", combined_flat.nbytes)

        return combined_flat

    def write_to_file(self,
                      np_arr: np.ndarray,
                      filename: str = "./output.txt",
                      sep: str = ", ",
                      formats: str = "%s") -> None:
        self.rng.shuffle(np_arr)
        np_arr.tofile(filename, sep=sep, format=formats)

    def get_random_size(self):
        rand_size = self.rng.integers(1000, 10000)

        return rand_size
if __name__ == "__main__":
    rand = RandomDataGenerator()

    combo = np.array([])
    combo_size_bytes_min = 106500000
    combo_size_bytes_max = combo_size_bytes_min + 1000000

    try:
        while True:
            ints = rand.gen_integers()
            reals = rand.gen_real_numbers()
            alpha = rand.gen_alphabetic()
            alpha_num = rand.gen_alphanumeric()
            print("===========================")
            combo = np.append(combo, ints)
            combo = np.append(combo, reals)
            combo = np.append(combo, alpha)
            combo = np.append(combo, alpha_num)

            if combo.nbytes in range(combo_size_bytes_min, combo_size_bytes_max):
                print(combo.nbytes)
                rand.write_to_file(combo)
                break

    except KeyboardInterrupt:
        print("Combo np Array is:", combo.nbytes)
        rand.write_to_file(combo)
        print("Combo np Array has been written to `output.txt` file!!", combo.nbytes)
