import csv


def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # take csv rows as list
        rows = list(csv_reader)

        # headers is row 0
        headers = rows[0]
        # first entry in dict is headers row
        data = {"headers": headers}
        
        # for rows 1 - last
        for row in rows[1:]:
            # key is always at 0
            key = row[0]
            # values are 1 - last
            values = row[1:]
            # zia the headers with the values as k,v pairs
            data[key] = dict(zip(headers[1:], values))
        
        return data

        
if __name__ == "__main__":
    data = read_csv("products.csv")
    for k, v in list(data.items())[1:]:
        print(k, v)
    # print("\n\n\n\n")
    # print(read_csv("products.csv"))
    pass
