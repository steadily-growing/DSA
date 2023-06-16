class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # convert jewel to a dictionary, check if the char in stones is in jewels then icrement counter else continue end the looop and return counter
        jewel_dict={}
        counter = 0
        

        for i in jewels:
            jewel_dict[i] = 0
            

        for char in stones:
            if char in jewel_dict:
                counter+=1
        return counter