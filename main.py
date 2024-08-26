from app.even_odd import check  # Import the function directly

def main():
    import sys
    if len(sys.argv) > 2:
        print("Usage: main.py [number]")
        sys.exit(1)
    
    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer.")
            sys.exit(1)
    else:
        number = 50  # Default number
    
    result = check(number)  # Use the function directly
    print(f"The number {number} is {'even' if result else 'odd'}.")

if __name__ == "__main__":
    main()
