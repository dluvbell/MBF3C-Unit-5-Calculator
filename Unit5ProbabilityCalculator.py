class Unit5ProbabilityCalculator:
    def __init__(self):
        print("MBF3C Unit 5: Probability & Everyday Risk Calculator Initialized.\n")

    # ==========================================
    # 5.1 & 5.2: Experimental Data & Odds
    # ==========================================
    def experimental_probability(self, successes, total):
        """Calculates experimental probability. (e.g., 10 successes out of 500 trials)"""
        prob = successes / total
        return round(prob, 3)

    def odds_to_probability(self, win_odds, lose_odds):
        """Converts Odds (Win:Lose) to Probability percentages."""
        total_outcomes = win_odds + lose_odds
        prob_win = win_odds / total_outcomes
        prob_lose = lose_odds / total_outcomes
        return {"Probability of Winning": round(prob_win, 3), "Probability of Failure": round(prob_lose, 3)}

    def probability_to_odds(self, prob_percent):
        """Converts a probability percentage into Odds in Favour and Odds Against."""
        odds_favour = f"{prob_percent}:{100 - prob_percent}"
        odds_against = f"{100 - prob_percent}:{prob_percent}"
        return {"Odds In Favour": odds_favour, "Odds Against": odds_against}

    # ==========================================
    # 5.3 & 5.4: Independent & Dependent Events
    # ==========================================
    def independent_events(self, prob_a, prob_b):
        """Calculates the probability of two completely independent events both occurring."""
        return round(prob_a * prob_b, 3)

    def dependent_without_replacement(self, target_initial, total_initial):
        """
        Calculates the probability of drawing a specific item on the SECOND draw,
        assuming one item of the same type was already drawn and REMOVED (Without Replacement).
        """
        prob_second = (target_initial - 1) / (total_initial - 1)
        return round(prob_second, 3)

    def conditional_rate_increase(self, base_rate, multiplier=None, flat_increase=None):
        """Calculates a new insurance or interest rate based on a dependent event (e.g., an accident)."""
        if multiplier:
            return base_rate * multiplier
        elif flat_increase:
            return base_rate + flat_increase
        return base_rate

    # ==========================================
    # 5.5: Expected Value (EV) & Warranties
    # ==========================================
    def expected_cost(self, item_cost, fail_prob_percent):
        """Calculates the expected mathematical loss of an item breaking or being defective."""
        return round(item_cost * (fail_prob_percent / 100), 2)

    def expected_value_game(self, prob_win_percent, win_amount, loss_amount):
        """Calculates the true Expected Value (EV) of a casino game or financial risk."""
        p_win = prob_win_percent / 100
        p_lose = 1 - p_win
        ev = (p_win * win_amount) - (p_lose * loss_amount)
        return round(ev, 2)

    def expected_warranty_profit(self, warranty_cost, item_cost, fail_prob_percent):
        """Calculates a company's Expected Profit off a customer buying an extended warranty."""
        exp_cost = self.expected_cost(item_cost, fail_prob_percent)
        profit = warranty_cost - exp_cost
        return round(profit, 2)


# --- USAGE EXAMPLES ---
if __name__ == "__main__":
    calc = Unit5ProbabilityCalculator()

    print("--- 1. Probability & Odds ---")
    print(f"Factory defect probability (50 bad out of 2500): {calc.experimental_probability(50, 2500)}")
    print(f"Startup failure probability (Odds 4:16): {calc.odds_to_probability(4, 16)['Probability of Failure']}")
    print(f"Converting 30% rain chance to Odds: {calc.probability_to_odds(30)}")

    print("\n--- 2. Independent & Dependent Events ---")
    print(f"Probability of Machine A (0.8) and B (0.9) both failing: {calc.independent_events(0.8, 0.9)}")
    print(f"Drawing a defective part twice in a row without replacement (started with 4 out of 15): {calc.dependent_without_replacement(4, 15)}")

    print("\n--- 3. Expected Value (EV) & Business ---")
    print(f"Expected Cost of an $800 phone breaking (15% probability): ${calc.expected_cost(800, 15)}")
    print(f"EV of a casino game (10% win chance, win $500, lose $20): ${calc.expected_value_game(10, 500, 20)}")
    print(f"Company's expected profit selling a $200 warranty on an $800 phone (15% failure rate): ${calc.expected_warranty_profit(200, 800, 15)}")