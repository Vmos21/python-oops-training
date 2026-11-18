class Scaler:
    dataMin, dataMax = 0, 0

    def fit(self, data):
        self.min = min(data)
        self.max = max(data)

    def transform(self, data):
        return [(x-self.min)/(self.max-self.min) for x in data]
    
    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

class TrainingRun:

    __history = []

    def __init__(self, model_name, epochs):
        self.model_name = model_name
        self.epochs = epochs

    def log(self, epoch, loss):
        self.__history.append({"epoch":epoch, "loss":loss})

    def history(self):
        return self.__history

    def best_epoch(self):
        loss = 100
        md = {}
        for d in self.__history:
            if d["loss"] < loss:
                loss = d["loss"]
                md = d
        return d

    def __str__(self):
        return f"TrainingRun(model={self.model_name}, epochs={self.epochs}, logged={len(self.__history)})"

'''
scaler = Scaler()
data = [10, 20, 30, 40, 50]
print(scaler.fit_transform(data))

run = TrainingRun("MyNet", 3)
run.log(1, 0.9)
run.log(2, 0.5)
run.log(3, 0.3)

print(run.best_epoch())
print(run)
'''
scaler = Scaler()
result = scaler.fit_transform([10, 20, 30, 40, 50])
assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
run = TrainingRun("MyNet", 3)
run.log(1, 0.9)
run.log(2, 0.5)
run.log(3, 0.3)
assert run.best_epoch() == {"epoch": 3, "loss": 0.3}
assert str(run) == "TrainingRun(model=MyNet, epochs=3, logged=3)"
print("✓ Problem 10 passed")