def solution(numbers, hand):
    left, right = [1,4,7,10], [3,6,9,12] #키패드
    cur_left, cur_right = 10, 12 #처음 위치
    result = ""
    for n in numbers:            
        if n in left: #왼쪽 열
            result += "L"
            cur_left = n
            
        elif n in right: #오른쪽 열
            result += "R"
            cur_right = n
            
        else: #가운데 열
            n = 11 if n == 0 else n
            left_dist = abs(n - cur_left) // 3 + abs(n - cur_left) % 3
            right_dist = abs(n - cur_right) // 3 + abs(n - cur_right) % 3
            
            if left_dist>right_dist:
                result += "R"
                cur_right = n
            elif left_dist<right_dist:
                result += "L"
                cur_left = n
            else:
                if hand == "left":
                    result += "L"
                    cur_left = n
                else:
                    result += "R"
                    cur_right = n
    return result
