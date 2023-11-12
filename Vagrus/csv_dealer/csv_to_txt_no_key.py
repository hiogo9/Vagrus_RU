import os
import csv
import json
from pprint import pprint
from libs.input_output import read_file

out = {}
cur_path = os.getcwd()
csv_dir_path = f'{cur_path}/csv_in'
out_json_dir = f'{cur_path}/json_out'
txt_out_dir = f'{cur_path}/txt_out'

if not os.path.isdir(out_json_dir):
    os.makedirs(out_json_dir)
if not os.path.isdir(txt_out_dir):
    os.makedirs(txt_out_dir)

csv_files = os.listdir(csv_dir_path)
csv_in_paths = [f'{csv_dir_path}/{f}' for f in csv_files]

for filename in csv_files:
    coding = "utf8"
    res_data = []
    path = f'{csv_dir_path}/{filename}'
    out_path = f'{txt_out_dir}/{filename.replace("csv","txt")}'
    key_path = f'{out_json_dir}/{filename.replace("csv","json")}'
    open(out_path, 'w', encoding="utf8").close()
    if not os.path.isfile(path):
        print(path)
        input('is not a file, press enter to continue')
        continue
    if not filename.endswith('.csv'):
        print(path)
        input('is not a  csv file, press enter to continue')
        continue

    with open(f'{path}', newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter='÷', quotechar='"')
        res_data = list(spamreader)

    for num,line_list in enumerate(res_data):
        try:
            l_uid = line_list[0]
            l_type = line_list[1]
            l_title = line_list[2]
            l_altltitle = line_list[3]
            l_desc = line_list[4]
            l_altdesc = line_list[5]
            out[l_uid] = {"uid":l_uid,
                        "type":l_type,
                        "title":l_title,
                        "altitle":l_altltitle,
                        "desc":l_desc,
                        "altdesc":l_altdesc,
                        "num":num
                        }
            with open(out_path, 'a', encoding="utf8") as f:
                if l_title:
                    res_string = l_title.replace('\n','\\n').replace('\r','') + '\n'
                    f.write(res_string)
                if l_altltitle:
                    res_string = l_altltitle.replace('\n','\\n').replace('\r','') + '\n'
                    f.write(res_string) 
                if l_desc:
                    res_string = l_desc.replace('\n','\\n').replace('\r','') + '\n'
                    f.write(res_string)
                if l_altdesc:
                    res_string = l_altdesc.replace('\n','\\n').replace('\r','') + '\n'
                    f.write(res_string)
        except Exception as e:
            print(f'{e} {line_list}')
            input('press enter to exit')
            exit()
    with open(key_path, 'w', encoding="utf8") as json_f:
        res_keys = json.dumps(out, indent=4,ensure_ascii=False)
        json_f.write(res_keys)


print('done')
input('press enter to exit')
exit()


