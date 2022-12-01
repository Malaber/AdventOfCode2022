class Input:
    def get_lines(script_path):

        script_number = script_path.split(".")[0]

        print("##########################")
        print
        print(f"############{script_number}############")
        print
        print("##########################")
        print

        with open(f"inputs/{script_number}.txt") as f:
            return f.readlines()
