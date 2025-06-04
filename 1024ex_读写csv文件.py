# 读取csv文件
# file_instance = open(path_to_file,encoding='UTF8')
# csv_reader = csv.reader(file_instance)
# for line in csv_reader:
#     print(line)
import csv
def read_csv(filename):

    file_instance = open(filename,encoding='UTF8')

    csv_reader = csv.reader(file_instance)

    for line in csv_reader:
        print(line)

    file_instance.close()


def write_csv(filename):
    file_instance = open(filename,'w',encoding='UTF8')

    csv_writer = csv.writer(file_instance)

    header = ['name','chinese','english','math']
    row_1 = ['zhangsan','80','87','100']

    csv_writer.writerow(header)
    csv_writer.writerow(row_1)
    file_instance.close()

if __name__ == '__main__':
    filename = 'students2.csv'
    write_csv(filename)
    read_csv(filename)