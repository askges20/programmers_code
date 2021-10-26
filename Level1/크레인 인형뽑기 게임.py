def solution(board, moves):
    h = len(board) #배열 크기
    basket = [] #바구니
    answer = 0 #터트린 인형 수
    for n in moves:
        for i in range(h):
            if board[i][n-1] != 0:
                basket.append(board[i][n-1]) #잡은 인형 바구니에 넣기
                board[i][n-1] = 0
                break
        if len(basket)>=2:
            if basket[-2] == basket[-1]:
                answer += 2
                basket = basket[:-2]
    return answer
