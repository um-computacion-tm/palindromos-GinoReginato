def is_palindrome(mystring):
    cleaned_string = mystring.replace(" ", "").lower()
    for indice in range(len(cleaned_string)):
        if cleaned_string[indice] != cleaned_string[-(indice + 1)]:
            print("no es")
            return False
    print("es")
    return True
