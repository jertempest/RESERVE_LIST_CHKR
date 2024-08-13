import sys


def file_chk(file_path):
    if len(sys.argv) != 2:
        print(
            "Correct input: python MTG_TRADEIN_PRICER.py <path/to/inventory list .csv>"
        )
        sys.exit(1)
    tradein_list = sys.argv[1]
    if not tradein_list.endswith(".csv"):
        print("It needs to be a csv file.")
        sys.exit(1)


def main():

    file_path = sys.argv[1]
    file_chk(file_path)
    
if __name__ == "__main__":
    main()