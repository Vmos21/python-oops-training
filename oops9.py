class Config:
    def __init__(self, settings_dict):
        self.settings_dict = settings_dict
    def from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                l = line.split()
                self.settings_dict[l[0]] = self.settings_dict[l[1]]
    @staticmethod
    def validate(key, value):
        if key != "" and value != None:
            return True
        return False

    def get(self, key, default = None):
        if key in self.settings_dict:
            return self.settings_dict[key]
        return default

cfg = Config({"lr":0.01, "epochs":100})
print(cfg.get("lr"))
print(cfg.get("missing", 42))
print(Config.validate("lr", 0.01))
print(Config.validate("", 0.01))
