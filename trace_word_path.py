def trace_word_path(word, grid):
    rows, cols = len(grid), len(grid[0])
    def dfs(r, c, idx, path, visited):
        if idx == len(word):
            return path
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != word[idx] or (r, c) in visited):
            return None
        visited.add((r, c))
        path.append([r, c])
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            result = dfs(r+dr, c+dc, idx+1, path, visited)
            if result:
                return result
        path.pop()
        visited.remove((r, c))
        return None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                result = dfs(r, c, 0, [], set())
                if result:
                    return result
    return "Not present"

print(trace_word_path("BISCUIT", [
  ["B", "I", "T", "R"],
  ["I", "U", "A", "S"],
  ["S", "C", "V", "W"],
  ["D", "O", "N", "E"]
]))

print(trace_word_path("HELPFUL", [
  ["L","I","T","R"],
  ["U","U","A","S"],
  ["L","U","P","O"],
  ["E","F","E","H"]
]))

print(trace_word_path("UKULELE", [
  ["N", "H", "B", "W"],
  ["E", "X", "A", "D"],
  ["L", "A", "U", "U"],
  ["E", "L", "U", "K"]
]))

print(trace_word_path("SURVIVAL", [
  ["V", "L", "R", "L"],
  ["V", "A", "I", "V"],
  ["I", "O", "S", "C"],
  ["V", "R", "U", "F"]
]))
