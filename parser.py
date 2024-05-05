import Lexx
from Lexx import tokens

token_index = 0
token_list = tokens

# token_list = [('<KEYWORD>', 'let'), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'A'),
#               ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('),
#               ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'Order'), ('<IDENTIFIER>', 'A'),
#               ('<PUNCTUATION>', ')'), ('<KEYWORD>', 'where'), ('<KEYWORD>', 'rec'), ('<IDENTIFIER>', 'Psum'),
#               ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'N'),
#               ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'eq'),
#               ('<INTEGER>', '0'), ('<OPERATOR>', '->'), ('<INTEGER>', '0'), ('<OPERATOR>', '|'),
#               ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','),
#               ('<IDENTIFIER>', 'N'), ('<OPERATOR>', '-'), ('<INTEGER>', '1'), ('<PUNCTUATION>', ')'),
#               ('<OPERATOR>', '+'), ('<IDENTIFIER>', 'T'), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'in'),
#               ('<IDENTIFIER>', 'Print'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('),
#               ('<INTEGER>', '1'), ('<PUNCTUATION>', ','), ('<INTEGER>', '2'), ('<PUNCTUATION>', ','),
#               ('<INTEGER>', '3'), ('<PUNCTUATION>', ','), ('<INTEGER>', '4'), ('<PUNCTUATION>', ','),
#               ('<INTEGER>', '5'), ('<PUNCTUATION>', ')'), ('<PUNCTUATION>', ')')]


token_list.append("END")
nextToken = token_list[token_index]
def read(token):
    global nextToken
    global token_index
    if nextToken[1]==token:
        print(f"{token} read success")
        print("Success")
        token_index+=1
        nextToken=token_list[token_index]
    else:
        print("error")

def E():
    if nextToken[1] == "let":
        read("let")
        D()
        read("in")
        E()
    elif nextToken[1] == "fn":
        read("fn")
        Vb()
        while nextToken[0] == "<IDENTIFIER>" or (nextToken[0] == "<PUNCTUATION>" and nextToken[1] == "("):
            Vb()
        read(".")
        E()
    else:
        Ew()






def D():
    Da()
    if nextToken[1] == "within":
        read("within")
        D()



def Vb():
    if nextToken[0] == "<IDENTIFIER>":
        read(nextToken[1])

    elif nextToken[1] == "(":
        read("(")

        if nextToken[0] == "<IDENTIFIER>":
            Vl()
            read(")")
        elif nextToken[0] == ")":
            read(")")

    else:
        print("error in Vb")


def Ew():
    T()
    if nextToken[1] == 'where':
        read('where')
        Dr()
def T():
    Ta()
    while(nextToken[0] == '<PUNCTUATION>' and nextToken[1]==','):
        read(",")
        Ta()
def Ta():
    Tc()
    while nextToken[1] == "aug":
        read("aug")
        Tc()


def Tc():
    B()
    if nextToken[0] == "<OPERATOR>" and nextToken[1] == "->":
        read("->")
        Tc()
        read("|")
        Tc()
def B():
    Bt()
    if nextToken[1] == "or":
        read("or")
        Bt()


def Bt():
    Bs()
    if nextToken[1] == "&":
        read("&")
        Bt()
def Bs():
    if nextToken[1] == "not":
        read("not")
    Bp()

def Bp():
    A()
    if nextToken[1] == "gr" or nextToken[1] == ">":
        read(nextToken[1])
        A()
    elif nextToken[1] == "ge" or nextToken[1] == ">=":
        read(nextToken[1])
        A()
    elif nextToken[1] == "ls" or nextToken[1] == "<":
        read(nextToken[1])
        A()
    elif nextToken[1] == "le" or nextToken[1] == "<=":
        read(nextToken[1])
        A()
    elif nextToken[1] == "eq":
        read("eq")
        A()
    elif nextToken[1] == "ne":
        read("ne")
        A()

def A():  # check later
    if nextToken[1] == "+":
        read("+")
        At()
    elif nextToken[1] == "-":
        read("-")
        At()
    else:
        At()
        while nextToken[1] in ("+", "-"):
            if nextToken[1] == "+":
                read("+")
                At()
            if nextToken[1] == "-":
                read("-")
                At()
def At():
    Af()
    while nextToken[1] in ("*", "/"):
        if nextToken[1] == "*":
            read("*")
            Af()
        if nextToken[1] == "/":
            read("/")
            Af()


def Af():
    Ap()
    if nextToken[1] == "":
        read("")
        Af()
def Ap():
    R()

    while nextToken[1] == "@":
        read("@")
        if nextToken[0] == "<IDENTIFIER>":
            read(nextToken[1])
            R()
        else:
            print("Error parsing Ap")


def R():
    Rn()
    while nextToken[0] in ("<IDENTIFIER>", "<INTEGER>", "<STRING>") or nextToken[1] in (
    'true', 'false', 'nil', '(', "dummy"):
        Rn()
        
def Rn():
    if nextToken[1] == "true":
        read("true")

    elif nextToken[1] == "false":
        read("false")

    elif nextToken[1] == "nil":
        read("nil")

    elif nextToken[1] == "dummy":
        read("dummy")

    elif nextToken[0] in ("<IDENTIFIER>", "<INTEGER>", "<STRING>"):
        read(nextToken[1])

    elif nextToken[1] == "(":
        read("(")
        E()
        read(")")
    else:
        pass




def Da():
    Dr()
    while nextToken[1] == "and":
        read("and")
        Dr()


def Dr():
    if nextToken[1] == "rec":
        read("rec")
        Db()

    else:
        Db()
def Db():
    if nextToken[0] == "<IDENTIFIER>":
        read(nextToken[1])
        if nextToken[0] == "<IDENTIFIER>" or nextToken[1] == "(":
            Vb()

        while nextToken[0] == "<IDENTIFIER>" or nextToken[1] == "(":
            Vb()

        if nextToken[1] == "=":
            read("=")
            E()

        else:
            print("Error in Db")

    elif nextToken[1] == "(":
        read("(")
        D()
        read(")")

    else:
        Vl()
        read("=")
        E()

def Vl():
    count = 0
    while nextToken[0] == "<IDENTIFIER>":
        read(nextToken[1])
        count = count + 1
        if nextToken[1] == ",":
            read(",")

        elif nextToken[0] == "<IDENTIFIER>":
            print("error in Vl")

    if count == 0:
        print("error in Vl")


E()
print(nextToken)