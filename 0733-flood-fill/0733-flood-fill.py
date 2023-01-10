class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [(sr, sc)]
        origin_color = image[sr][sc]
        len_x, len_y = len(image), len(image[0])
        while len(queue) != 0:
            x, y = queue.pop()
            if image[x][y] == origin_color and image[x][y] != color:
                image[x][y] = color
                if x < len_x-1:
                    queue.append((x+1, y))
                if x > 0:
                    queue.append((x-1, y))
                if y < len_y-1:
                    queue.append((x, y+1))
                if y > 0:
                    queue.append((x, y-1))
        return image