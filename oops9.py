class Config:
    def __init__(self, settings_dict):
        self.settings_dict = settings_dict
    def from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                l = line.split()
                self.settings_dict[l[0]] = self.settings_dict[l[1]]
            