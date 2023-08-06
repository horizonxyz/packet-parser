import importlib.util
import inspect

# Import the module
spec = importlib.util.spec_from_file_location("packet_structs", "packet_structs.py")
packet_structs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packet_structs)

# Get all classes in the module
classes = inspect.getmembers(packet_structs, inspect.isclass)

# Create a file to write the functions to
with open("packet_structs_functions.py", "w") as f:
    # Write a function for each class
    for name, cls in classes:
        f.write(f"def print_{name}(v):\n")
        f.write(f"  print('Fields of {name}:')\n")
        cnt = 0
        for field in cls._fields_:
            f.write(f"  print(f\" - {field[0]}: " + "{v." + field[0] + "}\")\n")
        f.write("\n")

print("Functions written to packet_structs_functions.py")