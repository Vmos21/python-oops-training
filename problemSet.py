"""
=============================================================
  Python OOP Problem Set — Test Your Skills
  Difficulty: Beginner → Intermediate
  Focus: ML-relevant OOP patterns
=============================================================

Instructions:
- Each problem has a description and expected output
- Write your solution below each problem
- Run the file to check your work
- Don't look ahead — each problem builds on the last

=============================================================
"""


# ─────────────────────────────────────────────────────────
# PROBLEM 1: Basic Class & __init__
# ─────────────────────────────────────────────────────────
# Create a class called `Student` with:
#   - Attributes: name (str), marks (list of ints)
#   - A method `average()` that returns the average of marks
#
# Expected:
#   s = Student("Vikash", [85, 90, 78, 92])
#   print(s.average())  →  86.25
#   print(s.name)       →  Vikash

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 2: __str__ and __repr__
# ─────────────────────────────────────────────────────────
# Create a class `Vector` with:
#   - Attributes: x, y (both floats)
#   - __str__ should return "Vector(x, y)"
#   - __repr__ should return "Vector(x=..., y=...)"
#
# Expected:
#   v = Vector(3.0, 4.0)
#   print(v)       →  Vector(3.0, 4.0)
#   print(repr(v)) →  Vector(x=3.0, y=4.0)

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 3: Operator Overloading (__add__, __len__)
# ─────────────────────────────────────────────────────────
# Extend your `Vector` class to support:
#   - Addition: Vector(1,2) + Vector(3,4) → Vector(4,6)
#   - Length: len(v) returns the magnitude as an int
#     (magnitude = sqrt(x² + y²), truncated to int)
#
# Expected:
#   v1 = Vector(1, 2)
#   v2 = Vector(3, 4)
#   print(v1 + v2)    →  Vector(4, 6)
#   print(len(v2))    →  5

# YOUR CODE HERE (modify your Vector class above):




# ─────────────────────────────────────────────────────────
# PROBLEM 4: Inheritance
# ─────────────────────────────────────────────────────────
# Create a base class `Shape` with:
#   - Attribute: name (str)
#   - Method: area() → raises NotImplementedError
#
# Create two subclasses:
#   - `Circle(Shape)` with attribute radius
#   - `Rectangle(Shape)` with attributes width, height
#   Both should override area()
#
# Expected:
#   c = Circle(5)
#   r = Rectangle(4, 6)
#   print(c.name)    →  Circle
#   print(c.area())  →  78.53981633974483
#   print(r.area())  →  24

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 5: super() and Method Overriding
# ─────────────────────────────────────────────────────────
# Create a class `Animal` with:
#   - __init__(self, name, sound)
#   - Method: speak() → returns "{name} says {sound}!"
#
# Create a subclass `Dog(Animal)` that:
#   - Takes only name in __init__
#   - Uses super() to set sound to "Woof"
#   - Overrides speak() to add "and wags tail" at the end
#
# Expected:
#   a = Animal("Cat", "Meow")
#   d = Dog("Buddy")
#   print(a.speak())  →  Cat says Meow!
#   print(d.speak())  →  Buddy says Woof! and wags tail

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 6: Encapsulation & Properties
# ─────────────────────────────────────────────────────────
# Create a class `BankAccount` with:
#   - Private attribute: __balance (starts at 0)
#   - Property: balance (getter only — no direct setting)
#   - Methods: deposit(amount), withdraw(amount)
#   - withdraw should raise ValueError if amount > balance
#
# Expected:
#   acc = BankAccount()
#   acc.deposit(1000)
#   acc.withdraw(300)
#   print(acc.balance)     →  700
#   acc.withdraw(900)      →  ValueError: Insufficient funds

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 7: __getitem__ and __len__ (ML-relevant!)
# ─────────────────────────────────────────────────────────
# This is how PyTorch datasets work under the hood.
#
# Create a class `Dataset` with:
#   - __init__ takes a list of samples (each sample is a tuple)
#   - __len__ returns the number of samples
#   - __getitem__(idx) returns the sample at that index
#   - __getitem__ should support negative indexing
#   - Raise IndexError for out-of-range indices
#
# Expected:
#   data = Dataset([(1, "cat"), (2, "dog"), (3, "bird")])
#   print(len(data))    →  3
#   print(data[0])      →  (1, 'cat')
#   print(data[-1])     →  (3, 'bird')
#   print(data[5])      →  IndexError

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 8: Inheritance Chain (ML Model Pattern)
# ─────────────────────────────────────────────────────────
# This mimics how PyTorch models are structured.
#
# Create a base class `Model` with:
#   - __init__(self, name)
#   - Method: forward(x) → raises NotImplementedError
#   - Method: predict(x) → calls forward(x) and returns result
#   - __str__ → "Model(name=...)"
#
# Create `LinearModel(Model)` with:
#   - __init__(self, weight, bias)
#     (name should auto-set to "LinearModel")
#   - Override forward(x) → returns weight * x + bias
#
# Create `StackedModel(Model)` with:
#   - __init__(self, models) where models is a list of Model objects
#     (name should auto-set to "StackedModel")
#   - Override forward(x) → passes x through each model in sequence
#     (output of model 1 becomes input of model 2, etc.)
#
# Expected:
#   m1 = LinearModel(2, 3)        # f(x) = 2x + 3
#   m2 = LinearModel(1, -1)       # f(x) = x - 1
#   print(m1.predict(5))           →  13    (2*5 + 3)
#   print(m2.predict(13))          →  12    (13 - 1)
#
#   stacked = StackedModel([m1, m2])
#   print(stacked.predict(5))      →  12    (2*5+3=13, 13-1=12)
#   print(stacked)                 →  Model(name=StackedModel)

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 9: Class Methods & Static Methods
# ─────────────────────────────────────────────────────────
# Create a class `Config` that acts as a settings container:
#   - __init__(self, settings_dict)
#   - Class method: from_file(filename) — reads a text file
#     where each line is "key=value" and creates a Config
#   - Static method: validate(key, value) — returns True if
#     key is a non-empty string and value is not None
#   - Method: get(key, default=None) — returns value for key
#     or default if not found
#
# Expected:
#   # Assume settings.txt contains:
#   #   learning_rate=0.01
#   #   epochs=100
#   #   batch_size=32
#
#   cfg = Config({"lr": 0.01, "epochs": 100})
#   print(cfg.get("lr"))           →  0.01
#   print(cfg.get("missing", 42)) →  42
#   print(Config.validate("lr", 0.01))  →  True
#   print(Config.validate("", 0.01))    →  False

# YOUR CODE HERE:




# ─────────────────────────────────────────────────────────
# PROBLEM 10: Putting It All Together — Mini ML Pipeline
# ─────────────────────────────────────────────────────────
# Build a small ML-like pipeline using everything you've learned.
#
# Create these classes:
#
# 1. `Scaler` — normalizes data
#    - fit(data): stores min and max of the data
#    - transform(data): returns normalized data
#      formula: (x - min) / (max - min) for each x
#    - fit_transform(data): does both in one call
#
# 2. `TrainingRun`
#    - __init__(self, model_name, epochs)
#    - Private attr __history (empty list)
#    - Method: log(epoch, loss) — appends {"epoch": epoch, "loss": loss}
#    - Property: history — returns the __history list
#    - Method: best_epoch() — returns the dict with lowest loss
#    - __str__ → "TrainingRun(model=..., epochs=..., logged=...)"
#      where logged is len of history
#
# Expected:
#   scaler = Scaler()
#   data = [10, 20, 30, 40, 50]
#   print(scaler.fit_transform(data))
#   →  [0.0, 0.25, 0.5, 0.75, 1.0]
#
#   run = TrainingRun("MyNet", 3)
#   run.log(1, 0.9)
#   run.log(2, 0.5)
#   run.log(3, 0.3)
#   print(run.best_epoch())  →  {'epoch': 3, 'loss': 0.3}
#   print(run)  →  TrainingRun(model=MyNet, epochs=3, logged=3)

# YOUR CODE HERE:




# =============================================================
# TEST RUNNER — uncomment each block as you solve problems
# =============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("  OOP Problem Set — Test Runner")
    print("=" * 50)
    print()
    print("Uncomment the test blocks below as you solve")
    print("each problem to verify your solutions.")
    print()

    # --- Test Problem 1 ---
    # s = Student("Vikash", [85, 90, 78, 92])
    # assert s.average() == 86.25, f"Expected 86.25, got {s.average()}"
    # assert s.name == "Vikash"
    # print("✓ Problem 1 passed")

    # --- Test Problem 2 ---
    # v = Vector(3.0, 4.0)
    # assert str(v) == "Vector(3.0, 4.0)"
    # assert repr(v) == "Vector(x=3.0, y=4.0)"
    # print("✓ Problem 2 passed")

    # --- Test Problem 3 ---
    # v1 = Vector(1, 2)
    # v2 = Vector(3, 4)
    # v3 = v1 + v2
    # assert str(v3) == "Vector(4, 6)"
    # assert len(v2) == 5
    # print("✓ Problem 3 passed")

    # --- Test Problem 4 ---
    # import math
    # c = Circle(5)
    # r = Rectangle(4, 6)
    # assert c.name == "Circle"
    # assert abs(c.area() - math.pi * 25) < 0.0001
    # assert r.area() == 24
    # print("✓ Problem 4 passed")

    # --- Test Problem 5 ---
    # a = Animal("Cat", "Meow")
    # d = Dog("Buddy")
    # assert a.speak() == "Cat says Meow!"
    # assert d.speak() == "Buddy says Woof! and wags tail"
    # print("✓ Problem 5 passed")

    # --- Test Problem 6 ---
    # acc = BankAccount()
    # acc.deposit(1000)
    # acc.withdraw(300)
    # assert acc.balance == 700
    # try:
    #     acc.withdraw(900)
    #     assert False, "Should have raised ValueError"
    # except ValueError:
    #     pass
    # print("✓ Problem 6 passed")

    # --- Test Problem 7 ---
    # data = Dataset([(1, "cat"), (2, "dog"), (3, "bird")])
    # assert len(data) == 3
    # assert data[0] == (1, "cat")
    # assert data[-1] == (3, "bird")
    # try:
    #     data[5]
    #     assert False, "Should have raised IndexError"
    # except IndexError:
    #     pass
    # print("✓ Problem 7 passed")

    # --- Test Problem 8 ---
    # m1 = LinearModel(2, 3)
    # m2 = LinearModel(1, -1)
    # assert m1.predict(5) == 13
    # assert m2.predict(13) == 12
    # stacked = StackedModel([m1, m2])
    # assert stacked.predict(5) == 12
    # assert str(stacked) == "Model(name=StackedModel)"
    # print("✓ Problem 8 passed")

    # --- Test Problem 9 ---
    # cfg = Config({"lr": 0.01, "epochs": 100})
    # assert cfg.get("lr") == 0.01
    # assert cfg.get("missing", 42) == 42
    # assert Config.validate("lr", 0.01) == True
    # assert Config.validate("", 0.01) == False
    # assert Config.validate("key", None) == False
    # print("✓ Problem 9 passed")

    # --- Test Problem 10 ---
    # scaler = Scaler()
    # result = scaler.fit_transform([10, 20, 30, 40, 50])
    # assert result == [0.0, 0.25, 0.5, 0.75, 1.0]
    # run = TrainingRun("MyNet", 3)
    # run.log(1, 0.9)
    # run.log(2, 0.5)
    # run.log(3, 0.3)
    # assert run.best_epoch() == {"epoch": 3, "loss": 0.3}
    # assert str(run) == "TrainingRun(model=MyNet, epochs=3, logged=3)"
    # print("✓ Problem 10 passed")

    # print()
    # print("🎉 All problems solved!")