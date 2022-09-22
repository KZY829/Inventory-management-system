roop = 0
item = {'pen':10, 'note':20, 'pencase':5}

while roop < 1:
    login = input('1:消費者モード 2:管理者モード 数字は半角で入力してください。>> ')
    if login == '2':
        password = input('パスワードを入力してください。>> ')
        if password == 'k0829#27':
            print(item)
            item_plus = input('在庫追加したい商品を入力してください。>> ')
            if item_plus == 'pen':
                item['pen'] += 1
                print(item)
                print('在庫追加完了を確認してください。')

            if item_plus == 'note':
                item['note'] += 1
                print(item)
                print('在庫追加完了を確認してください。')

            if item_plus == 'pen':
                item['pencase'] += 1
                print(item)
                print('在庫追加完了を確認してください。')
            exit = print('終了します')

        else:
            print('パスワードが違います。もう一度再起動してください。')
    # メイン
    if login == '1':
        print('{}商品名:在庫数'.format(item))
        shopping = input('ほしい商品名を入力してください。>> ')
        if shopping == 'pen':
            item['pen'] -= 1
            print(item)
            print('注文が完了しました。')

        if shopping == 'note':
            item['note'] -= 1
            print('注文が完了しました。')

        if shopping == 'pencase':
            item['pencase'] -= 1
            print('注文が完了しました。')
