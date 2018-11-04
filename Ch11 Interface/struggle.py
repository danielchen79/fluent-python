class Struggle:
    def __len__(self): return 42

from collections import abc
print(isinstance(Struggle(), abc.Sequence))
print(isinstance(Struggle(), abc.Sized))
print(issubclass(Struggle, abc.Sized))
