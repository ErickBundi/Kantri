class Rectangle:
    """A class to represent a rectangle with height and width properties."""
    
    def __init__(self, height, width):
        """
        Initialize a Rectangle object.
        
        Args:
            height (int): The height of the rectangle
            width (int): The width of the rectangle
        """
        self.height = height
        self.width = width
    
    def calculate_perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            int: The perimeter (2 * height + 2 * width)
        """
        return 2 * self.height + 2 * self.width
    
    def calculate_area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            int: The area (height * width)
        """
        return self.height * self.width
    
    def print_rectangle(self):
        """
        Print a visual representation of the rectangle using asterisks.
        """
        # Print top border
        print("*" * self.width)
        
        # Print middle rows
        for _ in range(self.height - 2):
            print("*" + " " * (self.width - 2) + "*")
        
        # Print bottom border
        print("*" * self.width)
    
    def display_info(self):
        """
        Display all information about the rectangle in the format shown in the screenshot.
        """
        print("Rectangle Calculator")
        print(f"Height: {self.height}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.calculate_perimeter()}")
        print(f"Area: {self.calculate_area()}")
        self.print_rectangle()


def main():
    """Main function to run the Rectangle Calculator program."""
    while True:
        try:
            # Get user input for height and width
            height = int(input("\nEnter height: "))
            width = int(input("Enter width: "))
            
            # Validate input
            if height <= 0 or width <= 0:
                print("Please enter positive numbers for height and width.")
                continue
            
            # Create rectangle object and display info
            rect = Rectangle(height, width)
            rect.display_info()
            
            # Ask if user wants to continue
            while True:
                continue_choice = input("\nContinue? (y/n): ").lower().strip()
                if continue_choice in ['y', 'n']:
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            
            if continue_choice == 'n':
                print("Thank you for using Rectangle Calculator!")
                break
        
        except ValueError:
            print("Invalid input. Please enter whole numbers for height and width.")


if __name__ == "__main__":
    main()
