import decisions

def main():
    options_selected = int(input("Enter the number of options selected: "))
    total_options = int(input("Enter the total number of options: "))

    ratio = decisions.get_options_ratio(options_selected, total_options) 

    rating = decisions.get_faculty_rating(ratio)

    print(f"Faculty Rating: {rating}")
main()


    
