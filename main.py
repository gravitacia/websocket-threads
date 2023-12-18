import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <num_threads>")
        sys.exit(1)

    num_threads = int(sys.argv[1])