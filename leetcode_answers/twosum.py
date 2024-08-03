def twoSum(nums: list[int], target: int):

        buffer = [0, 0]
        position = [0,0]
        
        for i, u in enumerate(nums):

            if sum(buffer) == target:
                return(result)
            
            else:
                buffer.append(u)
                buffer = buffer[1:]
                
                position.append(i)
                position = position[1:]

                result = position