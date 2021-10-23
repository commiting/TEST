import hashlib


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

if __name__ == '__main__':
    run= get_md5('{"username":"20154084","password":"123456"}')
    print(run)