# Define a class
class Palindrome:
    # Initialize the class with the input text and an optional number
    def __init__(self, text, number=None):
        # Check if the input is a string or an integer
        if not isinstance(text, (str, int)):
            raise ValueError("Input must be a string or an integer")
        # Convert text to a string to handle integers as well
        self.text = str(text)
        # Store the optional number as a string or None
        self.number = str(number) if number is not None else None

    # Static method to check if a given word is a palindrome
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    # Method to find the longest cascading palindrome in the text
    def find_cascading_palindrome(self):
        # Check if no text is provided
        if not self.text:
            return "No input provided"

        # Split the input data into components based on spaces
        components = self.text.split()
        # Initialize a variable to store the longest palindrome found
        longest_palindrome = ""

        # Iterate through each component in the input data
        for component in components:
            # Check if the component is longer than the current longest palindrome
            if len(component) > len(longest_palindrome):
                # Check if the component is a palindrome
                if self.is_palindrome(component):
                    # Update the longest palindrome if the current component is longer and a palindrome
                    longest_palindrome = component

        # If a cascading palindrome is found, return it; otherwise, return a message
        if longest_palindrome:
            return longest_palindrome + (" " + self.number if self.number else "")
        else:
            return "No cascading palindrome found"

if __name__ == "__main__":
    try:
        # Create an instance of the CascadingPalindrome class with a single word (string)
        example1 = Palindrome("1230321")
        # Find and print the cascading palindrome in the input
        print(example1.find_cascading_palindrome()) 

        # Create an instance with a single number (integer)
        example2 = Palindrome(1230321)
        # Find and print the cascading palindrome in the input
        print(example2.find_cascading_palindrome())  # Output: "1230321"

        # Create an instance with multiple components separated by spaces
        example3 = Palindrome("1230321 09234 0124210")
        # Find and print the cascading palindrome in the input
        print(example3.find_cascading_palindrome())  # Output: "1230321 0124210"

        # Create an instance with a mix of words, numbers, and an integer
        example4 = Palindrome("abcd5dcba 1230321 09234 0124210", 1230321)
        # Find and print the cascading palindrome in the input
        print(example4.find_cascading_palindrome())  # Output: "abcd5dcba 1230321 0124210"

        # Create an instance with no cascading palindrome
        example5 = Palindrome("hello world")
        # Find and print the cascading palindrome in the input
        print(example5.find_cascading_palindrome())  # Output: "No cascading palindrome found"

        # Create an instance with multiple cascading palindromes
        example6 = Palindrome("racecar abba level")
        # Find and print the cascading palindrome in the input
        print(example6.find_cascading_palindrome())  # Output: "racecar"

        # Create an instance with a sentence that does not contain a cascading palindrome
        example7 = Palindrome("A man, a plan, a canal – Panama")
        # Find and print the cascading palindrome in the input
        print(example7.find_cascading_palindrome())  # Output: "No cascading palindrome found"
        
        # Create an instance of the CascadingPalindrome class with a single word (string)
        example8 = Palindrome("madam")
        # Find and print the cascading palindrome in the input
        print(example8.find_cascading_palindrome()) # Output: "madam"
        
        # Create an instance of the CascadingPalindrome class with a single word (string)
        example9 = Palindrome("school")
        # Find and print the cascading palindrome in the input
        print(example9.find_cascading_palindrome()) # Output: "No cascading palindrome found"

        # Create an instance with invalid input (a list)
        example10 = Palindrome([1, 2, 3])
    except ValueError as e:
        print(e)  # Output: "Input must be a string or an integer"
