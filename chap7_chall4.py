answer = [81, 22, 32]
while True:
    n = input('数字当てゲーム！数字を入力するか、qで終了します:')
    if n == 'q':
        break
    try:
        n = int(n)
        if n in answer:
            print('正解')
            break
        else:
            print('不正解')
    except ValueError:
               print('数字を入力するか、qで終了します')
