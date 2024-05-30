from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        hashMap = defaultdict(list)

        for tnx in transactions:
            name, time, amount, city = tnx.split(",")
            hashMap[name].append([int(time), amount, city])  # Convert time to integer for numerical comparison

        for tnx in transactions:
            name, time1, amount1, city1 = tnx.split(",")
            time1 = int(time1)

            if int(amount1) > 1000:
                res.append(tnx)
            else:
                for time2, amount2, city2 in hashMap[name]:
                    if city1 != city2 and abs(time1 - time2) <= 60:
                        res.append(tnx)
                        break  # Break the loop once an invalid transaction is found for the same name

        return res
