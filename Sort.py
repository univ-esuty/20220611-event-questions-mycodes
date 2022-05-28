from operator import le

def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]


def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    ## 再帰関数を定義
    def recurrent(array: list, left: int, right: int):
        """配列のソート範囲を狭めながら再帰的にソートを行う。

        Args:
            array list: ソート対象の配列
            left int: 配列のソート範囲の左側を示す要素番号
            right int: 配列のソート範囲の右側を示す要素番号
        """

        # 配列の先頭を基準値とする（left, rightで範囲を絞るので0ではなくleftとなる）
        pivot = array[left]
        i, j = left, right

        while i <= j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            
            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        
        if j > left:
            recurrent(array, left, j)
        if i < right:
            recurrent(array, i, right)

    ## 再帰関数を実行
    recurrent(array, 0, len(array)-1)
    
    return array
    # ここまで記述


if __name__ == '__main__':
    main()
