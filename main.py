roop = 0
item = {'pen':10, 'note':20, 'pencase':5}

while roop < 1:
    login = input('1:消費者モード 2:管理者モード 数字は半角で入力してください。>> ')
    if login == '2':
        password = input('パスワードを入力してください。>> ')
        if password == 'k0829#27':
            action = input('1:在庫追加 2:商品追加 >> ')
            if action == '1':
                    print(item)
                    item_plus = input('在庫追加したい商品を入力してください。>> ')
                    if item_plus == 'pen':
                        item['pen'] += 1
                        print(item)
                        print('在庫追加完了を確認してください。')
                        print('終了します')

                    if item_plus == 'note':
                        item['note'] += 1
                        print(item)
                        print('在庫追加完了を確認してください。')
                        print('終了します')

                    if item_plus == 'pen':
                        item['pencase'] += 1
                        print(item)
                        print('在庫追加完了を確認してください。')
                        print('終了します')

            if action == '2':
                item_name_plus = input('追加する商品を英語かつ半角で入力 >> ')
                item_count_plus = input('追加する商品の在庫を半角で入力 >> ')
                item_count = int(item_count_plus)
                item[item_name_plus] = item_count
                print(item)
                print('商品追加を確認してください。')
                print('終了します。')
        
        else:
            print('パスワードが違います。もう一度再起動してください。')

    # メイン
    if login == '1':
        print('{}商品名:在庫数'.format(item))
        shopping = input('購入した商品名を入力してください。(一つずつ入力してください。)>> ')
        if shopping:
            item[shopping] -= 1
            print(item)
            print('注文が完了しました。')
