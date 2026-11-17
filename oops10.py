class Scaler:
    dataMin, dataMax = 0, 0

    def fit(self, data):
        self.min = min(data)
        self.max = max(data)

    def transform(data):
        return [(x-min)/(max-min) for x in data]
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

class TrainingRun:
    def __init__(self, model_name, epochs):
        self.model_name = model_name
        self.epochs = epochs

    def __history(l):
        pass