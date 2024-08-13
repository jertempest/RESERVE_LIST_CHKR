"""
Take CSV file check if there are any cards on the Reserve List (an in program list). Then Print out which cards were on both
"""

import sys
import csv
import file_chkr


r_list = "reserve_list.csv"
trade_list = sys.argv[1] if len(sys.argv) > 1 else "test_tradein.csv"

def compare_csv(r_list,trade_list):
    with open(r_list, mode="r") as csv_reserve, open(trade_list, mode="r") as csv_trade:
        reserve_read = csv.reader(csv_reserve)
        trade_read = csv.reader(csv_trade)
        
        reserve_set = set(tuple(row) for row in reserve_read)
        trade_set = set(tuple(row) for row in trade_read)
        
        matches = reserve_set.intersection(trade_set)
        
        for match in matches:
            print(match)

def main():
    file_chkr.file_chk(trade_list)
    compare_csv(r_list,trade_list)


if __name__ == "__main__":
    main()
