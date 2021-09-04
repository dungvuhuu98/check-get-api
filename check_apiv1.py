import requests
import time
import logging
import pyfiglet

Link = "http://10.200.39."
Range = [24,25,26]
Filename = 'list_endpoint/endpoint_v1.txt'
Ascii_banner = pyfiglet.figlet_format("Test BO API-V1")

def check_log():
    list = []
    with open('log/nohup_v1.log', 'r', encoding='utf-8') as file:
        countok = 0
        countf = 0
        for line in file:
            a = line.count('Query ok')
            b = line.count('Query fail')
            countok += a
            countf += b
            if b >= 1:
                list.append(line)
        print(str(f'\nQuery có {countok} endpoint ok, {countf} fail, coi log thêm nhé!\n'))
        for i in list:
            print(str(f'{i}'))

if __name__ == '__main__':
    print(Ascii_banner)
    print('Test APIv1 will start in 2s ...')
    time.sleep(2)
    logging.basicConfig(filename='log/nohup_v1.log', format='%(asctime)s - %(filename)s:%(lineno)d\t %(message)s', filemode='w', level=logging.DEBUG) # filemode='w': ghi de log cu
    try:
        logging.info(str(f'Test API is starting ...'))
        ii = 0
        with open(Filename, mode='r') as file:
            for l in file:
                ii+=1
                line = l.strip()
                for i in Range:
                    IP = Link+str(i)+line
                    r = requests.get(IP)
                    status = r.status_code
                    if status == 200:
                        logging.info(str(f'{IP} => Query ok, 200!'))
                        print(str(f'\nEndpoint: {ii} => {line}\n'))
                        print(str(f'\t{i} {IP} => Query ok, 200!'))
                    else:
                        logging.debug(str(f'{IP} => Query fail, {status}!'))
                        print(str(f'\t{i} {IP} => Query fail, {status}!'))
                    time.sleep(1.2)
        check_log()
        logging.info(str(f'API testing has ended!'))
        print('\nClose after 20 seconds ...')
        time.sleep(20)
    except Exception as e:
        logging.debug("{0}".format(e))
        print('[ERROR] Exception occur: ', str(e))