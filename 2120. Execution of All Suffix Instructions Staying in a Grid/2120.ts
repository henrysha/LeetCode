function executeInstructions(
  n: number,
  startPos: number[],
  s: string
): number[] {
  const m = s.length
  const answer = []
  for (let i = 0; i < m; i++) {
    const currPos = [...startPos]
    let j = i
    for (; j < m; j++) {
      move(currPos, s[j])
      if (
        currPos[0] < 0 ||
        currPos[0] >= n ||
        currPos[1] < 0 ||
        currPos[1] >= n
      ) {
        break
      }
    }
    answer.push(j - i)
  }
  return answer
}

const move = (currPos: number[], action: string): void => {
  switch (action) {
    case 'R':
      currPos[1] += 1
      return
    case 'L':
      currPos[1] -= 1
      return
    case 'U':
      currPos[0] -= 1
      return
    case 'D':
      currPos[0] += 1
      return
    default:
      return
  }
}
