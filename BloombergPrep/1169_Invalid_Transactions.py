"""
1169. Invalid Transactions
Medium

A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
 

Constraints:

- transactions.length <= 1000
- Each transactions[i] takes the form "{name},{time},{amount},{city}"
- Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
- Each {time} consist of digits, and represent an integer between 0 and 1000.
- Each {amount} consist of digits, and represent an integer between 0 and 2000.
"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = defaultdict(list)

        invalid = [False] * len(transactions)

        for i, transaction in enumerate(transactions):
            [name, time, amount, city] = transaction.split(',')
            previous_transactions = hashmap[name]
            
            if int(amount) > 1000:
                invalid[i] = True

            for t in previous_transactions:
                if abs(int(t['time']) - int(time)) <= 60 and t['city'] != city:
                    invalid[t['index']] = True
                    invalid[i] = True
            
            hashmap[name].append({'time': time, 'city': city, 'index': i})
            
        invalid_transactions = []

        for i in range(len(transactions)):
            if invalid[i]:
                invalid_transactions.append(transactions[i])
        
        return invalid_transactions

