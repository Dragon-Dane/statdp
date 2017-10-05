class Block:
    def __init__(self, statements):
        self.statements = statements


class Function:
    def __init__(self, declaration, body):
        self.declaration = declaration
        self.body = body


class FunctionDeclaration:
    def __init__(self, name, args, returns):
        self.name = name
        self.args = args
        self.returns = returns


class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class If:
    def __init__(self, condition, body, else_body):
        self.condition = condition
        self.body = body
        self.else_body = else_body


class TypeDeclaration:
    def __init__(self, names, type):
        self.names = names
        self.type = type


class Type:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class BinaryOperation:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class UnaryOperation:
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand


class Variable:
    def __init__(self, name):
        self.name = name


class Real:
    def __init__(self, value):
        self.value = value


class Boolean:
    def __init__(self, value):
        self.value = value


class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args


class ListIndex:
    def __init__(self, name, index):
        self.name = name
        self.index = index


class ConditionalVariable:
    def __init__(self, condition, true, false):
        self.condition = condition
        self.true = true
        self.false = false


class Assign:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
