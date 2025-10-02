class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        Calculates the maximum number of water bottles that can be drunk
        given initial full bottles and an exchange rate that increases.

        Args:
            numBottles: The initial number of full water bottles.
            numExchange: The initial number of empty bottles required for an exchange.

        Returns:
            The maximum total number of bottles drunk.
        """
        
        total_drunk_bottles = 0
        empty_bottles = 0
        
        # Step 1: Drink all initial full bottles
        total_drunk_bottles += numBottles
        empty_bottles += numBottles
        
        # numBottles is now 0 as they are all drunk
        
        # Step 2: Loop to perform exchanges as long as possible
        while empty_bottles >= numExchange:
            # Perform one exchange
            empty_bottles -= numExchange  # Use up 'numExchange' empty bottles
            total_drunk_bottles += 1      # Get and drink one new full bottle
            empty_bottles += 1            # The new bottle becomes empty
            
            numExchange += 1              # The exchange rate increases by 1
            
        return total_drunk_bottles
