def main():
    match_odds = {
        "home": 1.55,
        "draw": 4.2,
        "away": 5.72
    }
    if is_arbitrage(match_odds) == True:
        print("Arbitrage Opportunity!")
    else:
        print("No arbitrage opportunity")

# odds consist of a three-item list for each possible outcome: home, draw, away

def is_arbitrage (odds):
    """Check if given odds offer an arbitrage opportunity"""
    total_prob = sum(1/odds[odd] for odd in odds)
    # return True if so
    if total_prob < 1:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()