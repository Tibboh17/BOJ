def solution(sizes):
    sorted_sizes = []
    width = []
    height = []
    
    for size in sizes:
        size.sort()
        sorted_sizes.append(size)
    
    for size in sorted_sizes:
        width.append(size[0])
        height.append(size[1])
        
    answer = max(width) * max(height)
    
    return answer