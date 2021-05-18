def solution(bridge_length, weight, truck_weights):
    totaltime = 0
    totaltrucknum = len(truck_weights)
    arrivedtrucknum = 0
    bridge = []
    trucktime = []
    while(True):
        totaltime = totaltime + 1 #시간 지남
        for t in trucktime:
            if t == bridge_length: #다 건넜으면 내린다
                arrivedtrucknum = arrivedtrucknum + 1
                bridge = bridge[1:]
                trucktime = trucktime[1:]

        if len(truck_weights) > 0:
            if sum(bridge) + truck_weights[0] <= weight: #무게가 weight를 넘지 않는다면
                bridge.append(truck_weights[0]) #트럭이 다리를 건넌다
                truck_weights = truck_weights[1:] #대기 트럭에서 제외
                trucktime.append(0) #건너는 트럭 시간 시작

        if arrivedtrucknum == totaltrucknum:
            break
        
        for i in range(len(trucktime)):
            trucktime[i] = trucktime[i] + 1 #트럭 시간 지남
    
    return totaltime