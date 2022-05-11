from argparse import ArgumentParser
import json
import csv

def convert(csv_file, json_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    ap = ArgumentParser(description='Convert restaurant dataset CSV into JSON format. Useful for correcting mistakes in the dataset')

    ap.add_argument('input_file', type=str, help='Input data CSV')
    ap.add_argument('output_file', type=str, help='Output data JSON')

    args = ap.parse_args()
    
    convert(args.input_file, args.output_file)
