import sys
import json
import os

VOTES_FILE = "votes.json"

# Initialize data file if it doesn't exist
if not os.path.exists(VOTES_FILE):
    with open(VOTES_FILE, 'w') as f:
        json.dump({}, f)

def load_votes():
    with open(VOTES_FILE, 'r') as f:
        return json.load(f)

def save_votes(votes):
    with open(VOTES_FILE, 'w') as f:
        json.dump(votes, f, indent=2)

def add_candidate(name):
    votes = load_votes()
    if name in votes:
        print(f"Candidate '{name}' already exists.")
    else:
        votes[name] = 0
        save_votes(votes)
        print(f"Candidate '{name}' added.")

def vote(candidate):
    votes = load_votes()
    if candidate in votes:
        votes[candidate] += 1
        save_votes(votes)
        print(f"🗳 Vote cast for '{candidate}'")
    else:
        print(f"Candidate '{candidate}' does not exist.")

def show_results():
    votes = load_votes()
    if not votes:
        print("No candidates found.")
        return
    print("Voting Results:")
    for candidate, count in votes.items():
        print(f" - {candidate}: {count} votes")

def reset_votes():
    save_votes({})
    print("All votes have been reset.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python voting.py add <candidate>")
        print("  python voting.py vote <candidate>")
        print("  python voting.py results")
        print("  python voting.py reset")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add" and len(sys.argv) == 3:
        add_candidate(sys.argv[2])
    elif command == "vote" and len(sys.argv) == 3:
        vote(sys.argv[2])
    elif command == "results":
        show_results()
    elif command == "reset":
        reset_votes()
    else:
        print("Invalid command or arguments.")

