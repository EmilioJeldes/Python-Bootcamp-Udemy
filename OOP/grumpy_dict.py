class GrumpyDict(dict):
    
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOU WANT {key}, WELL IT AINT HERE!")
    
    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY?")
        print("OK FINE ...")
        return super().__setitem__(key, value)
    
    def __contains__(self, item):
        print("NO IT AINT HERE!")
        return False


d = GrumpyDict({"name": "Yoko", "city": "New York"})
print(d)
d["Place"] = "Santiago"

print(d)
