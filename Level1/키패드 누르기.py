def solution(numbers, hand):
    left, center, right = [1,4,7,10], [2,5,8,11], [3,6,9,12]
    cur_left, cur_right = 10, 12
    result = ""
    for n in numbers:
        if n==0:
            n = 11
            
        if n in left:
            result += "L"
            cur_left = n
            
        elif n in right:
            result += "R"
            cur_right = n
            
        else:
            if cur_left in center:
                left_dist = abs(center.index(n) - center.index(cur_left))
            else:
                left_dist = 1 + abs(center.index(n) - center.index(cur_left + 1))
            if cur_right in center:
                right_dist = abs(center.index(n) - center.index(cur_right))
            else:
                right_dist = 1 + abs(center.index(n) - center.index(cur_right - 1))
                
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
