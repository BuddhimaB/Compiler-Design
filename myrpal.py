import sys
from lexer import *
from parser import *

def main():
    # Check if the correct number of arguments is provided
    entered_ast = False
    rpal_program = ''
    
    if len(sys.argv) < 2:
        print("Usage: python myrpal.py file_name")
        sys.exit(1)
        
    else:
        entered_ast = False
        # Read the input file
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as file:
                rpal_program = file.read()
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
            sys.exit(1)
               
    
        if len(sys.argv) > 2:
            if sys.argv[2] == '-ast':
                entered_ast = True
            else:
                print('Invalid Command')
                sys.exit(1)
    

      
    
    # =====================================================
    # Initialize lexer and parser
    token_list = lexer(rpal_program)
    
    ast = parser(token_list, entered_ast)
    print(ast)
    
    # # Parse the input program and generate AST
    # try:
    #     ast = parser.parse()
    # except Exception as e:
    #     print(f"Error parsing input program: {e}")
    #     sys.exit(1)
    
    # # Print AST
    # print(ast)

if __name__ == "__main__":
    main()
