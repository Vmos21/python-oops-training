class Config:
    def __init__(self, settings_dict):
        self.settings_dict = settings_dict
    def from_file(filename):
        with open(filename, 'r') as file:
            for line in file:
                