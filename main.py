import threading
import time
# Ensure Python finds the `agents` module

from agent_a import generate_synthetic_data
from agent_b import simulate_scenario
from agent_d import generate_insights

def main():
    """ Orchestrates agent execution. """
    scenario = input("Enter business scenario: ")
    num_rows = int(input("Enter number of rows: "))

    # Generate synthetic data
    df = generate_synthetic_data(scenario, num_rows)
    if df is None:
        print("❌ Data generation failed. Exiting.")
        return

    # Run agents in parallel
    thread1 = threading.Thread(target=simulate_scenario, args=(df,))
    thread2 = threading.Thread(target=generate_insights, args=(df, scenario))

    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    end_time = time.time()

    print(f"\n✅ Execution completed in {round(end_time - start_time, 2)} seconds.")

if __name__ == "__main__":
    main()