class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()


class Strategy:
    def execute(self):
        raise NotImplementedError("Subclass must implement execute method")


class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Strategy A is executed"


class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Strategy B is executed"


# Usage
context = Context(ConcreteStrategyA())
print(context.execute_strategy()) 
context = Context(ConcreteStrategyB())
print(context.execute_strategy()) 


#       OUTPUT:
# Strategy A is executed
# Strategy B is executed
