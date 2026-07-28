class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
# Usage
# True if variables point to the same instance else False
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)

# Output: True