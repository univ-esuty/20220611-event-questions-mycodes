def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)


def serch_index(sorted_array, target_number):

    # ここから記述
    left, right = 0, len(sorted_array)-1
    
    while left <= right:
        idx = (left + right) // 2
        val = sorted_array[idx]
        
        if target_number < val:
            right = idx - 1
            continue
        
        if target_number > val:
            left = idx + 1
            continue
        
        return idx
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1


if __name__ == '__main__':
    main()
