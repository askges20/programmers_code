def solution(board, moves):
    h = len(board) #배열 크기
    basket = [] #바구니
    answer = 0 #터트린 인형 수
    for n in moves:
        catch = 0
        for i in range(h):
            if board[i][n-1] != 0:
                catch = board[i][n-1] #인형 잡기
                board[i][n-1] = 0
                break
        if catch == 0: #인형을 못잡은 경우
            continue
        basket.append(catch) #바구니에 넣기
        if len(basket)>=2:
            if basket[-2] == basket[-1]:
                answer += 2
                basket = basket[:-2]
    return answer
