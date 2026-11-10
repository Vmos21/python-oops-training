class Model:
    def __init__(self, name):
        self.name = name
    def forward(self, x):
        return "NotImplementedError:"
    def predict(self, x):
        return self.forward(x)
    def __str__(self):
        return f"Model(name={self.name})"
class LinearModel(Model):
    def __init__(self, weight, bias):
        super().__init__("LinearModel")
        self.weight = weight
        self.bias = bias
        
    def forward(self, x):
        return self.weight*x+self.bias

class StackedModel(Model):
    def __init__(self, models):
        super().__init__("StackedModel")
        self.models = models
    def forward(self, x):
        prev = x
        for model in self.models:
            prev = model.forward(prev)
        return prev

m1 = LinearModel(2, 3)
m2 = LinearModel(1, -1)
print(m1.predict(5))
print(m2.predict(13))
stacked = StackedModel([m1, m2])
print(stacked.predict(5))
print(stacked)