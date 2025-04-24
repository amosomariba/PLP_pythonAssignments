try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))

    result = numerator / denominator


except ZeroDivisionError as e:
    print(f"You cannot devide by 0!! {e}")

except ValueError as e:
    print(f"You entered an invilid value {e} ")


except Exception as e:
    print("There has been an error please try again!! {e}")


finally:
    print("Thanks for using my program")
