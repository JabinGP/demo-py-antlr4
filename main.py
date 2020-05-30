import sys
from antlr4 import *
from parser.CalLexer import CalLexer
from parser.CalParser import CalParser
from parser.CalVisitor import CalVisitor


class EvalVisitor(CalVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx: CalParser.AssignContext):
        text = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[text] = value
        return value

    def visitPrintExpr(self, ctx: CalParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx: CalParser.IntContext):
        return int(ctx.INT().getText())

    def visitId(self, ctx: CalParser.IdContext):
        text = ctx.ID().getText()
        if self.memory.__contains__(text):
            return self.memory[text]
        return 0

    def visitMulDiv(self, ctx: CalParser.MulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if (ctx.op.type == CalParser.MUL):
            return left * right

        return left/right

    def visitAddSub(self, ctx: CalParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        if (ctx.op.type == CalParser.ADD):
            return left + right

        return left - right

    def visitParens(self, ctx: CalParser.ParensContext):
        return self.visit(ctx.expr())


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CalLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalParser(stream)
    tree = parser.prog()

    evalVisitor = EvalVisitor()

    evalVisitor.visit(tree)


if __name__ == '__main__':
    main(sys.argv)
