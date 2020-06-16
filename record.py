import datetime
import json
import os
import subprocess
from time import sleep

from tqdm import tqdm

SSID_CMD = "/System/Library/PrivateFrameworks/Apple80211.framework/Resources/airport -I | grep SSID | " \
           "grep -v BSSID | cut -d ':' -f 2"


def main():
    name = 'speed_records.csv'
    # DATE, SSID, DOWNLOAD, UPLOAD, PING.
    if not os.path.isfile(name):
        with open(name, 'w') as w:
            w.write('date, ssid, download, upload, ping\n')
    with open(name, 'a+') as w:
        while True:
            ssid = subprocess.check_output(SSID_CMD, shell=True).decode('utf8').strip()
            now = datetime.datetime.now()
            output_cli = subprocess.check_output('speedtest-cli --json', shell=True)
            results = json.loads(output_cli.decode('utf8'))
            download = float(results['download']) * 1e-6
            upload = float(results['upload']) * 1e-6
            ping = results['ping']
            line = f'{now}, {ssid}, {download:.3f}, {upload:.3f}, {ping}'
            print(line)
            w.write(line + '\n')
            w.flush()
            for _ in tqdm(range(60 * 10), desc='waiting'):
                sleep(1)


if __name__ == '__main__':
    main()
