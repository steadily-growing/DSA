"""

Calculator:
    *2          //3

1 -> target

target = 10
1 * 2 * 2 * 2 * 2 * 2 // 3 = 10
res = 6

function
*2 by 2 
increase the counter
if result == target
multiply by 2
increse counter
multiple of 3 and the result > 10

1* 2 steps = 1 value = 2// 3 = 0 
*2 steps+=1  if the value == 10 : return steps
//3 steps+=1 if the value == 10:return steps

                        1
                      2    0  
                    4      0
                8.     1 0     0
            16.    2 2.  0 0.  0 0
         32    5 4. 0. 0. 0. 0. 0. 0 
      64.   10. 0. 0. 0. 0. 0. 0. 0
     
"""

def find_min_steps(target, value, steps):

    s = [1]
    res = 0
    seen = set()
    while s:

        s_len = len(s)

        while s_len:
            curr = s.pop()
            if curr == target:
                return res
            
            s.append(curr*2)
            s.append(curr//3)
            s_len -= 1
            
        res += 1
    

    return res

        














