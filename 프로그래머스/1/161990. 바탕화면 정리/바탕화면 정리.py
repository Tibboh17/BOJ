def solution(wallpaper):
    answer = []
    x_list = []
    y_list = []
    
    for i in range(len(wallpaper)):
        row = wallpaper[i]
        for j in range(len(row)):
            cell = row[j]
            if cell == "#":
                x_list.append(i)
                y_list.append(j)
                
    answer.append(min(x_list))
    answer.append(min(y_list))
    answer.append(max(x_list) + 1)
    answer.append(max(y_list) + 1)
    
    return answer