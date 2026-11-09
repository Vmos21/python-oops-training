class Dataset:
    def __init__(self, samples):
        self.samples = samples
    def __len__(self):
        return len(self.samples)
    def __getitem__(self, key):
        try:
            return self.samples[key]
        except IndexError:
            return "IndexError: Object Out Of Range"

data = Dataset([(1, "cat"), (2, "dog"), (3, "bird")])
print(len(data))
print(data[0])
print(data[-1])
print(data[5])