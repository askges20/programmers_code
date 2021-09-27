def solution(sizes):
    widths, heights = [], []
    for i in range(len(sizes)):
        widths.append(max(sizes[i]))
        heights.append(min(sizes[i]))
    return max(widths) * max(heights)
