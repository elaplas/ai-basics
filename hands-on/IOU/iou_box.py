# Find the intersection over union of two bounding boxes


def IOU(box1, box2):

    p1_1 = box1[0]
    p1_2 = box1[1]

    p2_1 = box2[0]
    p2_2 = box2[1]

    # box2 is on the left side of box1 without intersection 
    if p2_2[0] <= p1_1[0] or p2_1[0] >= p1_2[0]:
        return 0
    # box2 is on the right side of box1 without intersection 
    if p2_2[1] <= p1_1[1] or p2_1[1] >= p1_2[1]:
        return 0

    # x-coordinates of intersection region
    x_1 = max(p1_1[0], p2_1[0])
    x_2 = min(p1_2[0], p2_2[0])

    # y-coordinate of intersection region
    y_1 = max(p1_1[1], p2_1[1])
    y_2 = min(p1_2[1], p2_2[1])

    union = (p1_2[0] - p1_1[0])*(p1_2[1] - p1_1[1])  +  (p2_2[0] - p2_1[0])*(p2_2[1] - p2_1[1])
    intersection = (x_2-x_1)*(y_2 - y_1) 

    return  intersection / union


box1=[[3,4], [6,8]]
box2=[[4,2], [10,6]]

res = IOU(box1, box2)
print(res)



box1=[[3,4], [6,8]]
box2=[[7,2], [13,6]]

res = IOU(box1, box2)
print(res)