import argparse
from job import Job
from item import Item

def do_the_job(job, items):

    i = 1 if job.extra_margin else 0
    
    while i < len(items):

        item_prop = items[i].split()

        job.add_item(Item(item_prop[0], float(item_prop[1]), 
            item_prop[2] == "exempt" if len(item_prop) == 3 else False))

        i += 1

    job.calculate_total()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument("jp", help = "путь к файлу с работой", type = str, default = "")
    parser.add_argument("-sn", help = "сохранить счет-фактуру рядом с работой", action = "store_true")
    parser.add_argument("-ip", help = "путь к файлу со счет-фактурой", type = str, default = "")
    
    args = parser.parse_args()

    path = args.jp

    try:
        with open(path, 'r') as file:           
            lines = file.readlines()

    except IOError:
        print("Не удалось открыть файл на чтение.")

    job = Job(lines[0].split()[0] == "extra-margin")        
    do_the_job(job, lines)
    
    if args.sn:
        split_path = path.split('\\')
        split_path[-1] = "invoice_" + split_path[-1]
        path = '\\'.join(split_path)

    elif not args.ip == "":
        path = args.ip

    else:
        path = ""

    print("\nGood job! Your invoice is here:\n")
    if path == "":
        print(job)

    else:
        try:
            with open(path, 'w') as file:
                file.write(str(job))

        except IOError as e:
            print("Не удалось открыть файл на запись.")

        print(path)
    