import os
import sys
import datetime

introductory_problems = [
    "Weird Algorithm", "Missing Number", "Repetitions", "Increasing Array", "Permutations",
    "Number Spiral", "Two Knights", "Two Sets", "Bit Strings", "Trailing Zeros", "Coin Piles",
    "Palindrome Reorder", "Gray Code", "Tower of Hanoi", "Creating Strings", "Apple Division",
    "Chessboard and Queens", "Digit Queries", "Grid Paths"
]

sorting_and_searching = [
    "Distinct Numbers", "Apartments", "Ferris Wheel", "Concert Tickets", "Restaurant Customers",
    "Movie Festival", "Sum of Two Values", "Maximum Subarray Sum", "Stick Lengths", "Missing Coin Sum",
    "Collecting Numbers", "Collecting Numbers II", "Playlist", "Towers", "Traffic Lights",
    "Josephus Problem I", "Josephus Problem II", "Nested Ranges Check", "Nested Ranges Count",
    "Room Allocation", "Factory Machines", "Tasks and Deadlines", "Reading Books", "Sum of Three Values",
    "Sum of Four Values", "Nearest Smaller Values", "Subarray Sums I", "Subarray Sums II",
    "Subarray Divisibility", "Subarray Distinct Values", "Array Division", "Sliding Window Median",
    "Sliding Window Cost", "Movie Festival II", "Maximum Subarray Sum II"
]

dynamic_programming = [
    "Dice Combinations", "Minimizing Coins", "Coin Combinations I", "Coin Combinations II",
    "Removing Digits", "Grid Paths", "Book Shop", "Array Description", "Counting Towers",
    "Edit Distance", "Rectangle Cutting", "Money Sums", "Removal Game", "Two Sets II",
    "Increasing Subsequence", "Projects", "Elevator Rides", "Counting Tilings", "Counting Numbers"
]

graph_algorithms = [
    "Counting Rooms", "Labyrinth", "Building Roads", "Message Route", "Building Teams",
    "Round Trip", "Monsters", "Shortest Routes I", "Shortest Routes II", "High Score",
    "Flight Discount", "Cycle Finding", "Flight Routes", "Round Trip II", "Course Schedule",
    "Longest Flight Route", "Game Routes", "Investigation", "Planets Queries I", "Planets Queries II",
    "Planets Cycles", "Road Reparation", "Road Construction", "Flight Routes Check",
    "Planets and Kingdoms", "Giant Pizza", "Coin Collector", "Mail Delivery", "De Bruijn Sequence",
    "Teleporters Path", "Hamiltonian Flights", "Knight's Tour", "Download Speed", "Police Chase",
    "School Dance", "Distinct Routes"
]

range_queries = [
    "Static Range Sum Queries", "Static Range Minimum Queries", "Dynamic Range Sum Queries",
    "Dynamic Range Minimum Queries", "Range Xor Queries", "Range Update Queries", "Forest Queries",
    "Hotel Queries", "List Removals", "Salary Queries", "Prefix Sum Queries", "Pizzeria Queries",
    "Subarray Sum Queries", "Distinct Values Queries", "Increasing Array Queries", "Forest Queries II",
    "Range Updates and Sums", "Polynomial Queries", "Range Queries and Copies"
]

tree_algorithms = [
    "Subordinates", "Tree Matching", "Tree Diameter", "Tree Distances I", "Tree Distances II",
    "Company Queries I", "Company Queries II", "Distance Queries", "Counting Paths", "Subtree Queries",
    "Path Queries", "Path Queries II", "Distinct Colors", "Finding a Centroid", "Fixed-Length Paths I",
    "Fixed-Length Paths II"
]

mathematics = [
    "Josephus Queries", "Exponentiation", "Exponentiation II", "Counting Divisors", "Common Divisors",
    "Sum of Divisors", "Divisor Analysis", "Prime Multiples", "Counting Coprime Pairs",
    "Binomial Coefficients", "Creating Strings II", "Distributing Apples", "Christmas Party",
    "Bracket Sequences I", "Bracket Sequences II", "Counting Necklaces", "Counting Grids",
    "Fibonacci Numbers", "Throwing Dice", "Graph Paths I", "Graph Paths II", "Dice Probability",
    "Moving Robots", "Candy Lottery", "Inversion Probability", "Stick Game", "Nim Game I",
    "Nim Game II", "Stair Game", "Grundy's Game", "Another Game"
]

string_algorithms = [
    "Word Combinations", "String Matching", "Finding Borders", "Finding Periods", "Minimal Rotation",
    "Longest Palindrome", "Required Substring", "Palindrome Queries", "Finding Patterns",
    "Counting Patterns", "Pattern Positions", "Distinct Substrings", "Repeating Substring",
    "String Functions", "Substring Order I", "Substring Order II", "Substring Distribution"
]

geometry = [
    "Point Location Test", "Line Segment Intersection", "Polygon Area", "Point in Polygon",
    "Polygon Lattice Points", "Minimum Euclidean Distance", "Convex Hull"
]

advanced_techniques = [
    "Meet in the Middle", "Hamming Distance", "Beautiful Subgrids", "Reachable Nodes",
    "Reachability Queries", "Cut and Paste", "Substring Reversals", "Reversals and Sums",
    "Necessary Roads", "Necessary Cities", "Eulerian Subgraphs", "Monster Game I", "Monster Game II",
    "Subarray Squares", "Houses and Schools", "Knuth Division", "Apples and Bananas",
    "One Bit Positions", "Signal Processing", "New Roads Queries", "Dynamic Connectivity",
    "Parcel Delivery", "Task Assignment", "Distinct Routes II"
]

additional_problems = [
    "Shortest Subsequence", "Counting Bits", "Swap Game", "Prüfer Code", "Acyclic Graph Edges",
    "Strongly Connected Edges", "Even Outdegree Edges", "Multiplication Table", "Advertisement",
    "Special Substrings", "Permutation Inversions", "Maximum Xor Subarray", "Movie Festival Queries",
    "Chess Tournament", "Tree Traversals", "Network Renovation", "Graph Girth", "Intersection Points",
    "Inverse Inversions", "Monotone Subsequences", "String Reorder", "Stack Weights", "Pyramid Array",
    "Increasing Subsequence II", "String Removals", "Bit Inversions", "Xor Pyramid", "Writing Numbers",
    "String Transform", "Letter Pair Move Game", "Maximum Building I", "Sorting Methods", "Cyclic Array",
    "List of Sums", "Increasing Array II", "Food Division", "Bit Problem", "Swap Round Sorting",
    "Binary Subsequences", "Tree Isomorphism I", "Counting Sequences", "Critical Cities",
    "School Excursion", "Coin Grid", "Robot Path", "Programmers and Artists", "Course Schedule II",
    "Removing Digits II", "Coin Arrangement", "Counting Bishops", "Grid Puzzle I", "Grid Puzzle II",
    "Empty String", "Grid Paths", "Bit Substrings", "Reversal Sorting", "Counting Reorders",
    "Book Shop II", "Network Breakdown", "Visiting Cities", "Missing Coin Sum Queries", "Number Grid",
    "Maximum Building II", "Filling Trominos", "Stick Divisions", "Coding Company", "Flight Route Requests",
    "Two Stacks Sorting", "Tree Isomorphism II", "Forbidden Cities", "Area of Rectangles", "Grid Completion",
    "Creating Offices", "Permutations II", "Functional Graph Distribution", "New Flight Routes",
    "Grid Path Construction"
]

problem_sets = {
    "Introductory Problems": introductory_problems,
    "Sorting and Searching": sorting_and_searching,
    "Dynamic Programming": dynamic_programming,
    "Graph Algorithms": graph_algorithms,
    "Range Queries": range_queries,
    "Tree Algorithms": tree_algorithms,
    "Mathematics": mathematics,
    "String Algorithms": string_algorithms,
    "Geometry": geometry,
    "Advanced Techniques": advanced_techniques,
    "Additional Problems": additional_problems
}

def choose_problem_set():
    print("=== Choose a Problem Set ===")
    for i, set_name in enumerate(problem_sets.keys(), 1):
        print(f"{i}. {set_name}")
    choice = int(input("Enter the number of the problem set: "))
    set_name = list(problem_sets.keys())[choice - 1]
    return set_name, problem_sets[set_name]

def choose_problem(questions):
    print("=== Choose a Question ===")
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
    choice = int(input("Enter the number of the question: "))
    return questions[choice - 1]

def get_constraints():
    num_constraints = int(input("Enter the number of constraints: "))
    constraints = []
    for i in range(num_constraints):
        constraint = input(f"Enter constraint {i + 1}: ")
        constraints.append(constraint)
    return constraints

def get_header_details():
    print("=== Provide Details for the Header Comment ===")
    set_name, questions = choose_problem_set()
    question = choose_problem(questions)
    author = "andy41027"
    date_created = datetime.datetime.now().strftime("%Y-%m-%d")
    description = input("Enter a brief question description: ")
    constraints = get_constraints()

    notes = input("Enter additional notes (optional, press Enter to skip): ")

    header = "/*******************************************************\n"
    header += f" * Question set:     {set_name}\n"
    header += f" * Question :        {question}\n"
    header += f" * Author:           {author}\n"
    header += f" * Date Created:     {date_created}\n"
    header += f" * Description:      {description}\n"
    if constraints:
        header += f" * Constraints:      {constraints[0]}\n"
        for constraint in constraints[1:]:
            header += f" *                   {constraint}\n"
    if notes:
        header += f" * Notes:            {notes}\n"
    header += " *******************************************************/\n\n"
    return header

def prepend_header(file_name, header):
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' does not exist.")
        return

    with open(file_name, 'r') as file:
        content = file.read()

    if content.startswith("/*"):
        end_of_comment = content.find("*/") + 2
        content = content[end_of_comment:].lstrip()
    with open(file_name, 'w') as file:
        file.write(header + content)

    print(f"Header successfully added to '{file_name}'.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python prepend_script.py <file_name>")
        sys.exit(1)
    file_name = sys.argv[1]
    header = get_header_details()
    prepend_header(file_name, header)
